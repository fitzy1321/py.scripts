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
    print("Taking a break...")

    while True:
        try:
            auto_click()
        # except pyautogui.FailSafeException:
        #     # This Exception gets thrown when mouse is in one of the corners of the screen
        #     # Used to escape mouse spawms, but I don't need it for this script
        #     if PRINT_DEBUG:
        #         print("pyautogui.FailSafeException was thrown, but it was ignored")
        except KeyboardInterrupt:
            if __PRINT_DEBUG:
                print("KeyboardInterrupt thrown and caught. Exiting script")
            else:
                print("Back to work!")
            break


if __name__ == "__main__":
    args = None
    try:
        args = sys.argv[1:]
        # check for debug flag
        __PRINT_DEBUG = "--debug" in args or "-d" in args
        # check for fast click flag
        __FAST_CLICK = "--fast-click" in args or "-fc" in args

    except IndexError:
        pass

    if __PRINT_DEBUG:
        print(f"Cli arguments passed in: {args}")

    main()
