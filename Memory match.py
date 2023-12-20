import pyautogui
import time
from PIL import Image, ImageDraw
import os


def find_unknowns(coef):
    if coef == 1:
        coef = 0.75
    elif coef == 2:
        coef = 0.68
    list_of_unknowns = None
    try:
        list_of_unknowns = list(
            pyautogui.locateAllOnScreen(r'png\important\clever.png', confidence=coef, grayscale=True))
        print('Обнаружен лвл с клеверами')
        list_of_unknowns = anti_repeat_filter(list_of_unknowns)
        return list_of_unknowns
    except Exception as e:
        print('Не могу найти клеверы\n', e)
    try:
        list_of_unknowns = list(
            pyautogui.locateAllOnScreen(r'png\important\heart.png', confidence=coef, grayscale=True))
        print('Обнаружен лвл с сердечками')
        list_of_unknowns = anti_repeat_filter(list_of_unknowns)
        return list_of_unknowns
    except Exception as e:
        print('Не могу найти сердечки\n', e)
    try:
        list_of_unknowns = list(
            pyautogui.locateAllOnScreen(r'png\important\smile.png', confidence=coef, grayscale=True))
        print('Обнаружен лвл с смайликами')
        list_of_unknowns = anti_repeat_filter(list_of_unknowns)
        return list_of_unknowns
    except Exception as e:
        print('Не могу найти смайлики\n', e)
    try:
        list_of_unknowns = list(
            pyautogui.locateAllOnScreen(r'png\important\jelly.png', confidence=coef, grayscale=True))
        print('Обнаружен лвл с желейками')
        list_of_unknowns = anti_repeat_filter(list_of_unknowns)
        return list_of_unknowns
    except Exception as e:
        print('Не могу найти желлейки\n', e)
    if list_of_unknowns == None:
        print('Ничего ваще не нашел.')


def anti_repeat_filter(list_of_unknowns):
    ramx = list_of_unknowns[0][0] - 114
    ramy = list_of_unknowns[0][1] - 114
    count = 0
    delete_list = []
    filter_scr = pyautogui.screenshot(r'png\fromfilter.png'
                                      , region=(500, 60, 920, 920))
    with Image.open(r'png\fromfilter.png') as im:
        draw = ImageDraw.Draw(im)
        for every in range(len(list_of_unknowns)):
            count += 1
            if list_of_unknowns[every][0] - ramx > 10 or list_of_unknowns[every][1] - ramy > 10:
                ramx = list_of_unknowns[every][0]
                ramy = list_of_unknowns[every][1]
            else:
                draw.rectangle((list_of_unknowns[every][0],
                                list_of_unknowns[every][1],
                                list_of_unknowns[every][0] + list_of_unknowns[every][2],
                                list_of_unknowns[every][1] + list_of_unknowns[every][3]), outline='blue')
                delete_list.append(every)
        im.save(r'png\fromfilter.png')
        # im.show()

    print('Через фильтр не прошло', len(delete_list), 'значений:', delete_list)

    delete_list.reverse()
    for index in delete_list:
        list_of_unknowns.pop(index)
    return list_of_unknowns


def screen_all(unknowns):
    for every in unknowns:
        pyautogui.click(every)
        time.sleep(0.4)
        position = pyautogui.position()
        name = f'{position[0]}, {position[1]}'
        scr = pyautogui.screenshot(fr'png\stash\{name}.png'
                                   , region=(int(position[0]) - 52, int(position[1]) - 52, 105, 105))
        try:
            pyautogui.locateOnScreen(rf'png\important\avoid.png', confidence=0.8)
            print('Найден миксер, удаляем.')
            os.remove(fr'png\stash\{name}.png')
        except:
            pass
        try:
            pyautogui.locateOnScreen(rf'png\important\avoid2.png', confidence=0.8)
            os.replace(fr'png\stash\{name}.png', fr'png\stash\last\{name}.png')
            print('Найден повар, сослан в другую папку.')
        except:
            pass
        try:
            pyautogui.locateOnScreen(rf'png\important\joker.png', confidence=0.8)
            os.replace(fr'png\stash\{name}.png', fr'png\stash\last\{name}.png')
            print('Найден жопкер, сослан в другую папку.')
        except:
            pass
        pyautogui.click(every)
    time.sleep(0.5)


def find_match():
    files = os.listdir(r'png\stash')
    files.pop()
    for item2 in files:
        for item in files:
            if item2 == item:
                continue
            try:
                pyautogui.locate(rf'png\stash\{str(item)}', rf'png\stash\{str(item2)}', confidence=0.8)
                coords = str(item)[:-4].split(', ')
                pyautogui.click(int(coords[0]), int(coords[1]), duration=0.33)
                coords2 = str(item2)[:-4].split(', ')
                pyautogui.click(int(coords2[0]), int(coords2[1]), duration=0.33)
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
                pyautogui.locate(rf'png\stash\last\{str(item)}', rf'png\stash\last\{str(item2)}', confidence=0.75)
                coords = str(item)[:-4].split(', ')
                pyautogui.click(int(coords[0]), int(coords[1]), duration=0.5)
                coords2 = str(item2)[:-4].split(', ')
                pyautogui.click(int(coords2[0]), int(coords2[1]), duration=0.5)
                os.remove(rf'png\stash\last\{str(item)}')
                os.remove(rf'png\stash\last\{str(item2)}')
            except:
                continue

    time.sleep(3)
    unknowns = find_unknowns(1)
    if len(unknowns) > 5:
        mix_all()
        do_it(2)

    else:
        for mixer in unknowns:
            pyautogui.click(mixer)
        time.sleep(4)
        unknowns = find_unknowns(1)
        for mixer in unknowns:
            pyautogui.click(mixer)
    time.sleep(12)
    do_it(1)


def mix_all():
    print('тыкаем и на миксеры тоже')
    clear_stash()
    unknowns = find_unknowns(2)
    for every in unknowns:
        pyautogui.click(every)
        time.sleep(0.4)
        position = pyautogui.position()
        name = f'{position[0]}, {position[1]}'
        scr = pyautogui.screenshot(fr'png\stash\{name}.png',
                                   region=(int(position[0]) - 52, int(position[1]) - 52, 105, 105))
        pyautogui.click(every)
    try:
        find_match()
    except:
        time.sleep(12)
    do_it(1)


def do_it(coef):
    clear_stash()
    try:
        pyautogui.locateOnScreen(rf'png\important\win.png', confidence=0.8)
        print('ПАБЕДА')
        exit()
    except:
        pass
    unknowns = find_unknowns(coef)
    screen_all(unknowns)
    find_match()


def clear_stash():
    try:
        files = os.listdir(r'png\stash\last')
        for item in range(len(files)):
            os.remove(fr'png\stash\last\{files[item]}')
        files = os.listdir(r'png\stash')
        for item in range(len(files)):
            os.remove(fr'png\stash\{files[item]}')
        os.remove(r'png\fromfilter.png')
        print('папка stash была очищена')
    except FileNotFoundError:
        print()
    except Exception as e:
        print(e)


do_it(1)
