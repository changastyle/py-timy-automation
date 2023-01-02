import pyautogui
import time
import datetime as dt

screenWidth, screenHeigth = pyautogui.size();

print("PANTALLA: " + str(screenWidth) + " x " + str(screenHeigth) +" PX" )
hoy = dt.datetime.today()

if hoy.weekday() != 5 and hoy.weekday() != 1:

    # ABRO MY TIME:
    time.sleep(2)
    pyautogui.hotkey('winleft','d')
    time.sleep(3)
    pyautogui.click(139,32)
    pyautogui.click();
    time.sleep(3)
    pyautogui.click(921,546)
    time.sleep(3)

    # BOTON OFICINA:
    pyautogui.click(646,595)
    time.sleep(3)

    #BOTON SALIDA
    pyautogui.click(560,717)
    time.sleep(3)
    pyautogui.click(1887,20)
    time.sleep(3)

    #SALIDA DE LA OFFICE
    # pyautogui.click(559,714)


    # while True:
    #       mouseX, mouseY = pyautogui.position();
    #       print("MOUSE: (" + str(mouseX)  + "," +  str(mouseY),")")
    #       time.sleep(3)