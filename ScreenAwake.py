#!/usr/bin/python
import pyautogui,time
pyautogui.FAILSAFE = False
def keepAwake():
    pyautogui.press('f22') #simple keyboard move which keeps screen awake by pressing hotkey every 59 seconds
    time.sleep(60)
while True:
    keepAwake()
#keepAwakeSqaure function will make a square movement in cursor every 59 seconds similar to keepAwake Function
#uncomment the lines to use keepAwakeSqaure
'''
def keepAwakeSqaure():#this will make a square movement in cursor every 59 seconds
    for i in range(10):
      pyautogui.moveTo(100, 100, duration=0.25)
      pyautogui.moveTo(200, 100, duration=0.25)
      pyautogui.moveTo(200, 200, duration=0.25)
      pyautogui.moveTo(100, 200, duration=0.25)
      time.sleep(59)
while True:
    keepAwakeSqaure()
'''
#Script can be killed by executing'Ctrl + C' in Terminal
