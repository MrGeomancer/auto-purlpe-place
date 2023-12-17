import pyautogui
from PIL import Image, ImageDraw
import time
import os

try:
    files = os.listdir(r'png\stash')
    for item in range(len(files)):
        os.remove(fr'png\stash\{files[item]}')
    # os.makedirs(r'png\stash')
    os.makedirs(r'png\stash\povar')
except FileNotFoundError:
    print()
except Exception as e:
    print(e)


def matrix_coord(stolbik, ryad):
    a = matrix[8 * (ryad - 1) + (stolbik - 1)].get('x')
    b = matrix[8 * (ryad - 1) + (stolbik - 1)].get('y')
    return a, b

def screen_All():
    for i in matrix:
        pyautogui.click(i['x'],i['y'])
        time.sleep(0.4)
        position = pyautogui.position()
        name = f'{position[0]}, {position[1]}'

        scr = pyautogui.screenshot(fr'png\stash\{name}.png', region=(int(position[0])-25, int(position[1])-25,
                                                                     51, 51))
        try:
            pyautogui.locateOnScreen(rf'png\important\avoid.png', confidence=0.8)
            os.remove(fr'png\stash\{name}.png')
        except:
            pass
        try:
            pyautogui.locateOnScreen(rf'png\important\avoid2.png', confidence=0.8)
            os.replace(fr'png\stash\{name}.png',fr'png\stash\povar\{name}.png')
        except:
            pass

        pyautogui.click(i.get('x'), i.get('y'))


def find_match():
    files = os.listdir(r'png\stash')
    files.pop()
    for item2 in files:
        for item in files:
            if item2 == item:
                continue
            try:
                pyautogui.locate(rf'png\stash\{str(item)}',rf'png\stash\{str(item2)}',confidence=0.7)
                coords = str(item)[:-4].split(', ')
                pyautogui.click(int(coords[0]), int(coords[1]),duration=0.5)
                coords2 = str(item2)[:-4].split(', ')
                pyautogui.click(int(coords2[0]), int(coords2[1]),duration=0.5)
                os.remove(rf'png\stash\{str(item)}')
                os.remove(rf'png\stash\{str(item2)}')
                files.remove(str(item))
                files.remove(str(item2))
            except:
                continue
    files = os.listdir(r'png\stash\povar')
    for item2 in files:
        for item in files:
            if item2 == item:
                continue
            try:
                pyautogui.locate(rf'png\stash\povar\{str(item)}', rf'png\stash\povar\{str(item2)}', confidence=0.8)
                coords = str(item)[:-4].split(', ')
                pyautogui.click(int(coords[0]), int(coords[1]), duration=0.5)
                coords2 = str(item2)[:-4].split(', ')
                pyautogui.click(int(coords2[0]), int(coords2[1]), duration=0.5)
                os.remove(rf'png\stash\povar\{str(item)}')
                os.remove(rf'png\stash\povar\{str(item2)}')
            except:
                continue
    time.sleep(3)
    try:
        for mixer in pyautogui.locateAllOnScreen(r'png\important\clever.png', confidence=0.85):
            pyautogui.click(mixer)
        time.sleep(4)
        for mixer in pyautogui.locateAllOnScreen(r'png\important\clever.png', confidence=0.85):
            pyautogui.click(mixer)
    except:
        pass
    try:
        for mixer in pyautogui.locateAllOnScreen(r'png\important\heart.png', confidence=0.85):
            pyautogui.click(mixer)
        time.sleep(4)
        for mixer in pyautogui.locateAllOnScreen(r'png\important\heart.png', confidence=0.85):
            pyautogui.click(mixer)
    except:
        pass



    # for i in range(0,8):
    #     for ii in range(0,8):
    #         pyautogui.click(matrix_coord(i,ii),duration=0.3)


matrix = []

for i in range(8): #8
    for ii in range(8):
        matrix.append({'x': 558 + 114 * ii, 'y': 120 + 114 * i})

screen_All()
find_match()
# print(len(matrix))
# print(matrix[0].get('x'))
# print(matrix[0].get('y'))
# print(matrix[4].get('x'))
# stolbik, ryad = map(int,input().split())
# print(matrix[8*(ryad-1)+(stolbik-1)])

# print(matrix_clic(1,1))
# print((matrix_clic(1,1)[0]-53,matrix_clic(1,1)[1]-53,matrix_clic(1,1)[0]+60,matrix_clic(1,1)[1]+60))

# clever = (pyautogui.locateOnScreen(r'png\clever\idial.png',confidence=0.85))
# pyautogui.click(pyautogui.center(clever))
# time.sleep(0.4)
# print(clever)
# print(clever[0],clever[1],clever[2],clever[3])
# name = f'{pyautogui.center(clever)[0]}, {pyautogui.center(clever)[1]}'
# scr = pyautogui.screenshot(fr'png\stash\{name}.png', region=(int(clever[0])-1, int(clever[1])-1,
#                                                              int(clever[2])+2, int(clever[3])+2))
#
# clever = (pyautogui.locateOnScreen(r'png\clever\idial.png',confidence=0.85))
# pyautogui.click(pyautogui.center(clever))
# time.sleep(0.4)
# print(clever)
# print(clever[0],clever[1],clever[2],clever[3])
# name = f'{pyautogui.center(clever)[0]}, {pyautogui.center(clever)[1]}'
# scr = pyautogui.screenshot(fr'png\stash\{name}.png', region=(int(clever[0])-1, int(clever[1])-1,
#                                                              int(clever[2])+2, int(clever[3])+2))
# match = (pyautogui.locateOnScreen(fr'png\stash\{name}.png',confidence=0.85, region=(int(clever[0])-1, int(clever[1])-1,
#                                                              int(clever[2])+2, int(clever[3])+2)))






# with Image.open(fr'png\stash\{name}.png') as im:
#     im.show()

# 558 120
# 672 234
# 786 348


# for i in len(matrix):
#     # pyautogui.click(matrix[i].get('x'),matrix[i].get('x'))
#     pyautogui.click(matrix_clic(1,2)


# 670 780
# 120 230 340
