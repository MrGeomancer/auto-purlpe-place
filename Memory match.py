import pyautogui
from PIL import Image, ImageDraw
import time
import os

try:
    files = os.listdir(r'png\stash')
    for item in range(len(files)):
        os.remove(fr'png\stash\{files[item]}')
    files = os.listdir(r'png\stash\last')
    for item in range(len(files)):
        os.remove(fr'png\stash\{files[item]}')
    # os.makedirs(r'png\stash')
    os.makedirs(r'png\stash\last')
except FileNotFoundError:
    print()
except Exception as e:
    print(e)


def matrix_coord(stolbik, ryad):
    a = matrix[8 * (ryad - 1) + (stolbik - 1)].get('x')
    b = matrix[8 * (ryad - 1) + (stolbik - 1)].get('y')
    return a, b

def anti_repeat_filter(list_of_unknowns):
    ramx = list_of_unknowns[0][0]-114
    ramy = list_of_unknowns[0][1]-114
    count = 0
    delete_list = []
    for every in range(len(list_of_unknowns)):
        count += 1
        if list_of_unknowns[every][0] - ramx > 100 or list_of_unknowns[every][1] - ramy > 100:
            ramx = list_of_unknowns[every][0]
            ramy = list_of_unknowns[every][1]
        else:
            delete_list.append(every)

    delete_list.reverse()
    for index in delete_list:
        list_of_unknowns.pop(index)
    return list_of_unknowns


def find_unknowns():
    try:
        clevers = list(pyautogui.locateAllOnScreen(r'png\important\clever.png', confidence=0.86))
    except:
        pass
    clevers=anti_repeat_filter(clevers)
    return clevers



def screen_All(unknowns):
    for every in unknowns:
        pyautogui.click(every)
        time.sleep(0.4)
        position = pyautogui.position()
        name = f'{position[0]}, {position[1]}'

        scr = pyautogui.screenshot(fr'png\stash\{name}.png', region=(int(position[0])-53, int(position[1])-53,
                                                                     107, 107))
        try:
            pyautogui.locateOnScreen(rf'png\important\avoid.png', confidence=0.8)
            os.remove(fr'png\stash\{name}.png')
        except:
            pass
        try:
            pyautogui.locateOnScreen(rf'png\important\avoid2.png', confidence=0.8)
            os.replace(fr'png\stash\{name}.png',fr'png\stash\last\{name}.png')
        except:
            pass
        try:
            pyautogui.locateOnScreen(rf'png\important\joker.png', confidence=0.8)
            os.replace(fr'png\stash\{name}.png',fr'png\stash\last\{name}.png')
        except:
            pass
        pyautogui.click(every)



def find_match():
    files = os.listdir(r'png\stash')
    files.pop()
    for item2 in files:
        for item in files:
            if item2 == item:
                continue
            try:
                pyautogui.locate(rf'png\stash\{str(item)}',rf'png\stash\{str(item2)}',confidence=0.8)
                coords = str(item)[:-4].split(', ')
                pyautogui.click(int(coords[0]), int(coords[1]),duration=0.33)
                coords2 = str(item2)[:-4].split(', ')
                pyautogui.click(int(coords2[0]), int(coords2[1]),duration=0.33)
                os.remove(rf'png\stash\{str(item)}')
                os.remove(rf'png\stash\{str(item2)}')
            except:
                continue
    files = os.listdir(r'png\stash\last')
    for item2 in files:
        for item in files:
            if item2 == item:
                continue
            try:
                pyautogui.locate(rf'png\stash\last\{str(item)}', rf'png\stash\last\{str(item2)}', confidence=0.8)
                coords = str(item)[:-4].split(', ')
                pyautogui.click(int(coords[0]), int(coords[1]), duration=0.33)
                coords2 = str(item2)[:-4].split(', ')
                pyautogui.click(int(coords2[0]), int(coords2[1]), duration=0.33)
                os.remove(rf'png\stash\last\{str(item)}')
                os.remove(rf'png\stash\last\{str(item2)}')
            except:
                continue
    time.sleep(3)
    unknowns = find_unknowns()
    for mixer in unknowns:
        pyautogui.click(mixer)
    time.sleep(4)
    for mixer in unknowns:
        pyautogui.click(mixer)


    # for i in range(0,8):
    #     for ii in range(0,8):
    #         pyautogui.click(matrix_coord(i,ii),duration=0.3)


# matrix = []
#
# for i in range(8): #8
#     for ii in range(8):
#         matrix.append({'x': 558 + 114 * ii, 'y': 120 + 114 * i})
unknowns = find_unknowns()
screen_All(unknowns)
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
