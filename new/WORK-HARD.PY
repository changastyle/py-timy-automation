import pyautogui
import random as rand
import time
import threading
import VENTANAWORK as ventana
workingLoop = True
sleepingTime = 30

maxWidth, maxHeigth = pyautogui.size()
print("WORKING (" + str(maxWidth) +"," + str(maxHeigth) + "):")

lastX = -1
lastY = -1

while workingLoop:

    # 1 - TRAE POSICION ACTUAL MOUSE:
    currentMouseX, currentMouseY = pyautogui.position()

    # 2 - GENERA UN NUMERO RANDOM:
    random = rand.random();

    noMeMovi = True

    # 3 - TRAIGO X , Y
    print("LASTX:" + str(lastX) +","+ str(lastY) + " -> NOW: " + str(currentMouseX) +"," + str(currentMouseY))

    if lastX == -1 or lastY == -1:
        noMeMovi = True

    if lastX != currentMouseX and lastY != currentMouseY:
        noMeMovi = False


    if noMeMovi:
        # 4 - SI NO ME MUEVO, ENTONCES GENERO UN NUEVO NUMERO RANDOM Y MUEVO EL MOUSE:
        nuevoY = int(random * maxHeigth)
        nuevoX = int(random * maxWidth)
        pyautogui.moveTo(nuevoX, nuevoY)

        # MOVER EL MOUSE A POSICION:
        print("NEW POSITION: (" + str(nuevoX) + "," + str(nuevoY) + ")")

    currentMouseX, currentMouseY = pyautogui.position()
    lastX = currentMouseX
    lastY = currentMouseY
    time.sleep(sleepingTime)