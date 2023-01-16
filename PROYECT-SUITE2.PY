import pyautogui as auto
import time
from datetime import datetime

def poneteEn(imagenName,click, dobleClick):

    posicion = None
    reintentos = 3
    while reintentos >= 1:
        precision = reintentos * 0.3
        print("|------------------ " + str(imagenName) +" ------------------|")
        print("|    REINTENTOS: " + str(reintentos) + " - PRECISION: " + str(precision))
        posicion = auto.locateOnScreen(imagenName, grayscale=True, confidence=precision)
        print("|    posicion:" +  str(posicion))
        reintentos = reintentos - 1
        time.sleep(1)

        if posicion != None:
            print("|    break")
            break

    if posicion is not None:
        posicionCenter = auto.center(posicion)
        if click:
            auto.click(posicionCenter.x, posicionCenter.y)
        elif dobleClick:
            auto.click(posicionCenter.x, posicionCenter.y)
            auto.click()
        else:
            auto.moveTo(posicionCenter.x, posicionCenter.y)

        print("|    POSITION:" + str(posicion))
        print("|----------------------------------------------|\n")
        return posicionCenter

screenWidth, screenHeigth = auto.size();

ahora = datetime.now()
diaDeLaSemana = ahora.isoweekday()
print("PROYECT SUITE :" + str(diaDeLaSemana)  )

if diaDeLaSemana != 6 and diaDeLaSemana != 7:

    # 1 - CLEAN DESKTOP:
    time.sleep(2)
    auto.hotkey('winleft','d')
    time.sleep(3)

    # ME LOGEO PROYECT SUITE:
    time.sleep(2)
    poneteEn("fotos/open-project-suite.png", False, True);
    time.sleep(5)

    #ME LOGEO PROYECT SUITE:
    poneteEn("fotos/input-username.png", True, False);
    time.sleep(5)

    #ME LOGEO PROYECT SUITE:
    poneteEn("fotos/x9260.png", True, False);
    time.sleep(5)

    #ME LOGEO PROYECT SUITE:
    poneteEn("fotos/login-project-suite.png", True, False);
    time.sleep(5)

    # CARTEL QUE NO:
    # auto.click(844,723)
    # time.sleep(3)
    #
    # #BOTON NUEVA CARGA:
    poneteEn("fotos/boton-nva-carga.png", True, False);
    time.sleep(5)
    # auto.click(1750,483)
    # time.sleep(3)

    # #BOTON NUEVA CARGA:
    poneteEn("fotos/onboarding.png", True, False);
    time.sleep(5)

    # 4 HORAS:
    # poneteEn("fotos/4-hours.png", True, False);
    poneteEn("fotos/zero-veinti-cinco.png", True, False);
    auto.keyDown('backspace')
    auto.keyDown('backspace')
    auto.keyDown('backspace')
    auto.keyDown('backspace')
    auto.keyDown('backspace')
    auto.typewrite("12")
    time.sleep(3)

    # COMBO CATEGORIAS:
    poneteEn("fotos/combo-categoria.png", True, False);
    time.sleep(3)

    # CATEGORIA OTHERS:
    poneteEn("fotos/categoria-others.png", True, False);
    time.sleep(3)

    # BOTON APPLY:
    poneteEn("fotos/apply.png", True, False);
    time.sleep(3)


