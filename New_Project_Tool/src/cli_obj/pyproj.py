# py_proj.py

from src.cli_obj._base import CliBase


class PyProj(CliBase):
    def __init__(self, name, version=''):
        CliBase.__init__(self, _path=name)
        self._version = version

    def create(self, *args):
        self._make_virtual_env()

        CliBase.create_std_files(self)

    def _make_virtual_env(self):
        CliBase.call_cli(self, f"python{'3.7' if self._version == '' else self._version} -m venv venv")


# TODO: figure out this mess
# Error: Command '['/repo/python/New_Project_Tool/Cool/venv/bin/python', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1.
# Command 'python -m venv venv' returned non-zero exit status 1.
