import pyautogui
from pynput.mouse import Controller
import os
from pathlib import Path
import time
import keyboard
import win32api, win32con

mouse= Controller()
main_path = Path(__file__).parent

while 1:
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    img = pyautogui.locateCenterOnScreen(f'{main_path}\image\-Color.png', grayscale=False, confidence=0.9)

    if keyboard.is_pressed("P"):
        break

    if img is not None:
        pyautogui.leftClick(img)
        pyautogui.rightClick(img)
        print(current_time,"Une case en",mouse.position)
