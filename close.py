import pyautogui as auto
import time

xMax, yMax = auto.size();

print("xMAX:" + str(xMax))
time.sleep(2)
auto.moveTo((xMax - 35), 20)
