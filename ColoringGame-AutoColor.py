from tkinter import Button
import pyautogui
import os
from pathlib import Path
import time
import keyboard
import win32api, win32con

main_path = Path(__file__).parent

while 1:
    if keyboard.is_pressed("P"):
	    break

    else:
        coordonnées = pyautogui.locateCenterOnScreen(f'{main_path}\image\-Color.png', grayscale=False, confidence=0.9)
        pyautogui.leftClick(coordonnées)
        pyautogui.rightClick(coordonnées)
