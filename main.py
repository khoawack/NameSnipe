import pyautogui
import time

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

    pyautogui.click(blue_e)
    pyautogui.click(blue_e)
    pyautogui.click(blue_e)

    # pyautogui.moveTo(blue_e)  # remember to change to pyautogui.click(blue_e)
    # pyautogui.moveTo(blue_e)
    # pyautogui.moveTo(blue_e)

name_time()




from account import Account

# desired_name = "lmly"
#-------------------------------------------------------------- coords checker
# while True:
#     riot = pyautogui.position()
#     time.sleep(1)
#     print(riot)

# name = (626, 320)




# pyautogui.click(name)
# pyautogui.typewrite(desired_name)

# time.sleep(3)








#login-----------------------------------------------------
# user1 = Account("khoa")
#
# riot = (847, 1064)
# user_cord = (351, 365)
# password_cord = (325, 429)
# enter = (401, 801)
#
# pyautogui.click(riot)
# time.sleep(8)
# pyautogui.click(user_cord)
# time.sleep(.4)
# user1.user()
#
# pyautogui.click(password_cord)
# user1.password()
#
# pyautogui.click(enter)

