import pyautogui
import time

# pip install keyboard | pip install PyAutoGUI

check = (754, 335)
blue_e = (765, 444)

def name_time():
    while True:
        now = time.localtime()
        print(now[3], ":", now[4], ":", now[5])

        if int(now[3]) == 16:
            sniper()
            break


def sniper():
    pyautogui.click(check)
    
    pyautogui.moveTo(blue_e)  # remember to change to pyautogui.click(blue_e)
    pyautogui.moveTo(blue_e)
    pyautogui.moveTo(blue_e)

name_time()
