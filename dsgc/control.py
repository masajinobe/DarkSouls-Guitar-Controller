import pyautogui
import pydirectinput
# import time


def key_control(n0):
    if n0 == 64:
        pydirectinput.keyUp('s')
        pydirectinput.keyDown('w')
        print('E4 - W hold')

    if n0 == 68:
        pydirectinput.keyUp('w')
        pydirectinput.keyDown('s')
        print('G#4 - S hold')

    if n0 == 65:
        pydirectinput.press('o')  # Target
        print('F4 - O pressed')

    if n0 == 74:
        pydirectinput.press('e')  # Action
        print('D5 - E pressed')

    if n0 == 73:
        pydirectinput.keyUp('w')  # Stop
        pydirectinput.keyUp('s')
        print('C#5 - Stop')

    if n0 == 72:
        pydirectinput.press('q')  # Use Item
        print('C5 - Q pressed')

    if n0 == 67:
        pydirectinput.move(-20, 0)
        print('G4 - Look Left')

    if n0 == 69:
        pydirectinput.move(20, 0)
        print('A4 - Look Right')
