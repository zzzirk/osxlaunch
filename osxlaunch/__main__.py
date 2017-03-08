"""
Generate a macOS property list file for environment variables.
"""

import argparse
import os
import plistlib


def genplist(envvars):
    "Generate the launchctl program argument plist."
    launchctl = [
        "/bin/launchctl",
        "setenv",
    ]

    for ev in envvars:
        if ev.upper() in os.environ:
            launchctl.append(ev.upper())
            launchctl.append(os.environ[ev.upper()])

    return dict(Label="setenv.startup", ProgramArgument=launchctl,
                RunAtLoad=True, ServiceIPC=False)


def parse_args():
    "Parse command line arguments."
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", default=None)
    parser.add_argument("envvar", nargs="+")
    return parser.parse_args()


def main():
    "Main application logic."
    args = parse_args()

    plist = genplist(args.envvar)
    if args.filename is not None:
        plistlib.writePlist(plist, args.filename)
    print(plistlib.writePlistToString(plist))


if __name__ == '__main__':
    main()
