import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import random ; 
import csv 
from tkinter import *
from tkinter import ttk


# O que colocar : 
# barras de imc medio por iidade
# treinar graficos diferentes 
# aperfeiçoar os graficos ja existentes
# entrega até a terça 



dataImc = []
dataAge = []
sobrepeso = []
obeso = []
jovenssobrepeso = []
with open ('logDados.csv' ) as File : 
    line_reader = csv.reader(File, delimiter=';')
    
    for i in line_reader : 
        dataAge.append(int((i[0])))
        dataImc.append(float((i[1])))
        dataSex.append((i[2]))

    

for i in dataImc : 
    if (i > 25 and i <= 29) : 
        sobrepeso.append(i)
    if (i >29 ) : 
        obeso.append(i)    

print(len(sobrepeso))
np.random.seed(19680801)

def scattermap() : 
    fig, ax = plt.subplots( )

    sizes = np.random.uniform(15, 80, len(dataImc))
    colors = np.random.uniform(-20, 20, len(dataImc))

    ax.scatter(dataImc, dataAge, s=sizes, c=colors, vmin=0, vmax=100)

    ax.set_xlabel('Imc') 
    ax.set_ylabel('Idade')
    plt.show() ; 

def pixelmap() : 

    # plot
    fig, ax = plt.subplots()
    ax.set_title("IMC POR IDADE ")
    ax.hist2d(dataImc, dataAge,  bins=10)
    ax.set_xlabel("Imc")
    ax.set_ylabel("Idade")
    plt.show()

def barmap(): 
    fig, ax = plt.subplots()
    ax.hist(dataImc,bins=10, linewidth=0.5,width=1,edgecolor='black')
    plt.show()


def map3d():
    neoImc = [ ]
    neoAge = [ ]

    for i in range (0,25) : 
        neoImc.append( dataImc [ i ] )
        neoAge.append( dataAge [ i ]) 
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    # Make data.
    X = neoImc
    Y = dataAge
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)


    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)
    ax.set_zlim(-2, 1)
    ax.zaxis.set_major_locator(LinearLocator(10))
    # A StrMethodFormatter is used automatically

    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

def linearmap() : 
    fig, ax = plt.subplots()
    ax.plot(dataImc,dataAge)
    plt.show()

def piemap() : 
    fig, ax = plt.subplots()
    labels = ["Sobrepeso", "Obeso","Peso Normal"]
    sobrepeso_percent = (len(sobrepeso)*100)/len(dataImc)
    obeso_percent = (len(obeso)*100)/len(dataImc)
    tamanhos = [sobrepeso_percent, obeso_percent ,  100-sobrepeso_percent]
    ax.pie(tamanhos, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

#tk para UI/UX 
window = Tk()
window.title("Gráficos")
window.geometry('500x300')
window.configure(background = "#7a9aeb")

buttom = ttk.Button(window, text="Scatter ", command= scattermap).grid(row=1,column=0)
buttom2 = ttk.Button(window, text="Pixel", command=pixelmap).grid(row=1,column=1)
buttom3 = ttk.Button(window, text="Barra", command=barmap).grid(row=1,column=2)
buttom4 = ttk.Button(window, text="PROIBIDO", command=linearmap).grid(row=2,column=0)
buttom5 = ttk.Button(window, text="TRAVA 3080", command=map3d).grid(row=2,column=1)
buttom6 = ttk.Button(window, text="Pizza", command=piemap).grid(row=1,column=3)
window.mainloop()