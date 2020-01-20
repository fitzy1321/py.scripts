# main.py

# from src.git_creds import Creds
import src.args as cli_args
from src.factory import project_factory
import os


def change_working_dir(path: str):
    _path = os.getcwd() + path if not os.path.isabs(path) else path

    try:
        os.makedirs(_path)
    except FileExistsError:
        pass

    os.chdir(_path)


def run():
    # Step 1: GitHub Credentials
    # TODO : look into configpaser

    _args = cli_args.get()
    if not _args.ProjType:
        print("You did not specify a language, defaulting to python")
        _args.ProjType = "python"

    _folder = f'{_args.path}/{_args.name}'
    print(_folder)
    change_working_dir(_folder)

    try:
        _projectTool = project_factory(_args.ProjType, _args.name)
        _projectTool.create(_args.Additional)
    except AssertionError:
        pass
