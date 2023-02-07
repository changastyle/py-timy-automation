import pyautogui as auto
from datetime import datetime
import time
import sys
import logging
from NEEDED import OCRNico
def listaContiene(lista , valor):
    si = False
    if any(valor in str for str in lista):
        si = True

    return si
def poneteEn(imagenName,click, dobleClick , altaPrecicion):

    posicion = None
    reintentos = 3

    while reintentos >= 1:
        precision = reintentos * 0.3
        print("|------------------ " + str(imagenName) +" ------------------|")
        print("|    REINTENTOS: " + str(reintentos) + " - PRECISION: " + str(precision))
        logging.info("|------------------ " + str(imagenName) +" ------------------|")
        logging.info("|    REINTENTOS: " + str(reintentos) + " - PRECISION: " + str(precision))
        posicion = auto.locateOnScreen(imagenName, grayscale=True, confidence=precision)
        print("|    posicion:" +  str(posicion))
        logging.info("|    posicion:" +  str(posicion))

        if not altaPrecicion:
            reintentos = reintentos - 1
        time.sleep(1)

        if posicion != None:
            print("|    break")
            logging.info("|    break")
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
        logging.info("|    POSITION:" + str(posicion))
        print("|----------------------------------------------|\n")
        logging.info("|----------------------------------------------|\n")
        return posicionCenter
def damePos(imagenName,escalaGrises,altaPrecicion):

    posicion = None

    precision = 2 * 0.33
    print("|------------------ " + str(imagenName) +" ------------------|")
    print("|    REINTENTOS: " + str(reintentos) + " - PRECISION: " + str(precision))
    posicion = auto.locateOnScreen(imagenName, grayscale=escalaGrises, confidence=precision)
    print("|    posicion:" +  str(posicion))

    return posicion