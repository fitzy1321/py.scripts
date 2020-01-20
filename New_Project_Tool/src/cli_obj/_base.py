# base.py
import abc
import os
import subprocess


class CliBase(metaclass=abc.ABCMeta):
    def __init__(self, _path: str):
        self._path = _path

    @abc.abstractmethod
    def create(self, *args):
        pass

    @staticmethod
    def call_cli(command: str):
        try:
            subprocess.run(command, shell=True, check=True)
        except Exception as e:
            print(type(e))
            print(e)
            exit()

    def create_std_files(self):
        self.call_cli('echo empty > .gitignore && echo empty > README.md')

    @staticmethod
    def _get_file_prefix():
        return "/" if os.name != "nt" else "\\"

    def initialize_git_repo(self):
        pass

    # TODO: maybe implement method for licence
