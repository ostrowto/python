# mouse_Move.py

import pyautogui

print('Your screen resolution is: ', pyautogui.size())
print('How long should the program run? ')

input_time = int(input('Please input how long the program should run \n - in seconds (whole numbers only)?\n ... and please press enter   '))

print('Your mouse will be active during ', input_time,  'seconds')
print('Press CTRL+C for interrupt the running program')

pyautogui.moveTo(800, 600, duration = input_time)