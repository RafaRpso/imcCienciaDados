import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import random ; 
import csv 



# O que colocar : 
# barras de imc medio por iidade
# treinar graficos diferentes 
# aperfeiçoar os graficos ja existentes
# entrega até a terça 

dataImc = []
dataAge = []
dataSex = []
qtdIdososObesos = 0
qtdCriancasObesas = 0 
qtdObesos = 0 
mediaImc = 0 ; 
mediaIdade =0 ; 

with open ('logDados.csv' ) as File : 
    line_reader = csv.reader(File, delimiter=';')
    
    for i in line_reader : 
        dataAge.append(int((i[0])))
        dataImc.append(float((i[1])))
        dataSex.append((i[2]))

    for i in range(0,len(dataImc)) : 
        if (float(dataImc[i]) >  30 ) : 
            qtdObesos+=1 
        if ( int(dataAge[i]) > 50 and float(dataImc[i]) > 30) : 
            qtdIdososObesos+=1 
        elif (int(dataAge[i]) < 14 and float(dataImc[i] > 30 )) : 
            qtdCriancasObesas+=1  

for i in dataImc : 
    mediaImc += i ; 
mediaImc = mediaImc/len(dataImc) 

for i in dataAge : 
    mediaIdade += i ; 

print(qtdObesos)
print (qtdIdososObesos)
print(qtdCriancasObesas)



mediaImc = mediaImc/len(dataImc) 
mediaIdade = mediaIdade/len(dataAge)
np.random.seed(19680801)

def scattermap() : 
    fig, ax = plt.subplots( )

    sizes = np.random.uniform(15, 8, len(dataImc))
    colors = np.random.uniform(15, 80, len(dataImc))

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

def barmap(x): 
    fig, ax = plt.subplots()
    ax.hist(x,bins=10, linewidth=0.5,width=15,edgecolor='black')
 

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

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)

    # Customize the z axis.
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    # A StrMethodFormatter is used automatically
    ax.zaxis.set_major_formatter('{x:.02f}')

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

barmap(dataAge,dataImc)