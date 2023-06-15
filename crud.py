drinks = []

def add_drink(drink):
    drinks.append(drink)

def del_drink(drink):
    drinks.remove(drink)
    try:
        drinks.remove(drink)
    except Exception:
        print("no existe en la lista")    

def show_drinks():
    print("-" * 4, "my drinks", "-" * 4)
    for drink in drinks:
        print("-->", drink)    

chise_text = """
elige una opcion:
1 - agregar
2 - eliminar
3 - mostrar
4 - salir
"""   
while  True:
    choise_user = int(input(chise_text))
    if choise_user == 1:
        drink = input('ingresa una bebida: ')
        add_drink(drink)
    elif choise_user == 2:
        drink = input('ingresa una bebida: ')
        del_drink(drink)
    elif choise_user == 3:
        show_drinks()
    elif choise_user == 4:
        break
    else:
        print('opción incorrecta')
