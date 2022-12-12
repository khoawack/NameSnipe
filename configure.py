import pyautogui
import keyboard

# pip install keyboard | pip install PyAutoGUI


while True:
    # hover over check button and press q to get check coords
    if keyboard.read_key() == "q":
        check = pyautogui.position()
        print("Check coordinate:", check)

    # hover over BE button and press w to get check coords
    if keyboard.read_key() == "w":
        BE = pyautogui.position()
        print("Blue Essence coordinate:", BE)