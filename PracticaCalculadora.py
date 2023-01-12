import os

def menu():
    
        os.system('clear')
        print('--- Mi Calculadora ---')
        print('1.- Suma')
        print('2.- Resta')
        print('3.- Multiplicación')
        print('4.- División')
        print('5.- Salir')

while True:

    menu()
    
    opciones_menu = input('Ingresa una operación: ')
    
    if opciones_menu=='1':
        print('')
        input('Seleccionaste la suma')
    elif opciones_menu=='2':
        print('')
        input('Seleccionaste la resta')
    elif opciones_menu=='3':
        print('')
        input('Seleccionaste la multiplicación')
    elif opciones_menu=='4':
        print('')
        input('Seleccionaste la división')
    elif opciones_menu=='5':
        break
    else:
        print('')
        input('No has pulsado ninguna opción correcta...\npulsa una tecla para continuar')



