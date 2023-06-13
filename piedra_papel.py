# elección aleatoria de la maquina
import random

# funtion randint(min,max)
rand_int = random.randint(1,3)
if rand_int==1:
    choise_maq = 'piedra'
elif rand_int == 2:
    choise_maq = 'papel'
else:
    choise_maq ='tijeras'        
# elecció|n de usuario
choise_text = '''
escribe una de las opciones:
piedra
papel
tijeras
'''
choise_user = input(choise_text)
# impresión de opciones
print('usuario eligio ->', choise_user)
print('maquina eligio ->', choise_maq)

# ganador!
if choise_maq == choise_user:
    print("es un empate")
else:
    if choise_maq == 'piedra' and choise_user == 'papel':
        print("gana usuario!")
    elif choise_maq == 'piedra' and choise_user == 'tijeras':
        print('gana maquina')  
    elif choise_maq == 'papel' and choise_user == 'tijeras':
        print("gana usuario")  
    elif choise_maq == 'papel' and choise_user == 'piedra':
        print('gana maquina') 
    elif choise_maq == 'tijeras' and choise_user == 'piedra':
        print('gana usuario!')
    else:
        print('gana maquina')             
           
