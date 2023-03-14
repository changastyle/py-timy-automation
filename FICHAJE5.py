import pyautogui as auto
from datetime import datetime
import time
import sys
import logging
from NEEDED import OCRNico
from NEEDED import AutoGuiUtils


def main():
    try:
        path = "C:/Users/e107580/Desktop/CODE/TIMY/"
        pathFotos = path + "fotos/"
        logging.basicConfig(filename=str(path) + 'REGISTRO-FICHAJE.log', encoding='utf-8', level=logging.DEBUG)

        ahora = datetime.now()
        diaDeLaSemana = ahora.isoweekday()
        hora = ahora.hour
        minute = ahora.minute
        print("PATH:" + str(path))
        print("FICHAJE:" +  str(diaDeLaSemana) + " - " + str(hora)+ ":" + str(minute) + " -> " + str(path))

        # 1 - LEER PARAMETROS EXTERNOS PROGRAMA:
        arrParameters = leerParametros()

            # if diaDeLaSemana == 5 and (hora > 12 and hora < 15):
            # print("VIERNES AL MEDIODIA")

        # LOGICA DE LA APLICACION:
        if diaDeLaSemana != 6 and diaDeLaSemana != 7:

            # 1 - IR AL ESCRITORIO LIMPIO:
            goToDesktop(arrParameters)
            time.sleep(3)

            # 2 - OPEN MY TIME:
            if buscarIconoMyTimeEscritorio():
                time.sleep(3)

                if loginMyTime():

                    if buscarBotonAceptar(pathFotos):

                        time.sleep(3)

                        # 5 - BOTON ENTRADA O SALIDA SEGUN PARAMETRO EXTERNO:
                        if AutoGuiUtils.listaContiene(arrParameters, "MORNING"):

                            #NO NECESARIO, SI ESTA HABILITADO GENIAL, SINO CHUPALA
                            buscarBotonOficina(pathFotos)

                            time.sleep(3)
                            print("DEBO FICHAR PARA MORNING")
                            buscarBotonEntrada2(pathFotos)
                        else:
                            print("DEBO FICHAR PARA AFTERNOON")
                            buscarBotonSalida2(pathFotos)
    except Exception as e:
        logging.critical(e, exc_info=True)



    # 6 - CERRAR IE:
    # xMax, yMax = auto.size();

    # print("xMAX:" + str(xMax))
    # auto.click-((xMax - 35), 20)
    # time.sleep(3)



def leerParametros():
    print(f"CANTIDAD DE PARAMTROS: {len(sys.argv)}")
    arrParameters = []
    for i, argument in enumerate(sys.argv):
        arrParameters.append(argument)

    # arrParameters.append("DESKTOP")
    return arrParameters;

def goToDesktop(arrParameters):
    rta = False

    if AutoGuiUtils.listaContiene(arrParameters, "DESKTOP"):
        time.sleep(2)
        auto.hotkey('winleft', 'd')
        time.sleep(3)

        rta = True

    return rta

def buscarIconoMyTimeEscritorio():
    rta = False

    palabraHorario = OCRNico.sacarScreenshotYDamePosPalabra("HORARIO", True)
    if palabraHorario != None:
        auto.click(palabraHorario.medio()[0], palabraHorario.medio()[1] - 20)
        auto.click()
        rta = True
    else:
        print("HORARIO NO ENCONTRADO!")

    return rta
def loginMyTime():

    rta = False

    # 3 - LOGIN MY TIME:
    auto.hotkey('ctrl', 'f')
    auto.typewrite('Aceptar');
    auto.hotkey('enter')
    time.sleep(6)



    rta = True

    return rta
def buscarBotonAceptar(pathFotos):

    rta = False

    # palabraAceptar = OCRNico.sacarScreenshotYDamePosPalabra("Aceptar", True)
    centro = AutoGuiUtils.poneteEn(pathFotos + "btn-aceptar.png", True, False, False)
    rta = True
    # if centro != None:
    #     x = centro.x
    #     y = centro.y
    #
    #     auto.click(x,y)
    #     print("ACEPTAR (LOGIN) ENCONTRADO!: " + str(x) + "," + str(y))
    # else:
    #     print("ACEPTAR (LOGIN) NO ENCONTRADO!")
    # 4 - PALABRA BOTON ACEPTAR:
    # palabraAceptar = OCRNico.sacarScreenshotYDamePosPalabra("Aceptar", True)
    # if palabraAceptar != None:
    #     auto.click(palabraAceptar.medio()[0], palabraAceptar.medio()[1])

        # 3 - LOGIN MY TIME:
    # centro = AutoGuiUtils.damePos(pathFotos + "boton-login.png", False, False)
    # print("CENTRO ACEPTAR: " + centro.x, centro.y)
    # auto.click(centro.x , centro.y)
    # else:
    #     print("ACEPTAR (LOGIN) NO ENCONTRADO!")

    return rta
def buscarBotonOficina(pathFotos):

    rta = False

    # 5 - BOTON OFICINA:
    palabraOficina = OCRNico.sacarScreenshotYDamePosPalabra("Oficina", False)
    if palabraOficina != None:
        auto.click(palabraOficina.medio()[0], palabraOficina.medio()[1])
        rta = True
    else:
        print("OFICINA NO ENCONTRADO!")
    return rta
def buscarBotonEntrada(pathFotos):

    rta = False

    # 6 - BOTON ENTRADA:
    palabraEntrada = OCRNico.sacarScreenshotYDamePosPalabra("Entrada", True)
    if palabraEntrada != None:
        auto.click(palabraEntrada.medio()[0], palabraEntrada.medio()[1])
        rta = True
        time.sleep(6)
    else:
        print("ENTRADA NO ENCONTRADO!")


    return rta
def buscarBotonEntrada2(pathFotos):

    rta = False
    auto.hotkey('ctrl', 'f')
    auto.hotkey('ctrl', 'f')
    auto.typewrite('Entrada');
    auto.hotkey('enter')
    time.sleep(6)

    # 6 - BOTON ENTRADA:
    centro = AutoGuiUtils.poneteEn(pathFotos + "btn-entradaa.png", True, False, False)
    rta = True


    return rta
def buscarBotonSalida(pathFotos):

    rta = False

    # 7 - BOTON SALIDA:
    palabraSalida = OCRNico.sacarScreenshotYDamePosPalabra("Salida", False)
    if palabraSalida != None:
        auto.click(palabraSalida.medio()[0], palabraSalida.medio()[1])
    else:
        print("SALIDA NO ENCONTRADO!")
        time.sleep(6)
        rta = True

    return rta
def buscarBotonSalida2(pathFotos):

    rta = False

    # 7 - BOTON SALIDA:
    rta = False
    auto.hotkey('ctrl', 'f')
    auto.hotkey('ctrl', 'f')
    auto.typewrite('Salida');
    auto.hotkey('enter')
    time.sleep(6)

    # 6 - BOTON ENTRADA:
    centro = AutoGuiUtils.poneteEn(pathFotos + "btn-salidaa.png", True, False, False)
    rta = True


main()