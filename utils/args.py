import argparse
import configparser


CONST_ARGUMENT_FILES = "files"
CONST_ARGUMENT_FORMAT = "format"
CONST_ARGUMENT_CONFIG = "config"

def parse_args() -> tuple[list, str, str]:
    parser = argparse.ArgumentParser()

    parser.add_argument(f"--{CONST_ARGUMENT_FILES}", type=str, nargs="*",
        help="files with serialized data",
    )
    parser.add_argument(f"--{CONST_ARGUMENT_FORMAT}", type=str,
        help="target format for serialization",
    )
    parser.add_argument(f"--{CONST_ARGUMENT_CONFIG}", type=str,
        help="config file for serialization",
    )

    known, _ = parser.parse_known_args()
    args = known.__dict__

    files = args.get(CONST_ARGUMENT_FILES)
    if files is None:
        files = []

    fmt = args.get(CONST_ARGUMENT_FORMAT)
    if fmt is None:
        fmt = ""

    config = args.get(CONST_ARGUMENT_CONFIG)
    if config is None:
        config = ""

    return files, fmt, config

def parse_config(path: str = "") -> tuple[list, str]:
    parser = configparser.ConfigParser()
    parser.read(path)

    args = parser.defaults()

    str_files = args.get(CONST_ARGUMENT_FILES)
    if str_files is None:
        str_files = ""

    files = str_files.split(" ")

    fmt = args.get(CONST_ARGUMENT_FORMAT)
    if fmt is None:
        fmt = ""

    return files, fmt

def get_app_args() -> tuple[list, str]:
    files, fmt, cfg = parse_args()

    if len(files) == 0 or fmt == "":
        _files, _fmt = parse_config(cfg)

        if len(files) == 0: files = _files
        if fmt == "": fmt = _fmt

    return files, fmt
