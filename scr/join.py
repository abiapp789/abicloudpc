import pyautogui
import time
import os

pyautogui.FAILSAFE = True


os.startfile(r"C:\Users\Public\Desktop\Zoom Workplace.lnk")
time.sleep(0.76)
pyautogui.click(x=702, y=303, button="left")
time.sleep(1.28)
pyautogui.click(x=849, y=479, button="left")
time.sleep(1.67)
pyautogui.write("83241465223", interval=0.02)
time.sleep(1.29)
pyautogui.click(x=979, y=649, button="left")
time.sleep(2.23)
pyautogui.click(x=988, y=486, button="left")
time.sleep(1.88)
pyautogui.write("245522", interval=0.02)
time.sleep(1.08)
pyautogui.click(x=997, y=651, button="left")
time.sleep(4.09)
