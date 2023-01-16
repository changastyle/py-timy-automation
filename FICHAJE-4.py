import pyautogui as auto
from datetime import datetime
import time
import sys
import logging

print(f"CANTIDAD DE PARAMTROS: {len(sys.argv)}")
arrParameters = []
for i, argument in enumerate(sys.argv):
    arrParameters.append(argument)

# arrParameters.append("MORNING")
# arrParameters.append("AFTERNOON")
for parameterLoop in arrParameters:
  print(parameterLoop)

# print("HOY ES: " + str(diaSemana))

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

ahora = datetime.now()
diaDeLaSemana = ahora.isoweekday()
hora = ahora.hour;

pathLog ="C:/Users/e107580/Desktop/CODE/TIMY/"
path = pathLog + "/fotos/"
logging.basicConfig(filename=str(pathLog)+'REGISTRO-FICHAJE.log', encoding='utf-8', level=logging.DEBUG)


print("FICHAJE ESPAÑA -> DIA:" + str(diaDeLaSemana) + " -> " + str(hora) )
logging.info("FICHAJE ESPAÑA -> DIA:" + str(diaDeLaSemana) + " -> " + str(hora) )


if diaDeLaSemana != 6 and diaDeLaSemana != 7:
    if diaDeLaSemana == 5 and (hora > 12 or hora < 14):
        print("VIERNES AL MEDIODIA")
        logging.info("VIERNES AL MEDIODIA")
    else:
        # LOGICA DE LA APLICACION:

        # 1 - DESKTOP CLEAN:
        time.sleep(2)
        auto.hotkey('winleft','d')
        time.sleep(3)

        # 2 - OPEN MY TIME:
        poneteEn(path + "my-time-link-2.png", False , True, True)
        time.sleep(6)

        # 3 - LOGIN MY TIME:
        poneteEn(path + "boton-login.png", True, False, False)
        time.sleep(5)

        # 5 - BOTON ENTRADA O SALIDA SEGUN PARAMETRO EXTERNO:
        if listaContiene(arrParameters, "MORNING"):
            print("DEBO FICHAR PARA MORNING")
            logging.debug("DEBO FICHAR PARA MORNING")

            # 4 - BOTON OFICINA:
            poneteEn(path + "boton-oficina.png", True, False, False)
            time.sleep(3)

            poneteEn(path + "boton-entrada.png", True, False, False)
        else:

            print("DEBO FICHAR PARA AFTERNOON")
            logging.debug("DEBO FICHAR PARA AFTERNOON")
            poneteEn(path + "boton-salida.png", True, False, False)

        time.sleep(10)

        # 6 - CERRAR IE:
        auto.click(1887, 20)
        time.sleep(3)


