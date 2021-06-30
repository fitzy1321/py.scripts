import pyautogui
import time
import random

def click(sleep_time):
    time.sleep(sleep_time)
    pyautogui.click()

def main():
    while True:
        # get a time between 1 second and 3 minutes
        wait = random.randrange(1, 180)
        click(wait)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
