# funciones en python
# def name_function(params):
# codigo
# return

# funcion sin parametros y sin retorna
def saludos():
    print("hola a todos!")

saludos()   

# funciones con un  parametro
def get_age_in_future(age):
    print(f"en 3 años tendras {age + 3} años")


get_age_in_future(18)

# funciones con  dos parametros sin  retorno
def suma(num1, num2):
    print(F"{num1}+{num2}= {num1 + num2}")

suma(12, 35) 
# funciones con parametros opcionales   

def get_heroes( h1 = "ironman", h2 = "spiderman"):
    print([h1, h2])

    get_heroes()
    get_heroes("batman")
    get_heroes("batman", "superman")
    get_heroes( h2="batman", h1="superman")

# funciones con retorno
def title(texto):
    return texto.title()

text_changed = title("hOlA a TodOs")
print(text_changed)
    
