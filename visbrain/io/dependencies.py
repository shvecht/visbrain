"""Test if dependencies are installed."""

from importlib import import_module
from typing import Optional

from packaging.version import InvalidVersion, Version

__all__ = (
    'is_mne_installed',
    'is_mne_bids_installed',
    'is_nibabel_installed',
    'is_opengl_installed',
    'is_pandas_installed',
    'is_lspopt_installed',
    'is_xlrd_installed',
    'is_tensorpac_installed',
    'is_sc_image_installed',
)


def _default_hint(
    package: str,
    min_version: Optional[str],
    upgrade: bool = True,
) -> str:
    constraint = f">={min_version}" if min_version else ""
    if constraint:
        command = f"pip install -U \"{package}{constraint}\""
    elif upgrade:
        command = f"pip install -U {package}"
    else:
        command = f"pip install {package}"
    return f"Install it with `{command}`."


def _check_dependency(
    module_name: str,
    *,
    package: Optional[str] = None,
    min_version: Optional[str] = None,
    raise_error: bool = False,
    install_hint: Optional[str] = None,
):
    package_name = package or module_name
    try:
        module = import_module(module_name)
    except Exception as exc:  # pragma: no cover - import failure path
        if raise_error:
            hint = install_hint or _default_hint(package_name, min_version)
            raise IOError(f"{package_name} is not installed. {hint}") from exc
        return False

    if min_version is not None:
        version = getattr(module, '__version__', None)
        if version is not None:
            try:
                if Version(version) < Version(min_version):
                    if raise_error:
                        hint = install_hint or _default_hint(package_name, min_version)
                        raise IOError(
                            f"{package_name} {version} is too old. {hint}"
                        )
                    return False
            except InvalidVersion:  # pragma: no cover - defensive
                pass
    return True


def is_mne_installed(raise_error=False):
    """Test if MNE is installed."""

    return _check_dependency(
        'mne',
        min_version='1.6.1',
        raise_error=raise_error,
        install_hint="Install it with `pip install -U \"mne>=1.6.1\"`.",
    )


def is_mne_bids_installed(raise_error=False):
    """Test if mne-bids is installed."""

    return _check_dependency(
        'mne_bids',
        min_version='0.12',
        raise_error=raise_error,
        install_hint="Install it with `pip install -U \"mne-bids>=0.12\"`.",
        package='mne-bids',
    )


def is_nibabel_installed(raise_error=False):
    """Test if nibabel is installed."""
    try:
        import nibabel  # noqa
        is_installed = True
    except:
        is_installed = False
    # Raise error (if needed) :
    if raise_error and not is_installed:
        raise IOError("nibabel not installed. See https://github.com/"
                      "nipy/nibabel for installation instructions.")
    return is_installed


def is_opengl_installed(raise_error=False):
    """Test if OpenGL is installed."""
    try:
        import OpenGL.GL as GL  # noqa
        is_installed = True
    except:
        is_installed = False
    # Raise error (if needed) :
    if raise_error and not is_installed:
        raise IOError("OpenGL not installed. See http://vispy.org/installation"
                      ".html#backend-requirements for installation "
                      "instructions.")
    return is_installed


def is_pandas_installed(raise_error=False):
    """Test if pandas is installed."""
    try:
        import pandas  # noqa
        is_installed = True
    except:
        is_installed = False
    # Raise error (if needed) :
    if raise_error and not is_installed:
        raise IOError("pandas not installed. See https://pandas.pydata.org/#"
                      "best-way-to-install for installation instructions.")
    return is_installed


def is_lspopt_installed(raise_error=False):
    """Test if lspopt is installed."""
    try:
        import lspopt  # noqa
        is_installed = True
    except:
        is_installed = False
    # Raise error (if needed) :
    if raise_error and not is_installed:
        raise IOError("lspopt not installed. See https://github.com/hbldh/"
                      "lspopt#installation for installation instructions.")
    return is_installed


def is_tensorpac_installed(raise_error=False):
    """Test if tensorpac is installed."""
    try:
        import tensorpac  # noqa
        is_installed = True
    except:
        is_installed = False
    # Raise error (if needed) :
    if raise_error and not is_installed:
        raise IOError("tensorpac not installed. See https://github.com/Etienne"
                      "Cmb/tensorpac#installation for installation "
                      "instructions.")
    return is_installed


def is_xlrd_installed(raise_error=False):
    """Test if xlrd is installed."""
    try:
        import xlrd  # noqa
        is_installed = True
    except:
        is_installed = False
    # Raise error (if needed) :
    if raise_error and not is_installed:
        raise IOError("xlrd not installed. In a terminal, run : pip install "
                      "xlrd")
    return is_installed


def is_sc_image_installed(raise_error=False):
    """Test if scikit-image is installed."""
    try:
        import skimage  # noqa
        is_installed = True
    except:
        is_installed = False
    # Raise error (if needed) :
    if raise_error and not is_installed:
        raise IOError("scikit-image not installed. In a terminal, run : pip"
                      " install scikit-image")
    return is_installed
