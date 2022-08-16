from math import * ; 
import random ; 

file = open("logDados.csv", "a" )
num = 0 ; 
for i in range ( 0, 10000 ) : 
    
    randomGenero = random.randint(0,1) 
    randomPopulacao = random.randint(0,100)
    randomIdade = random.randint(0,100)
    print(randomPopulacao)
    #parametrizacao imc 
    if (randomPopulacao>=0 and randomPopulacao<=73  ) : 
        imc  = random.uniform(18.5,24.9)
    elif (randomPopulacao>73 and randomPopulacao<=88) : 
        imc = random.uniform(16.5,18.8)
    elif  (randomPopulacao >88 and randomPopulacao<= 99.8) : 
        imc = random.uniform(25.0, 29.9) 
    else : 
        imc = random.uniform(30.9, 35.0)

    #parametrizacaoIdade (https://educa.ibge.gov.br/jovens/conheca-o-brasil/populacao/18318-piramide-etaria.html#:~:text=A%20popula%C3%A7%C3%A3o%20acima%20de%2030,anos%2C%204%2C9%25.)
    if (randomIdade>=0 and randomIdade <=20) :
        idade = random.randint(12,17)
    elif(randomIdade>20 and randomIdade<=50) :
        idade = random.randint(18,28)
    elif (randomIdade >50 and randomIdade<=70) : 
        idade = random.randint(26,39)
    elif (randomIdade > 70 and randomIdade<=85) : 
        idade = random.randint(40,49)
    elif(randomIdade > 85 and randomIdade<= 93) : 
        idade = random.randint(50,59)
    elif(randomIdade > 93 and randomIdade<= 97 ) : 
        idade = random.randint(60,64)
    else : 
        idade = random.randint(65,80)
    
    
    file.write( str(idade)+";"+str( round(imc,2)) + "\n")
file.close()