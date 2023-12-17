import pyautogui
import keyboard
from PIL import Image, ImageDraw
import os

for clever in pyautogui.locateAllOnScreen(r'png\important\clever.png', confidence=0.85):
    print(pyautogui.click(clever))

# def find_match():
#     files = os.listdir(r'png\stash')
#     for item in files:
#         print(item)
#
#
# # find_match()
# files = os.listdir(r'png\stash')
# print(files)
# files.pop()
# print(files)
# print(type(files))

# stopping = False
# for i in количество файлов в папке:
#     локейт он скрин "Клевер"(картинка i,confidence=0.85)
#
#
# for pos in pyautogui.locateAllOnScreen('idial.png',confidence=0.85):
#     print(pos)

# clever=pyautogui.locateAllOnScreen('idial.png',confidence=0.8)
# print(clever)
# print(pyautogui.center(clever[0]))

# while True:
#     keyboard.wait('www')
#     print(pyautogui.position())


    # pyautogui.click(780,780)


