"""Download helper utilities for Visbrain optional datasets."""

from __future__ import annotations

import argparse
import logging
import os
import sys
from pathlib import Path
from urllib import request
import zipfile
from warnings import warn

from .rw_config import load_config_json
from .path import get_data_url_path, path_to_visbrain_data


logger = logging.getLogger('visbrain')


__all__ = ["download_file", "available_downloads", "main"]


def available_downloads() -> dict[str, dict[str, str]]:
    """Return the mapping of downloadable datasets."""

    return load_config_json(get_data_url_path())


def get_data_url(name, astype):
    """Get filename and url to a file.

    Parameters
    ----------
    name : string
        Name of the file.
    astype : string
        Type of the file to download.

    Returns
    -------
    url : string
        Url to the file to download.
    """
    # Get path to data_url.txt :
    urls = available_downloads()[astype]
    # Try to get the file :
    try:
        url_to_download = urls[name]
        if not bool(url_to_download.find('dl=1') + 1):
            warn("The dropbox url should contains 'dl=1'.")
        return urls[name]
    except:
        raise IOError(name + " not in the default path list of files.")


def reporthook(blocknum, blocksize, totalsize):
    """Report downloading status."""
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = min(100, readsofar * 1e2 / totalsize)
        s = "\rSTATUS : %5.1f%% %*d / %d" % (
            percent, len(str(totalsize)), readsofar, totalsize)
        sys.stderr.write(s)
        if readsofar >= totalsize:  # near the end
            sys.stderr.write("\n")
    else:  # total size is unknown
        sys.stderr.write("\rread %d" % (readsofar,))


def download_file(name, astype=None, filename=None, to_path=None, unzip=False,
                  remove_archive=False, use_pwd=False):
    """Download a file into the Visbrain data cache.

    Parameters
    ----------
    name : string
        Name of the file to download or url.
    astype : str | None
        If name is a name of a file that can be downloaded, astype refer to the
        type of the file.
    filename : string | None
        Name of the file to be saved in case of url.
    to_path : string | None
        Download file to the path specified.
    unzip : bool | False
        Unzip archive if needed.
    remove_archive : bool | False
        Remove archive after unzip.
    use_pwd : bool | False
        Download the file to the current directory.

    Returns
    -------
    path_to_file : string
        Path to the downloaded file.
    """
    # Default visbrain-path to data (platform specific cache):
    if use_pwd:
        vb_path = Path.cwd()
    elif to_path is not None:
        vb_path = Path(to_path)
    else:
        vb_path = Path(path_to_visbrain_data(folder=astype, create=True,
                                             allow_bundled=False))
        vb_path = vb_path if vb_path.suffix else Path(vb_path)
        to_path = str(vb_path)
    if bool(name.find('http') + 1):
        if filename is None:
            filename = os.path.split(name)[1]
        assert isinstance(filename, str)
        url = name
    else:
        assert isinstance(name, str) and isinstance(astype, str)
        filename, url = name, get_data_url(name, astype)
        if to_path is None:
            to_path = Path(path_to_visbrain_data(folder=astype, create=True,
                                                 allow_bundled=False))
        else:
            to_path = Path(to_path)
    to_path = Path(to_path)
    to_path.mkdir(parents=True, exist_ok=True)
    path_to_file = to_path / filename
    to_download = not path_to_file.is_file()

    # Dowload file if needed :
    if to_download:
        logger.info('Downloading %s' % path_to_file)
        # Check if directory exists else creates it
        if not to_path.exists():
            logger.info('Folder %s created' % to_path)
            to_path.mkdir(parents=True, exist_ok=True)
        # Download file :
        fh, _ = request.urlretrieve(url, str(path_to_file), reporthook=reporthook)
        # Unzip file :
        if unzip:
            # Unzip archive :
            zip_file_object = zipfile.ZipFile(fh, 'r')
            zip_file_object.extractall(path=str(to_path))
            zip_file_object.close()
            logger.info('Unzip archive')
            if remove_archive:  # Remove archive :
                logger.info('Archive %s removed' % path_to_file)
                path_to_file.unlink()
    else:
        logger.info("File already dowloaded (%s)." % path_to_file)
    return str(path_to_file)


def _infer_type(names: list[str], config: dict[str, dict[str, str]]) -> str:
    """Infer the dataset type from its name(s)."""

    matches = {name: [] for name in names}
    for dtype, entries in config.items():
        for name in names:
            if name in entries:
                matches[name].append(dtype)
    inferred: set[str] = set()
    for name, types in matches.items():
        if not types:
            raise ValueError(f"Dataset '{name}' is not defined in data_url.json")
        if len(types) > 1:
            raise ValueError(
                f"Dataset '{name}' appears in multiple categories: {types}. "
                "Specify --type explicitly."
            )
        inferred.update(types)
    if len(inferred) > 1:
        raise ValueError(
            "Mixed dataset categories detected. Pass --type to disambiguate."
        )
    return inferred.pop()


def _should_unzip(filename: str, explicit: bool | None) -> bool:
    """Determine whether archives should be extracted."""

    if explicit is not None:
        return explicit
    return filename.lower().endswith('.zip')


def main(argv: list[str] | None = None) -> int:
    """Run the command line interface for dataset downloads."""

    parser = argparse.ArgumentParser(
        description=(
            "Download optional Visbrain datasets into the writable cache. "
            "Run without arguments to list available resources."
        )
    )
    parser.add_argument(
        "name",
        nargs="*",
        help="Name(s) of the dataset to download. Use --list to inspect options.",
    )
    parser.add_argument(
        "--type",
        "-t",
        dest="dtype",
        help="Dataset category (e.g. templates, roi, topo, example_data).",
    )
    parser.add_argument(
        "--dest",
        dest="dest",
        help="Destination directory. Defaults to the Visbrain data cache.",
    )
    parser.add_argument(
        "--use-pwd",
        dest="use_pwd",
        action="store_true",
        help="Download into the current working directory.",
    )
    parser.add_argument(
        "--list",
        dest="list_only",
        action="store_true",
        help="List available datasets and exit.",
    )
    parser.add_argument(
        "--unzip",
        dest="unzip",
        action="store_true",
        help="Force extraction of downloaded ZIP archives.",
    )
    parser.add_argument(
        "--keep-archive",
        dest="keep_archive",
        action="store_true",
        help="Retain ZIP archives when --unzip is used (default removes them).",
    )
    parser.add_argument(
        "--no-unzip",
        dest="no_unzip",
        action="store_true",
        help="Prevent automatic extraction even for known archives.",
    )

    args = parser.parse_args(argv)
    config = available_downloads()

    if args.list_only or not args.name:
        for dtype, entries in sorted(config.items()):
            print(f"[{dtype}]")
            for key in sorted(entries):
                print(f"  - {key}")
            print()
        return 0

    names = list(dict.fromkeys(args.name))
    dtype = args.dtype
    if dtype is None:
        try:
            dtype = _infer_type(names, config)
        except ValueError as exc:
            parser.error(str(exc))

    unzip_flag: bool | None
    if args.unzip and args.no_unzip:
        parser.error("--unzip and --no-unzip are mutually exclusive")
    if args.unzip:
        unzip_flag = True
    elif args.no_unzip:
        unzip_flag = False
    else:
        unzip_flag = None

    for name in names:
        unzip = _should_unzip(name, unzip_flag)
        download_file(
            name,
            astype=dtype,
            to_path=args.dest,
            unzip=unzip,
            remove_archive=not args.keep_archive if unzip else False,
            use_pwd=args.use_pwd,
        )
    return 0


if __name__ == "__main__":  # pragma: no cover - manual invocation
    sys.exit(main())
