import pyautogui
import random as rand


random = rand.random();

maxWidth, maxHeigth = pyautogui.size()
nuevoY = int(random * maxHeigth)
nuevoX = int(random * maxWidth)
pyautogui.moveTo(nuevoX, nuevoY)

print("ME MOVI: " + str(nuevoX) + " , " + str(nuevoY))