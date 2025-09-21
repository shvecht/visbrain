"""Sleep GUI package exports."""

__all__ = ["Sleep", "SleepDataset"]


def __getattr__(name):
    if name == "Sleep":
        from .sleep import Sleep
        return Sleep
    if name == "SleepDataset":
        from .model import SleepDataset
        return SleepDataset
    raise AttributeError(f"module 'visbrain.gui.sleep' has no attribute {name!r}")
