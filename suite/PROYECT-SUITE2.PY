import pyautogui as auto
import time
from datetime import datetime
import logging
import sys
from NEEDED import OCRNico
from NEEDED import AutoGuiUtils

path = "//"
pathFotos = path +"fotos/"

arrParameters = []
for i, argument in enumerate(sys.argv):
    arrParameters.append(argument)
    arrParameters.append("DESKTOP")

try:
    ahora = datetime.now()
    diaDeLaSemana = ahora.isoweekday()
    hora = ahora.hour
    minute = ahora.minute

    path = "//"
    pathFotos = path + "fotos/"
    print("PATH:" + str(path))
    logging.basicConfig(filename=str(path)+'REGISTRO-PROYECT-SUITE.log', encoding='utf-8', level=logging.DEBUG)



    if diaDeLaSemana != 6 and diaDeLaSemana != 7:

        # 1 - CLEAN DESKTOP:
        if AutoGuiUtils.listaContiene(arrParameters, "DESKTOP"):
            time.sleep(2)
            auto.hotkey('winleft','d')
            time.sleep(3)

        # ME LOGEO PROYECT SUITE:
        # time.sleep(2)
        # poneteEn(path + "open-project-suite.png", False, True);
        # time.sleep(5)
        palabraHorario = OCRNico.sacarScreenshotYDamePosPalabra("SUITE", True)
        if palabraHorario != None:
            auto.click(palabraHorario.medio()[0], palabraHorario.medio()[1] - 20)
            auto.click()
        else:
            print("SUITE NO ENCONTRADO!")
        time.sleep(6)

        # #ME LOGEO PROYECT SUITE:
        # AutoGuiUtils.poneteEn(pathFotos + "input-username.png", True, False);
        # time.sleep(5)
        #
        # # #ME LOGEO PROYECT SUITE:
        # AutoGuiUtils.poneteEn(pathFotos + "x9260.png", True, False);
        # time.sleep(5)

        # #ME LOGEO PROYECT SUITE:
        AutoGuiUtils.poneteEn(pathFotos + "login-project-suite.png", True, False , False);
        time.sleep(10)


        # # CARTEL QUE NO:
        # auto.click(844,723)
        # time.sleep(3)

        #BOTON NUEVA CARGA:
        # AutoGuiUtils.poneteEn(pathFotos + "boton-nva-carga.png", True, False, False);
        # time.sleep(5)


        #BOTON NUEVA CARGA:
        AutoGuiUtils.poneteEn(pathFotos + "boton-nva-carga.png", True, False , False);
        time.sleep(5)

        palabraOnboarding = OCRNico.sacarScreenshotYDamePosPalabra("Onboarding", False)
        if palabraOnboarding != None:
            auto.click(palabraOnboarding.medio()[0], palabraOnboarding.medio()[1])
            print("ONBOARDING ENCONTRADO")
        else:
            print("ONBOARDING NO ENCONTRADO!")


        #
        # # 4 HORAS:
        # AutoGuiUtils.poneteEn( pathFotos + "fotos/4-hours.png", True, False);
        AutoGuiUtils.poneteEn(pathFotos + "zero-veinti-cinco.png", True, False,True);
        auto.hotkey('ctrl','a')
        auto.keyDown('backspace')
        auto.keyDown('backspace')
        auto.keyDown('backspace')
        auto.keyDown('backspace')
        auto.keyDown('backspace')
        auto.typewrite("12")
        time.sleep(3)

        # # COMBO CATEGORIAS:
        AutoGuiUtils.poneteEn(pathFotos + "combo-categoria.png", True, False, True);
        time.sleep(3)
        #
        # # CATEGORIA OTHERS:
        # AutoGuiUtils.poneteEn(pathFotos + "categoria-others.png", True, False, False);
        # time.sleep(3)
        auto.keyDown('o')
        auto.keyDown('t')
        auto.scroll(-100)
        time.sleep(3)

        #
        # # BOTON APPLY:
        AutoGuiUtils.poneteEn( pathFotos + "apply.png", True, False, True);
        time.sleep(3)


    # 6 - CERRAR IE:
    auto.click(1887, 20)
    time.sleep(3)

except Exception as e:
    logging.critical(e, exc_info=True)
