import pyautogui
import keyboard

stopping = False

def pressed():
    global stopping
    stopping = True

keyboard.add_hotkey("delete", lambda: pressed())

while not stopping:
    pyautogui.click(630, 930, duration=0)
    pyautogui.click(1200, 840, duration=0)

