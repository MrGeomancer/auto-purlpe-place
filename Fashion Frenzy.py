import pyautogui
import keyboard

stopping = False

def pressed():
    global stopping
    stopping = True

keyboard.add_hotkey("delete", lambda: pressed())

while not stopping:
    pyautogui.click(1200, 160)
    pyautogui.click(1200, 320)
    pyautogui.click(1200, 420)
    pyautogui.click(1200, 560)
    pyautogui.click(1200, 660)
    pyautogui.click(900, 660)
    pyautogui.click(92, 153)
    pyautogui.click(1341, 416)



