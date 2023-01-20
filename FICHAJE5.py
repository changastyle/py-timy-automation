import pyautogui as auto
from datetime import datetime
import time
import sys
import logging
from NEEDED import OCRNico
from NEEDED import AutoGuiUtils


print(f"CANTIDAD DE PARAMTROS: {len(sys.argv)}")
arrParameters = []
for i, argument in enumerate(sys.argv):
    arrParameters.append(argument)


try:
    ahora = datetime.now()
    diaDeLaSemana = ahora.isoweekday()
    hora = ahora.hour
    minute = ahora.minute

    path = "C:/Users/e107580/Desktop/CODE/TIMY/"
    pathFotos = path + "fotos/"
    print("PATH:" + str(path))
    logging.basicConfig(filename=str(path)+'REGISTRO-FICHAJE.log', encoding='utf-8', level=logging.DEBUG)

    print("FICHAJE ESPAÑA -> DIA:" + str(diaDeLaSemana) + " -> " + str(hora) + ":" + str(minute))
    logging.info("FICHAJE ESPAÑA -> DIA:" + str(diaDeLaSemana) + " -> " + str(hora)+ ":" + str(minute) )


    if diaDeLaSemana != 6 and diaDeLaSemana != 7:
        if diaDeLaSemana == 5 and (hora > 12 and hora < 15):
            print("VIERNES AL MEDIODIA")
            logging.info("VIERNES AL MEDIODIA")
        else:
            # LOGICA DE LA APLICACION:

            # 1 - DESKTOP CLEAN:
            if AutoGuiUtils.listaContiene(arrParameters, "DESKTOP"):
                time.sleep(2)
                auto.hotkey('winleft','d')
                time.sleep(3)

            # 2 - OPEN MY TIME:
            palabraHorario = OCRNico.sacarScreenshotYDamePosPalabra("HORARIO", True)
            if palabraHorario != None:
                auto.click(palabraHorario.medio()[0], palabraHorario.medio()[1]-20)
                auto.click()
            else:
                print("HORARIO NO ENCONTRADO!")
            time.sleep(6)

            # 3 - LOGIN MY TIME:
            # palabraAceptar = OCRNico.sacarScreenshotYDamePosPalabra("Aceptar", True)
            # if palabraAceptar != None:
            #     auto.click(palabraAceptar.medio()[0], palabraAceptar.medio()[1])
            # else:
            #     print("ACEPTAR (LOGIN) NO ENCONTRADO!")
            # time.sleep(6)
            # 3 - LOGIN MY TIME:
            AutoGuiUtils.poneteEn(pathFotos + "boton-login.png", True, False, False)
            time.sleep(5)


            # 3 - BOTON OFICINA:
            palabraOficina = OCRNico.sacarScreenshotYDamePosPalabra("Oficina", False)
            if palabraOficina != None:
                auto.click(palabraOficina.medio()[0], palabraOficina.medio()[1])
            else:
                print("OFICINA NO ENCONTRADO!")
            time.sleep(6)

            # 5 - BOTON ENTRADA O SALIDA SEGUN PARAMETRO EXTERNO:
            if AutoGuiUtils.listaContiene(arrParameters, "MORNING"):
                print("DEBO FICHAR PARA MORNING")
                logging.debug("DEBO FICHAR PARA MORNING")

                # 3 - BOTON ENTRADA:
                palabraEntrada = OCRNico.sacarScreenshotYDamePosPalabra("Entrada", False)
                if palabraEntrada != None:
                    auto.click(palabraEntrada.medio()[0], palabraEntrada.medio()[1])
                else:
                    print("ENTRADA NO ENCONTRADO!")
                time.sleep(6)

            else:

                print("DEBO FICHAR PARA AFTERNOON")
                logging.debug("DEBO FICHAR PARA AFTERNOON")

                # 3 - BOTON SALIDA:
                palabraSalida = OCRNico.sacarScreenshotYDamePosPalabra("Salida", False)
                if palabraSalida != None:
                    auto.click(palabraSalida.medio()[0], palabraSalida.medio()[1])
                else:
                    print("SALIDA NO ENCONTRADO!")
                time.sleep(6)

            time.sleep(10)

    # 6 - CERRAR IE:
    auto.click(1887, 20)
    time.sleep(3)

except Exception as e:
    logging.critical(e, exc_info=True)
