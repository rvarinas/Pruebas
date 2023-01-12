import os

def menu():
    
        os.system('clear')
        print('--- Mi Calculadora ---')
        print('1.- Suma')
        print('2.- Resta')
        print('3.- Multiplicación')
        print('4.- División')
        print('5.- Raiz n')
        print('6.- Exponente n')
        print('7.- Seno')
        print('8.- Salir')

while True:

    menu()
    
    opciones_menu = input('Ingresa una operación: ')
    
    if opciones_menu=='1':
        print('')
        print('Seleccionaste la suma')
        num1=int(input('Ingresa el primer valor: '))
        num2=int(input('Ingresa el segundo valor: '))
        res=0
        res=num1+num2
        print('El resultado es: ',res)
        print('')
        input('Enter para regresar al menu')
        
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
        print('')
        print('Seleccionaste la raiz')
        input('Ingresa el número base: ')

    elif opciones_menu=='8':
        break
    else:
        print('')
        input('No has pulsado ninguna opción correcta...\npulsa una tecla para continuar')



