import cv2
import pyautogui
import time

def secondaryLogin():
    tmp = pyautogui.locateCenterOnScreen("resources/w.png")
    pyautogui.moveTo(tmp[0], tmp[1], 0.1)
    pyautogui.click()

    tmp = pyautogui.locateCenterOnScreen("resources/l.png")
    pyautogui.moveTo(tmp[0], tmp[1], 0.1)
    pyautogui.click()

    tmp = pyautogui.locateCenterOnScreen("resources/d.png")
    pyautogui.moveTo(tmp[0], tmp[1], 0.1)
    pyautogui.click()

    tmp = pyautogui.locateCenterOnScreen("resources/m.png")
    pyautogui.moveTo(tmp[0], tmp[1], 0.1)
    pyautogui.click()

    tmp = pyautogui.locateCenterOnScreen("resources/s.png")
    pyautogui.moveTo(tmp[0], tmp[1], 0.1)
    pyautogui.click()

    tmp = pyautogui.locateCenterOnScreen("resources/1.png")
    pyautogui.moveTo(tmp[0], tmp[1], 0.1)
    pyautogui.click()

    tmp = pyautogui.locateCenterOnScreen("resources/5.png")
    pyautogui.moveTo(tmp[0], tmp[1], 0.1)
    pyautogui.click()

    tmp = pyautogui.locateCenterOnScreen("resources/2.png")
    pyautogui.moveTo(tmp[0], tmp[1], 0.1)
    pyautogui.click()


secondaryLogin()
