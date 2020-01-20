# args.py
import argparse
import os

def get():
    _parser = argparse.ArgumentParser(
        prog="Creator.py",
        description="A Python Automation Tool to create new src project \
                    structures.",
        usage="./creator.sh [project_name] [project_type] [-a]|[--add-creds]",
    )

    _parser.add_argument(
        "-a", "--add-creds", help="Add GitHub Credentials", action="store_true"
    )

    _parser.add_argument("name", metavar="name", type=str, help="name of your project")
    _parser.add_argument(
        "ProjType", metavar="proj_type", help="type of project to create", nargs="?"
    )

    _parser.add_argument('path', nargs='?', default=os.getcwd())

    _parser.add_argument("Additional", nargs="*", default=[])

    return _parser.parse_args()

