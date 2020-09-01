from pywinauto.keyboard import send_keys
from colorama import init, Fore, Back
import pywinauto
import keyboard

init()  # Colorama


def control_move(note):
    if note == 64:
        send_keys('{s up}')
        send_keys('{w down}')
        print(Fore.BLACK + Back.YELLOW + 'E4 - W')

    if note == 68:
        send_keys('{w up}')
        send_keys('{s down}')
        print(Fore.BLACK + Back.CYAN + 'G#4 - S')

    if note == 65:
        send_keys('{w up}')
        send_keys('{s up}')
        keyboard.press_and_release('o')  # Target
        print(Fore.BLACK + Back.GREEN + 'F4 - O pressed')

    if note == 74:
        send_keys('{w up}')
        send_keys('{s up}')
        keyboard.press_and_release('e')  # Action
        print(Fore.BLACK + Back.MAGENTA + 'D5 - E pressed')

    if note == 72:
        send_keys('{w up}')
        send_keys('{s up}')
        keyboard.press_and_release('q')  # Use Item
        print(Fore.BLACK + Back.RED + 'C5 - Q pressed')

    if note == 67:
        pywinauto.mouse.move(coords=(-10, 0))
        print(Fore.BLACK + Back.WHITE + 'G4 - Look Left')

    if note == 63:
        pywinauto.mouse.click(button='left')
        print(Fore.BLACK + Back.WHITE + 'D#4 - Click!')

    if note == 69:
        pywinauto.mouse.move(coords=(10, 0))
        print(Fore.BLACK + Back.WHITE + 'A4 - Look Right')
