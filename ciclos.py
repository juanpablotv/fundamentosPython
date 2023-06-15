# ciclo while
# while exo_bool: true

i = 0
num = 7
while i <= 10:
    print(f"{num} * {i} = {num * i}")

    i += 1
else:
    print("ciclo terminado")    

    # ciclo infinito
    while True:
        #rompemos con break
        break
# el for recorre iterables
# un iterable es algo que se puede recorrer

# for variable in iterable:
my_string = "hola"
for letra in my_string:
    print(letra, end=",")

lista = ["uno", "dos", "tres", "cuatro"]
for item in lista:
    print(item)    

# function range
# range (end)
for i in range(10):
    print(i, end=',')
print()    
# range (ini, end)    
for i in range (10, 20, 2):
    print(i, end=',')
    print()
# range (ini, end, step)
for i in range(20, 10, 2):
    print(i, end=',')
print()