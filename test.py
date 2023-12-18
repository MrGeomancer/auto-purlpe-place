import pyautogui
import keyboard
from PIL import Image, ImageDraw
import os

try:
    clevers = list(pyautogui.locateAllOnScreen(r'png\important\smile.png', confidence=0.86))
except:
    pass
print(clevers[0][0])
scr = pyautogui.screenshot(fr'png\stash\smile.png', region=(int(pyautogui.center(clevers[0][0]))-53, int(pyautogui.center(clevers[0][0]))-53,
                                                                     107, 107))



# print(clevers[1])
# print(type(clevers[1]))
# print(clevers[0][1])
# print(type(clevers[0][0]))
# print(int(clevers[0][0]))
# print(clevers[46])

# ramx = 392
# ramy = -46
# count = 0
# delete_list = []
# for every in range(len(clevers)):
#     count += 1
#     # print(clevers)
#     if clevers[every][0] - ramx > 100 or clevers[every][1] - ramy > 100:
#         ramx = clevers[every][0]
#         ramy = clevers[every][1]
#     else:
#         delete_list.append(every)
#
# delete_list.reverse()
#
# # for i in clevers:
# #
# #     print(clevers.index(i), i)
# for index in delete_list:
#     clevers.pop(index)
#
# for i in clevers:
#
#     print(clevers.index(i), i)
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


