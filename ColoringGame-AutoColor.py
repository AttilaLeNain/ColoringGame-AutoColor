import pyautogui
import os
from pathlib import Path
import time
import keyboard
import win32api, win32con

main_path = Path(__file__).parent

while 1:

    img = pyautogui.locateCenterOnScreen(f'{main_path}\image\-Color.png', grayscale=False, confidence=0.9)

    if keyboard.is_pressed("P"):
        break

    if img is not None:
        pyautogui.leftClick(img)
        pyautogui.rightClick(img)
