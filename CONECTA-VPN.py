import time

import pytesseract
import cv2
from pytesseract import Output
import pyautogui as auto
from NEEDED.Word import Word
import pyautogui as auto
import AutoRecursivo
import logging
import pytesseract
import time

path = "C:/Users/e107580/Desktop/CODE/TIMY/"
pathFotos = path + "fotos-vpn/"
url = "https://fiorirh.intrallianz.es:4443/sap/bc/ui2/flp/FioriLaunchpad.html?sap-client=200&sap-language=ES#manage-clocktime"
clave="JaimePuto33"
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\e107580\AppData\Local\Programs\Tesseract-OCR2\tesseract.exe'
logging.basicConfig(filename=str(path) + 'LOG-VPN.log', encoding='utf-8', level=logging.DEBUG)
def main():
    print("CONECTO LA VPN AL INICIAR:")
    abrirAnyConect()
    dameBtnConectar()
    ponerPassword()
    time.sleep(10)
    botonAceptar()

def dameBtnConectar():
    posBtnConectar = AutoRecursivo.poneteEn(pathFotos + "btn-conectar.png")
    print("VEO BOTON DE CONECTAR:" + str(posBtnConectar))
    if posBtnConectar == -1:
        abrirAnyConect()
    else:
        auto.moveTo(posBtnConectar.x, posBtnConectar.y)
        auto.click()
        time.sleep(2)
def ponerPassword():
    posPassword = AutoRecursivo.poneteEn(pathFotos + "btnPassword.png")
    print("VEO PASSWORD:" + str(posPassword))
    if posPassword == -1:
        dameBtnConectar()
    else:
        auto.typewrite(clave)
        auto.hotkey("enter")
        time.sleep(3)
def botonAceptar():
    posPassword = AutoRecursivo.poneteEn(pathFotos + "btn-aceptar.png")
    print("VEO BTN ACEPTAR:" + str(posPassword))
    if posPassword == -1:
        botonAceptar()
    else:
        auto.moveTo(posPassword.x, posPassword.y)
        auto.click()
        time.sleep(2)
def abrirAnyConect():

    auto.hotkey("win")
    auto.typewrite("VPN")
    auto.hotkey("enter")

    time.sleep(2)

main()