from tkinter import *
from tkinter import ttk
from math import *  
import pymysql

conectar = pymysql.connect(db='tbSistemaImc',user='root',passwd='akemih32')
modal =  conectar.cursor()

window = Tk()
window.title("IMC PROGRAMA")
window.geometry('500x300')
window.configure(background = "#7a9aeb")
form1 = Label(window, text = "Insira aqui a sua altura ").grid(row=0, column=0)
form2 = Label(window, text = "Insira aqui o seu peso ").grid(row=1, column=0)

altura = StringVar() 
peso = StringVar()

res_form = Entry(window, textvariable=altura).grid(row= 0 , column = 1 )
res_form2 = Entry(window,textvariable=peso).grid(row= 1 , column = 1 )

def userClick() : 
    alt = float ( altura.get() )  ; 
    pes = float ( peso.get() )  ; 
    imc = round ( pes / alt**2, 2 )  

    modal.execute("INSERT INTO tbImc (alturaUsuario,pesoUsuario,imcUsuario) VALUES ('"+str(alt)+"', '"+str(pes)+"','"+str(imc)+"')")
    conectar.commit()
    conectar.close()
    window = Tk()
    window.title("IMC PROGRAMA")
    window.geometry('300x200')
    window.configure(background = "#7a9aeb")
    form1 = Label(window, text = "SEU IMC É  " + str(imc) ).grid(row=1, column=0)
    
    if (imc < 18 ) : 
        form2 = Label(window, text = "Você está extremamente magro.  " ).grid(row=2, column=0)
    elif (imc >18 and imc <25) :
        form2 = Label(window, text = "Sua condição é a ideal :)" ).grid(row=2, column=0)
    elif (imc >25 and imc < 30) :
        form2 = Label(window, text = "Você está com sobrepeso, fique atento" ).grid(row=2, column=0)
    else : 
        form2 = Label(window, text = "Você está obeso, procure um médico" ).grid(row=2, column=0)
buttom = ttk.Button(window, text="Enviar IMC ", command= userClick).grid(row=3,column=0)



window.mainloop()




