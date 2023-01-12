import random as rand
import datetime as dt
import time
random = int(rand.random() * 6)

ahora = dt.datetime.now();
print( str(ahora.hour) +":" + str(ahora.minute) + ":" +  str(ahora.second)  + " -> WAITING: " + str(random) + " MINUTES")

time.sleep( random * 60)

fin = dt.datetime.now();
print("TERMINE DE ESPERAR - PROCEDO: " + str(fin.hour) + ":" + str(fin.minute))