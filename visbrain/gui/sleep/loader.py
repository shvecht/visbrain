"""Asynchronous helpers for loading sleep datasets."""
from __future__ import annotations

import logging
from concurrent.futures import Future, ThreadPoolExecutor
from typing import Any, Callable, Optional

try:  # pragma: no cover - optional Qt dependency
    from visbrain.qt import QtCore, QtWidgets
except Exception:  # pragma: no cover - optional Qt dependency
    QtCore = QtWidgets = None  # type: ignore[assignment]

logger = logging.getLogger("visbrain")


def call_on_main_thread(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    """Execute *func* on the Qt GUI thread and return its result."""

    if QtCore is None or QtWidgets is None:
        return func(*args, **kwargs)

    app = QtWidgets.QApplication.instance()
    if app is None:
        return func(*args, **kwargs)

    gui_thread = app.thread()
    if gui_thread is None or gui_thread is QtCore.QThread.currentThread():
        return func(*args, **kwargs)

    class _Invoker(QtCore.QObject):
        def __init__(self) -> None:
            super().__init__()
            self._result: Any = None
            self._error: Optional[BaseException] = None

        @QtCore.Slot()
        def invoke(self) -> None:  # pragma: no cover - executed on GUI thread
            try:
                self._result = func(*args, **kwargs)
            except BaseException as exc:  # pragma: no cover - defensive
                self._error = exc

        def result(self) -> Any:
            if self._error is not None:
                raise self._error
            return self._result

    proxy = _Invoker()
    proxy.moveToThread(gui_thread)
    QtCore.QMetaObject.invokeMethod(
        proxy,
        "invoke",
        QtCore.Qt.BlockingQueuedConnection,
    )
    return proxy.result()


class AsyncSleepLoader:
    """Load :class:`~visbrain.io.read_sleep.ReadSleepData` objects in a thread."""

    def __init__(self, *, max_workers: int = 1) -> None:
        self._executor = ThreadPoolExecutor(
            max_workers=max_workers,
            thread_name_prefix="sleep-loader",
        )

    def shutdown(self) -> None:
        """Shut down the executor without blocking test teardown."""

        self._executor.shutdown(wait=False)

    def submit(
        self,
        function: Callable[..., Any],
        *args: Any,
        on_result: Callable[[Any], None] | None = None,
        on_error: Callable[[BaseException], None] | None = None,
        **kwargs: Any,
    ) -> Future:
        """Submit *function* to the loader and optionally register callbacks."""

        future: Future = self._executor.submit(function, *args, **kwargs)

        if on_result is not None or on_error is not None:
            def _callback(done: Future) -> None:
                try:
                    result = done.result()
                except BaseException as exc:  # pragma: no cover - error path
                    if on_error is not None:
                        call_on_main_thread(on_error, exc)
                    else:
                        logger.exception("Asynchronous sleep load failed", exc_info=exc)
                    return
                if on_result is not None:
                    call_on_main_thread(on_result, result)

            future.add_done_callback(_callback)

        return future
