#!/usr/bin/env python3

"""Auto Mouse Clicker Script. Make it look like your still online with Python Automation."""

import pyautogui
from time import sleep
from random import randint
import sys

# Disable FailSafeException when mouse is in screen corners.
# I don't need a failsafe for this script.
pyautogui.FAILSAFE = False

# Flag to print debug statements to console.
__PRINT_DEBUG = False

# Flag to bypass random thread sleep, a.k.a. more debugging stuff.
__FAST_CLICK = False


def auto_click(sleep_time: int = None) -> None:
    """Click function will pause current thread for a random intervaul, then click the mouse."""
    if not sleep_time:
        # get a time between 1 second and 3 minutes
        # to make clicks look a little more 'natural'
        sleep_time = randint(1, 180) if not __FAST_CLICK else 1

    if __PRINT_DEBUG and not __FAST_CLICK:
        print(f"Random thread sleep for: {sleep_time} seconds.")
    elif __PRINT_DEBUG and __FAST_CLICK:
        print("Thread sleep for 1 second.")

    # pause the current thread
    sleep(sleep_time)

    # it's that easy to click a mouse with python :)
    pyautogui.click()

    if __PRINT_DEBUG:
        print("Clicked")


def main() -> None:
    """Primary loop for auto clicker script."""
    print("Clicking away...")

    while True:
        try:
            auto_click()
        except KeyboardInterrupt:
            msg = "KeyboardInterrupt thrown and caught. Exiting script" if __PRINT_DEBUG else "Back to work!"
            print(msg)
            break


if __name__ == "__main__":
    args = None
    try:
        args = sys.argv[1:]
        d_flags = ["--debug", "-d"]
        fc_flags = ["--fast-click", "-f", "-fc"]

        # check for debug flag, with generator expression
        __PRINT_DEBUG = any((df in args) for df in d_flags)
        # check for fast click flag, with generator expression
        __FAST_CLICK = any((ff in args) for ff in fc_flags)

    except IndexError:
        pass

    if __PRINT_DEBUG:
        print(f"Cli arguments passed in: {args}")

    main()
