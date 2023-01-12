import pyautogui
import time
import datetime as dt

screenWidth, screenHeigth = pyautogui.size();

hoy = dt.datetime.today()
print("PROYECT SUITE :" + str(hoy.weekday())  )

if hoy.weekday() != 5 and hoy.weekday() != 0:

    # ABRO MY TIME:
    time.sleep(2)
    pyautogui.hotkey('winleft','d')
    time.sleep(3)

    # ABRO IE:
    pyautogui.click(231,46)
    pyautogui.click();
    time.sleep(5)

    #ME LOGEO PROYECT SUITE:
    pyautogui.click(126,498)
    time.sleep(12)

    #CARTEL QUE NO:
    pyautogui.click(844,723)
    time.sleep(3)

    #BOTON NUEVA CARGA:
    pyautogui.click(1750,483)
    time.sleep(3)

    #BOTON NUEVA CARGA:
    pyautogui.click(1750,483)
    time.sleep(3)

    if hoy.hour < 9:
        #ANTES DE LAS 9 -> TRAINING - 2HS:

        # MY LAST BOOKED TASK:
        pyautogui.click(508,493)
        time.sleep(10)

        #MAIL SERVICES:
        # pyautogui.click(416,717)
        pyautogui.click(224,784)
        time.sleep(2)

        # SCROLLEO PARA ABAJO UN TOQUE:
        pyautogui.scroll(-150)
        time.sleep(2)

        #2 HORA - YA SCROLEADO>
        pyautogui.click(889,779)
        time.sleep(2)

        # OPEN COMBO CATEGORY YA SCROLEADO
        pyautogui.click(590,858)
        time.sleep(2)

        # CATEGORY OTHER:
        pyautogui.click(471,655)
        time.sleep(2)

        # BOTON APPLY SCROLEADO:
        pyautogui.click(1548,976)
        time.sleep(2)

    elif hoy.hour > 9 and hoy.hour < 10:

        # ENTRE LAS 9 Y LAS 10 -> AGILE CEREMONIES - 1HR:

        # MY LAST BOOKED TASK:
        pyautogui.click(508,493)
        time.sleep(3)

        #AGILE CEREMONIES:
        pyautogui.click(338,787)
        time.sleep(2)

        # SCROLLEO PARA ABAJO UN TOQUE:
        pyautogui.scroll(-100)
        time.sleep(2)

        #1 HORA - YA SCROLEADO>
        pyautogui.click(769,790 )
        time.sleep(2)

        # OPEN COMBO CATEGORY YA SCROLEADO
        pyautogui.click(590,858)
        time.sleep(2)

        # CATEGORY OTHER:
        pyautogui.click(471,655)
        time.sleep(2)

        # BOTON APPLY SCROLEADO:
        pyautogui.click(1548,976)
        time.sleep(2)
    else:

        #POR LA TARDE ONBOARDING - 4HR:

        #BOTON ONBOARDING:
        pyautogui.click(219,713)
        time.sleep(3)

        #4HR:
        pyautogui.click(999,722)
        time.sleep(3)

        # #COMBO ACTIVIDAD:
        pyautogui.click(590,782)
        time.sleep(3)

        # #TECH ACTIVIDAD:
        pyautogui.click(424,702)
        time.sleep(3)

        # #BOTON APLLY:
        pyautogui.moveTo(1549,962)
        time.sleep(3)

    # # CERRAR IE:
    # pyautogui.click(1887,20)
    # time.sleep(3)

    #CLICK BARRA BUSQUEDA:
    # pyautogui.click(213,514)
    # time.sleep(3)
    #
    # pyautogui.typewrite("onboarding");
    # pyautogui.press("enter")
    # time.sleep(3)
    #
    # # BOTON OFICINA:
    # pyautogui.click(646,595)
    # time.sleep(3)
    #
    # # BOTON SALIDA
    # pyautogui.click(560,717)
    # time.sleep(3)
    #


    #SALIDA DE LA OFFICE
    # pyautogui.click(559,714)


    # while True:
    #       mouseX, mouseY = pyautogui.position();
    #       print("MOUSE: (" + str(mouseX)  + "," +  str(mouseY),")")
    #       time.sleep(3)