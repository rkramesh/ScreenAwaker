#!/usr/bin/python
import pyautogui,time

def keepAwake():#simple cursor move which keeps screen awake by moving cursor every 59 seconds
    pyautogui.moveTo(100, 100, duration=1)
    time.sleep(59)
while True:
    keepAwake()
#the script can be killed by executing'Ctrl + C' in Terminal

'''uncomment the lines to use keepAwakeSqaure 
def keepAwakeSqaure():#this will make a square movement in cursor every 59 seconds
    for i in range(10):
      pyautogui.moveTo(100, 100, duration=0.25)
      pyautogui.moveTo(200, 100, duration=0.25)
      pyautogui.moveTo(200, 200, duration=0.25)
      pyautogui.moveTo(100, 200, duration=0.25)
while True:
    keepAwakeSqaure()
'''
