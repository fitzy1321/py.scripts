"""Change current working directory to repo root folder."""

import os
import subprocess


def chdir_to_git_root():
    """Read above. Might close if stderr has a value."""
    og_dir = path = os.getcwd()
    y = subprocess.Popen(
        ["git", "rev-parse", "--show-toplevel"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    stdout, stderr = y.communicate()
    if stderr:
        print(stderr)
        raise SystemExit(1)

    git_parent = bytes(stdout).strip()
    os.chdir(git_parent)
    print(os.getcwd())

    if git_parent != og_dir:
        print(f"Changed current working directory to: {path}")
