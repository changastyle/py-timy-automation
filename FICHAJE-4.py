import pyautogui as auto
from datetime import datetime
import time
import sys

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

ahora = datetime.now()
diaDeLaSemana = ahora.isoweekday()
hora = ahora.hour;
print("FICHAJE ESPAÑA -> DIA:" + str(diaDeLaSemana) + " -> " + str(hora) )

if diaDeLaSemana != 6 and diaDeLaSemana != 7:
    if diaDeLaSemana == 5 and (hora > 12 or hora < 14):
        print("VIERNES AL MEDIODIA")
    else:
        # LOGICA DE LA APLICACION:
        path ="C:/Users/e107580/Desktop/CODE/TIMY/fotos/"

        # 1 - DESKTOP CLEAN:
        time.sleep(2)
        auto.hotkey('winleft','d')
        time.sleep(3)




        # 2 - OPEN MY TIME:
        poneteEn(path + "my-time-link-2.jpg", False , True)
        time.sleep(6)

        # 3 - LOGIN MY TIME:
        poneteEn(path + "boton-login.png", True, False)
        time.sleep(5)

        # 4 - BOTON OFICINA:
        poneteEn(path + "boton-oficina.png", True, False)
        time.sleep(3)

        # 5 - BOTON ENTRADA O SALIDA SEGUN PARAMETRO EXTERNO:
        if listaContiene(arrParameters, "MORNING"):
            print("DEBO FICHAR PARA MORNING")
            poneteEn(path + "boton-entrada.png", True, False)
        else:
            print("DEBO FICHAR PARA AFTERNOON")
            poneteEn(path + "boton-salida2.png", True, False)
        time.sleep(10)

        # 6 - CERRAR IE:
        auto.click(1887, 20)
        time.sleep(3)


