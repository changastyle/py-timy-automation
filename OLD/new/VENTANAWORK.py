import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x500")
ventana.title("WORK")

status = tk.StringVar()
textArea= -1

# def play():
#     WORK.workingLoop = True
#     WORK.sleepingTime = int(inputSleepingTime.get())
#     WORK.hilo(textArea)
#     status.set("Status: PLAY")
#
# def stop():
#     WORK.workingLoop = False
#     status.set("Status: STOPED")
# def quit():
#     WORK.hiloFinish()




inputSleepingTime = tk.Entry(ventana)
inputSleepingTime.pack()
# inputSleepingTime.insert(0,str(WORK.sleepingTime))

lblStatus = tk.Label(ventana, textvariable=status).pack()

btnPlay = tk.Button(ventana, text="Play" ,padx= 20 , pady=20)
btnPlay.pack()

btnStop = tk.Button(ventana, text="Stop",padx= 20 , pady=20)
btnStop.pack()

btnQuit = tk.Button(ventana, text="Quit",padx= 20 , pady=20)
btnQuit.pack()


textArea = tk.Text(ventana, height=8, width=30)
textArea.pack()



ventana.mainloop()