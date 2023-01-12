import pyautogui as auto
import time
import datetime as dt

def poneteEn(imagenName,click, dobleClick):

    posicion = None

    while posicion is None:
        time.sleep(1)
        posicion = auto.locateOnScreen(imagenName, grayscale=True, confidence=.8)
        # break

    posicionCenter = auto.center(posicion)
    if click:
        auto.click(posicionCenter.x, posicionCenter.y)
    elif dobleClick:
        auto.click(posicionCenter.x, posicionCenter.y)
        auto.click()
    else:
        auto.moveTo(posicionCenter.x, posicionCenter.y)

    print("POSITION:" + str(posicion))

    return posicionCenter

screenWidth, screenHeigth = auto.size();

hoy = dt.datetime.today()
print("PROYECT SUITE :" + str(hoy.weekday())  )

if hoy.weekday() != 5 and hoy.weekday() != 0:

    # 1 - CLEAN DESKTOP:
    time.sleep(2)
    auto.hotkey('winleft','d')
    time.sleep(3)

    # ABRO PROYECT SUITE:
    auto.click(231,46)
    auto.click();
    time.sleep(12)

    #ME LOGEO PROYECT SUITE:
    poneteEn("fotos/login-ps.png", True, False);
    time.sleep(5)

    # #CARTEL QUE NO:
    auto.click(844,723)
    time.sleep(3)
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
    poneteEn("fotos/4-hours.png", True, False);
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


