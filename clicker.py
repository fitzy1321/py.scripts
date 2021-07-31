#!/usr/bin/env python3

"""Auto Mouse Clicker Script. Make it look like your still online with Python Automation."""

import pyautogui
from time import sleep
from random import randint
import typer


# Disable FailSafeException when mouse is in screen corners.
# I don't need a failsafe for this script.
pyautogui.FAILSAFE = False

# Flag to print debug statements to console.
_PRINT_DEBUG = False

# Flag to bypass random thread sleep, a.k.a. more debugging stuff.
_FAST_CLICK = False


def auto_click(sleep_time: int = None) -> None:
    """Click function will pause current thread for a random intervaul, then click the mouse."""
    if not sleep_time:
        # get a time between 1 second and 3 minutes
        # to make clicks look a little more 'natural'
        sleep_time = randint(1, 180) if not _FAST_CLICK else 1

    if _PRINT_DEBUG and not _FAST_CLICK:
        print(f"Random thread sleep for: {sleep_time} seconds.")
    elif _PRINT_DEBUG and _FAST_CLICK:
        print("Thread sleep for 1 second.")

    # pause the current thread
    sleep(sleep_time)

    # it's that easy to click a mouse with python :)
    pyautogui.click()

    if _PRINT_DEBUG:
        print("Clicked")


def main(
    debug: bool = typer.Option(..., "--debug", "-d"),
    fast_click: bool = typer.Option(..., "--fast-click", "-f"),
) -> None:
    """Auto Mouse Clicker Script. Make it look like your still online with Python Automation."

    Args:
        debug (bool, optional): Print debug statements.
        fast_click (bool, optional): One second clicks. Useful for debugging.
    """
    print("Clicking away...")

    _PRINT_DEBUG = debug
    _FAST_CLICK = fast_click
    while True:
        try:
            auto_click()
        except KeyboardInterrupt:
            msg = (
                "KeyboardInterrupt thrown and caught. Exiting script"
                if _PRINT_DEBUG
                else "Back to work!"
            )
            print(msg)
            break


if __name__ == "__main__":
    typer.run(main)
