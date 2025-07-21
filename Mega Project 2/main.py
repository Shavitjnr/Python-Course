import pyautogui
import random
import time

# Get the screen size from pyautogui
screen_width, screen_height = pyautogui.size()

while True:
    # Move to a random position
    x = random.randint(0, screen_width - 1)
    y = random.randint(0, screen_height - 1)
    pyautogui.moveTo(x, y)
    a = pyautogui.position()
    print(a)
    time.sleep(1)
