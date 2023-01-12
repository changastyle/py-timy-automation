import pyautogui
import time
import datetime as dt

screenWidth, screenHeigth = pyautogui.size();

print("PANTALLA: " + str(screenWidth) + " x " + str(screenHeigth) +" PX" )
hoy = dt.datetime.today()
print("DIA:" + str(hoy.weekday()))

if hoy.weekday() != 5 : #and hoy.weekday() != 1

    # ABRO MY TIME:
    time.sleep(2)
    pyautogui.hotkey('winleft','d')
    time.sleep(3)

    # ABRO IE:
    pyautogui.click(139,32)
    pyautogui.click()
    time.sleep(3)

    # ME LOGEO EN MY TIME:
    pyautogui.click(921,546)
    time.sleep(3)

    # LA PRIMERA VEZ DEL DIA EL BOTON ES MAS GRANTE TIENE OTRA DISTRIBUCION:
    if hoy.hour < 10:

        # BOTON OFICINA:
        pyautogui.click(929,595)
        time.sleep(5)

        # BOTON SALIDA
        pyautogui.click(753,716)
        time.sleep(5)

    else:
        # BOTON OFICINA:
        pyautogui.click(646,595)
        time.sleep(5)

        # BOTON SALIDA
        pyautogui.click(560,717)
        time.sleep(5)


    # CERRAR IE:
    pyautogui.click(1887,20)
    time.sleep(3)

    #SALIDA DE LA OFFICE
    # pyautogui.click(559,714)


    # while True:
    #       mouseX, mouseY = pyautogui.position();
    #       print("MOUSE: (" + str(mouseX)  + "," +  str(mouseY),")")
    #       time.sleep(3)