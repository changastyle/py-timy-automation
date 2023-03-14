import time

import pytesseract
import cv2
from pytesseract import Output
import pyautogui as auto
from NEEDED.Word import Word
import pyautogui as auto

path = "C:/Users/e107580/Desktop/CODE/TIMY/"
pathFotos = path + "fotos/"
url = "https://fiorirh.intrallianz.es:4443/sap/bc/ui2/flp/FioriLaunchpad.html?sap-client=200&sap-language=ES#manage-clocktime"

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\e107580\AppData\Local\Programs\Tesseract-OCR2\tesseract.exe'

def main():
    print("Hola")

    abrirChrome()

    # time.sleep(3)
    # auto.hotkey("tab")
    # auto.hotkey("tab")
    # auto.hotkey("enter")

    # dameOficina()
    # dameEntrada()
    # dameSalida()
def dameSalida():
    posVeoFecha = poneteEn(pathFotos + "fecha.png")
    print("VEO FECHA:" + str(posVeoFecha))
    if posVeoFecha == -1:

        print("ESPERO HASTA VER FECHA")
        time.sleep(2)
        dameEntrada()
    else:
        auto.moveTo(posVeoFecha.x, posVeoFecha.y)
        auto.click()
        time.sleep(2)

        print("CONTROL F")
        auto.hotkey("esc")
        auto.hotkey("ctrl","f")
        auto.typewrite("Salida")
        auto.hotkey("enter")
        posSalida1 = poneteEn(pathFotos + "salida1.png");


        if posSalida1 == -1:

            posSalida2 = poneteEn(pathFotos + "salida2.png")
            if posSalida2 == -1:
                logearse()
            else:
                auto.moveTo(posSalida2.x, posSalida2.y)
                auto.click()
        else:
            auto.moveTo(posSalida1.x, posSalida1.y)
            auto.click()
def dameEntrada():
    posVeoFecha = poneteEn(pathFotos + "fecha.png")
    print("VEO FECHA:" + str(posVeoFecha))
    if posVeoFecha == -1:

        print("ESPERO HASTA VER FECHA")
        time.sleep(2)
        dameEntrada()
    else:
        auto.moveTo(posVeoFecha.x, posVeoFecha.y)
        auto.click()
        time.sleep(2)

        print("CONTROL F")
        auto.hotkey("esc")
        auto.hotkey("ctrl","f")
        auto.typewrite("Entrada")
        auto.hotkey("enter")
        posEntrada1 = poneteEn(pathFotos + "entrada1.png");


        if posEntrada1 == -1:

            posEntrada2 = poneteEn(pathFotos + "entrada2.png")
            if posEntrada2 == -1:
                logearse()
            else:
                auto.moveTo(posEntrada2.x, posEntrada2.y)
                auto.click()
        else:
            auto.moveTo(posEntrada1.x, posEntrada1.y)
            auto.click()
def dameOficina():
    posVeoFecha = poneteEn(pathFotos + "fecha.png")
    print("VEO FECHA:" + str(posVeoFecha))
    if posVeoFecha == -1:

        print("ESPERO HASTA VER FECHA")
        time.sleep(2)
        dameOficina()
    else:
        auto.moveTo(posVeoFecha.x, posVeoFecha.y)
        auto.click()
        time.sleep(2)

        print("CONTROL F")
        auto.hotkey("esc")
        auto.hotkey("ctrl","f")
        auto.typewrite("Oficina")
        auto.hotkey("enter")
        posOffice = poneteEn(pathFotos + "office.png");


        if posOffice == -1:

            posOffice2 = poneteEn(pathFotos + "office2.png")
            if posOffice2 == -1:
                logearse()
            else:
                auto.moveTo(posOffice2.x, posOffice2.y)
                auto.click()
        else:
            auto.moveTo(posOffice.x, posOffice.y)
            auto.click()
def abrirChrome():

    # posChrome = poneteEn(pathFotos + "chrome.png")
    # if posChrome == -1:
    auto.hotkey("win")
    auto.typewrite("chrome")
    auto.hotkey("enter")

    time.sleep(2)
    dameBarraURL()
    # else:
    #     print("ENCONTRE CHROME")
    #     auto.moveTo(posChrome.x, posChrome.y)
    #     auto.click()
    #

def dameNewTab():
    posTabMT = poneteEn(pathFotos + "tabMyTime.png")

    if posTabMT == -1:
        print("ABRO NEW TAB")
        # abrirChrome()
        posTab = poneteEn(pathFotos + "newTab.png");
        auto.moveTo(posTab.x, posTab.y)
        auto.click()

        dameBarraURL()
    else:
        print("ENCONTRE TAB MY TIME")
        auto.moveTo(posTabMT.x, posTabMT.y)
        auto.click()
def dameBarraURL():

    posBarra = poneteEn(pathFotos + "barraBusqueda.png");

    if posBarra == -1:
        dameNewTab()
    else:
        auto.moveTo(posBarra.x, posBarra.y)
        auto.click()

        auto.typewrite(url)
        auto.hotkey('enter')

        logearse()
def logearse():

    posLogin = poneteEn(pathFotos + "login.png");

    if posLogin == -1:
        dameBarraURL()
    else:
        auto.moveTo(posLogin.x, posLogin.y + 120)
        auto.click()

def poneteEn(imagenName):
    posicionCenter = -1
    posicion = None
    reintentos = 3
    cant = 0

    while cant < 5:
        precision = reintentos * 0.3
        print("|------------------ " + str(imagenName) +" ------------------|")
        print("|    CANT-REINTENTOS: " + str(cant) + " - PRECISION: " + str(precision))
        posicion = auto.locateOnScreen(imagenName, grayscale=True, confidence=precision)
        print("|    posicion:" +  str(posicion))
        cant = cant +1
        time.sleep(1)

        if posicion != None:

            print("|    POSITION:" + str(posicion))
            print("|----------------------------------------------|\n")
            posicionCenter = auto.center(posicion)


            print("|    break")
            break

    return posicionCenter
def sacarScreenshotYDamePosPalabra(nombrePalabraBuscada ,verbose):
    rutaImagen = "../screenshot.png"

    print("SACANDO SCREENSHOT")
    im1 = auto.screenshot()
    im1.save(rutaImagen)

    return damePosCentralDePalabraEnImagen(rutaImagen,nombrePalabraBuscada, verbose)
def damePosCentralDePalabraEnImagen(rutaImagen , nombrePalabraBuscada , verbose):
    rta = None

    img = cv2.imread(rutaImagen)
    BW = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    results = pytesseract.image_to_data(BW ,output_type=Output.DICT)
    arrResultadosTexto = results["text"]

    arrPalabras = []
    i = 0
    for nombre in arrResultadosTexto:
        x = results["left"][i]
        y = results["top"][i]
        w = results["width"][i]
        h = results["height"][i]
        wordLoop = Word(nombre,x,y,h,w)

        if len(str(nombre).strip()) > 1:
            arrPalabras.append(wordLoop)
        i = i + 1


    for palabraLoop in arrPalabras:
        if verbose:
            print(str(palabraLoop))
        if nombrePalabraBuscada in palabraLoop.nombre:
            rta = palabraLoop
            break

    return rta


def buscarIconoChrome():
    rta = False

    palabraHorario = OCRNico.sacarScreenshotYDamePosPalabra("HORARIO", True)
    if palabraHorario != None:
        auto.click(palabraHorario.medio()[0], palabraHorario.medio()[1] - 20)
        auto.click()
        rta = True
    else:
        print("HORARIO NO ENCONTRADO!")

    return rta


main()