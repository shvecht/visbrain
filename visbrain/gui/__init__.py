"""Public entrypoints for the :mod:`visbrain.gui` package."""

__all__ = ["Sleep", "SleepDataset", "Brain", "Signal", "Figure"]


def __getattr__(name):
    if name == "Sleep":
        from .sleep import Sleep
        return Sleep
    if name == "SleepDataset":
        from .sleep.model import SleepDataset
        return SleepDataset
    if name == "Brain":
        from .brain import Brain
        return Brain
    if name == "Signal":
        from .signal import Signal
        return Signal
    if name == "Figure":
        from .figure import Figure
        return Figure
    raise AttributeError(f"module 'visbrain.gui' has no attribute {name!r}")
