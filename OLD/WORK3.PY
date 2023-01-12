import pyautogui
import random as rand
import time
import threading
import tkinter as tk

workingLoop = True
sleepingTime = 30
textArea = -1
hiloGlobal: tk.Text
def hilo(textAreaRec):
    hiloGlobal = threading.Thread(target=working)
    hiloGlobal.start()
    textArea = textAreaRec
def hiloFinish():
    hiloGlobal.join()
def working():
    maxWidth, maxHeigth = pyautogui.size()
    out = "WORKING (" + str(maxWidth) +"," + str(maxHeigth) + "):"
    print(out)
    textArea.insert(tk.END, out + "\n")


    lastX = -1
    lastY = -1

    while workingLoop:

        # 1 - TRAE POSICION ACTUAL MOUSE:
        currentMouseX, currentMouseY = pyautogui.position()

        # 2 - GENERA UN NUMERO RANDOM:
        random = rand.random();

        noMeMovi = True

        # 3 - TRAIGO X , Y
        out = "LASTX:" + str(lastX) +","+ str(lastY) + " -> NOW: " + str(currentMouseX) +"," + str(currentMouseY)
        print(out + "\n")
        textArea.insert(tk.END, out + "\n")

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
            out2 ="NEW POSITION: (" + str(nuevoX) + "," + str(nuevoY) + ")"
            print(out2)
            textArea.insert(tk.END, out2 + "\n")

        currentMouseX, currentMouseY = pyautogui.position()
        lastX = currentMouseX
        lastY = currentMouseY
        time.sleep(sleepingTime)