import sys
import time
import pygetwindow as gw
import pyautogui
import pytesseract as tess

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

window = gw.getWindowsWithTitle('BlueStacks')[0]
window.activate()
window.moveTo(0, 0)

# Window Defaults
win_off = 42
win_x = window.left + 1
win_y = window.top + win_off + 1
win_w = 540 + win_off
win_h = 800 + win_off

time.sleep(0.5)


# Functions?

def check(x, y, w, h, t, c):
    px = win_x + x
    py = win_y + y

    while True:
        print("Trying: " + t)
        shot = pyautogui.screenshot(region=(px, py, w, h))
        shot.save(r'C:\Users\green\AppData\Local\HOME Macros\img.png')

        im = Image.open(r"C:\Users\green\AppData\Local\HOME Macros\img.png")
        txt = tess.image_to_string(im)
        print("Read: " + txt)

        if not c:
            if txt == t:
                return True
            else:
                return False
        else:
            if txt == t:
                break

    pyautogui.click(x=px + w / 2, y=py + h / 2)

    return


def check_allpokemon(click=True):
    return check(108, 100, 150, 48, "All Pokémon", click)


def check_labels(click=False):
    return check(214, 74 - win_off, 60, 30, "Labels", click)


def check_exit(click=False):  # Doesn't Work
    return check(270, 814 - win_off, 36, 36, "X", click)


def check_box(tx_, click=False):
    px = 124
    py = 210 - win_off
    pw = 150
    ph = 64
    drag = 96 + 24
    bit = 4

    while True:
        found = check(px, py, pw, ph, tx_, click)

        img = Image.open(r"C:\Users\green\AppData\Local\HOME Macros\img.png")
        text = tess.image_to_string(img)

        if found:
            break
        else:
            pyautogui.moveTo(win_x + win_w / 2, win_y + win_h / 2)
            pyautogui.mouseDown()
            pyautogui.moveTo(win_x + win_w / 2, win_y + win_h / 2 - drag - bit, duration=0.25)
            pyautogui.moveTo(win_x + win_w / 2, win_y + win_h / 2 - drag, duration=0.125)
            pyautogui.mouseUp()

    pyautogui.click(x=win_x + px + pw / 2, y=win_y + py + ph / 2)
    return


def select_all():
    # Drag Up Just In Case

    st_x = win_x + 74
    st_y = win_y + 340 - win_off

    time.sleep(0.5)
    pyautogui.moveTo(x=st_x, y=st_y)
    pyautogui.mouseDown()
    pyautogui.moveTo(x=st_x, y=st_y + 400, duration=0.5)
    pyautogui.mouseUp()

    st_x = win_x + 74
    st_y = win_y + 340 - win_off
    spc_x = 106
    spc_y = 136

    pyautogui.mouseDown(x=st_x, y=st_y)
    time.sleep(3)
    pyautogui.mouseUp()

    j = 0
    while j < 4:
        i = 0
        while i < 5:
            if not (i == 0 and j == 0):
                pyautogui.click(x=st_x + i * spc_x, y=st_y + j * spc_y)
            time.sleep(0.125)
            i += 1
        j += 1

    st_x = win_x + 76
    st_y = win_y + 574 - win_off

    pyautogui.moveTo(x=st_x, y=st_y)
    pyautogui.mouseDown()
    pyautogui.moveTo(x=st_x, y=st_y - 400, duration=0.25)
    pyautogui.mouseUp()

    j = 0
    while j < 2:
        i = 0
        while i < 5:
            pyautogui.click(x=st_x + i * spc_x, y=st_y + j * spc_y)
            time.sleep(0.125)
            i += 1
        j += 1

    click(64, 834, 0.5)
    click(292, 555, 1.5)
    click(292, 574, 8)
    click(288, 834, 1)
    click(288, 172, 0)

    return


def click(x, y, sleep):
    pyautogui.click(win_x + x, win_y + y - win_off)
    time.sleep(sleep)
    return


def wonder_loop(pus_x, pus_y, to, start_at, counter):
    space = 104

    i = 0
    while i < to:
        if counter >= start_at:
            print("Opening Ball #"+str(counter+1)+".")
            click(pus_x + i * space, pus_y, 18)
            while True:
                if pyautogui.pixelMatchesColor(win_x + 392, win_y + 628 - win_off, (247, 251, 247), tolerance=10):
                    break
                else:
                    time.sleep(1)
            click(276, 648, 1)
        i += 1
        counter += 1

    return counter


def program_wonderopen():
    if len(sys.argv) > 2:
        if 0 < int(sys.argv[2]) <= 10:
            start_at = int(sys.argv[2]) - 1
        else:
            print("ERROR: Start value needs to be between 1 and 10.")
            sys.exit()
    else:
        start_at = 0

    at = 0

    at = wonder_loop(174, 288, 3, start_at, at)
    at = wonder_loop(122, 458, 4, start_at, at)
    at = wonder_loop(174, 624, 3, start_at, at)

    print("Enjoy your Pokémon! :)")

    return


# MAIN


if (len(sys.argv) > 1) and (sys.argv[1] == "-l"):
    if not check_labels():
        check_allpokemon()

    box = "HOME"
    count = 1

    while count < 60:
        tx = "{} {}".format(box, count)
        check_box(tx)
        time.sleep(0.5)
        select_all()
        count += 1


elif (len(sys.argv) > 1) and (sys.argv[1] == "-w"):
    program_wonderopen()

else:
    print("DexTool HOME v0.1 by @PoshoDev")
    print("-l\tAuto label.")
    print("-w\tOpen all completed Wonder trades.")
