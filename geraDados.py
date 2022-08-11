from math import * ; 
import random ; 

file = open("logDados.txt", "a" )

num = 0 ; 
for i in range ( 0, 10000 ) : 
    imc = random.uniform(18.5,30)
    idade = random.randint(8,80)
    file.write( str(idade)+";"+str( round(imc,2)) + "\n")
file.close()