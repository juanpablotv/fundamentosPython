# funtion input -> retorna string

num_a = int(input("ingresa un numero: "))
num_b = int(input("ingresa un numero: "))

print(num_a + num_b)

name = input("ingresa tu nombre: ")
age = int(input("ingresa tu edad: "))
city = input("ingresa tu ciudad/pueblo: ")


#string format
"""
hola, soy juan pablo, tengo 18 años y vivo en zitlaltepec
"""
greeting = "hola, soy {}, tengo {} años y vivo en {}"

print(greeting.format(name, age, city))

greeting_2 = f"hola soy { name }, tengo { age } años y vivo en { city }"
print(greeting_2)

