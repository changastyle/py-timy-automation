import pyautogui as auto
import pytesseract
import cv2
import time
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
