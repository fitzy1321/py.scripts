# factory.py
from typing import Dict, Any, Union, Callable

from src import DotnetProj, CppProj, PyProj, RustProj
from src.cli_obj import *


def project_factory(proj_type: str, name: str):
    _langs = {
        'python2': lambda _name: PyProj(_name),
        'python3': lambda _name: PyProj(_name, proj_type),
        'dotnet': lambda _name: DotnetProj(_name),
        'cpp': lambda _name: CppProj(_name),
        'rust': lambda _name: RustProj(_name),
    }
    if proj_type not in _langs:
        raise AssertionError("Project Type doesn't exist")
    else:
        return _langs[proj_type](name)
