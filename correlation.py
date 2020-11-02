import csv
from matplotlib import pyplot as plt
import numpy as np

filename = 'pulso.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    #Obteniendo valores  de la primera grafica 
    volts1,volts2,times = [], [],[]

    for row in reader:
        if row[1] == '':
            continue
        
        time1 = float(row[0])
        times.append(time1)

        volt1 = float(row[1])
        volts1.append(volt1)

        volt2 = float(row[2])
        volts2.append(volt2)
        
        tiempo = np.array(times)
        
        voltaje1 = np.array(volts1)

        voltaje2 = np.array(volts2)

    result = []

    for i in range((len(volts1)+len(volts2)) - 2 ):
        sample = 0
        for j in range((len(volts2)-1),-1,-1):
            if i - j < 0:
                continue
            if i - j > (len(volts1) - 1 ):
                continue
            sample += volts2[j] * volts1[i-j]
        result.insert(i,sample)

    #Graficando informacion
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(list(range((len(volts1)+len(volts2)) - 2 )),result, c= 'red')

    #Formateando la grafica
    plt.title("Correlation", fontsize=20)
    plt.xlabel('Samples',fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Value", fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)

    plt.show()

    
    


   
