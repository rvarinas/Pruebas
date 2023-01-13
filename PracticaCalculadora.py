import os
import math
import numpy as np

def Sumatoria(num1,num2):
    return num1+num2

def Resta(num1,num2):
    return num1-num2

def Multiplicacion(num1,num2):
    return num1*num2

def Division(num1,num2):
    return num1/num2

def Raiz(num1):
    return np.sqrt(num1)

def menu():
    
        os.system('clear')
        print('--- Mi Calculadora ---')
        print('1 ----> Suma')
        print('2 ----> Resta')
        print('3 ----> Multiplicación')
        print('4 ----> División')
        print('5 ----> Raiz')
        print('6 ----> Exponente n')
        print('7 ----> Seno')
        print('8 ----> Salir')
        print('')

while True:

    menu()
        
    opciones_menu = input('Ingresa una operación: ')


    if opciones_menu=='1':
        print('')
        print('Seleccionaste la suma')
        print('')
        num1=float(input('Ingresa el valor: '))
        num2=float(input('Ingresa el segundo valor: '))
        print('')
        print('El resultado de',num1,'+',num2,'=',Sumatoria(num1,num2))
        print('')    
        input('Enter para regresar al menu')
        
    elif opciones_menu=='2':
        print('')
        print('Seleccionaste la resta')
        print('')
        num1=float(input('Ingresa el primer valor: '))
        num2=float(input('Ingresa el segundo valor: '))
        print('')
        print('El resultado de',num1,'-',num2, '=',Resta(num1,num2))
        print('')
        input('Enter para regresar al menu')

    elif opciones_menu=='3':
        print('')
        print('Seleccionaste la multiplicación')
        print('')
        num1=float(input('Ingresa el primer valor: '))
        num2=float(input('Ingresa el segundo valor: '))
        print('')
        print('El resultado de',num1,'*',num2,'=',Multiplicacion(num1,num2))
        print('')
        input('Enter para regresar al menu')

    elif opciones_menu=='4':
        print('')
        print('Seleccionaste la división')
        print('')
        num1=float(input('Ingresa el primer valor: '))
        num2=float(input('Ingresa el seundo valor: '))
        print('El resultado de',num1,'/',num2,'=',Division(num1,num2))
        print('')
        input('Enter para regresar al menu')
    elif opciones_menu=='5':
        print('')
        print('Seleccionaste la raiz')
        print('')
        num1=int(input('Ingresa el valor: '))
        print('El resultado de la raiz de',num1,'=',Raiz(num1))
        print('')
        input('Enter para regresar al menu')

    elif opciones_menu=='8':
        break
    else:
        print('')
        input('No has pulsado ninguna opción correcta...\npulsa una tecla para continuar')



