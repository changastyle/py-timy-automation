import tkinter as tk
import WORK
import pyautogui
import random as rand
import time

ventana = tk.Tk()
ventana.geometry("400x500")
ventana.title("WORK")

status = tk.StringVar()
sleepingTime = 10
textArea = tk.Text()
workingLoop = False

def play():
    WORK.workingLoop = True
    WORK.sleepingTime = int(inputSleepingTime.get())
    WORK.hilo(textArea)
    status.set("Status: PLAY")

    maxWidth, maxHeigth = pyautogui.size()
    out = "WORKING (" + str(maxWidth) +"," + str(maxHeigth) + "):"
    print(out)
    textArea.insert(tk.END, str(out + "\n"))


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




inputSleepingTime = tk.Entry(ventana)
inputSleepingTime.pack()
inputSleepingTime.insert(0,str(WORK.sleepingTime))

lblStatus = tk.Label(ventana, textvariable=status).pack()

btnPlay = tk.Button(ventana, text="Play" ,padx= 20 , pady=20, command=lambda: play())
btnPlay.pack()

btnStop = tk.Button(ventana, text="Stop",padx= 20 , pady=20, command=lambda:stop())
btnStop.pack()

btnQuit = tk.Button(ventana, text="Quit",padx= 20 , pady=20, command=lambda:quit())
btnQuit.pack()


textArea = tk.Text(ventana, height=8, width=30)
textArea.pack()



ventana.mainloop()