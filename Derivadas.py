#enconding: utf-8
#Autor:  Garrido Conde Jordan 
#/usr/bin/env/python3.1
#Importacion de librerias para estilo 	
import colorama
from colorama import Fore
from colorama import Style
#Importacion de librerias para algebra y calculo
import sympy as sym
from sympy import *
from sympy import symbols, Eq, solve, sqrt
#Definicion de simbolos algebraicos 
x, y, z, a, b, c, d, t = sym.symbols('x y z a b c d t')
#Derivada de una funcion 
dx = parse_expr(input(Fore.GREEN + Style.BRIGHT +"Introduce la funcion>" + Style.RESET_ALL))
print(Fore.YELLOW + Style.BRIGHT + "Calculando la derivada..." + Style.RESET_ALL )
print (".")
print (".")
yprime = dx.diff(x)
dxderivate = Derivative(dx,x,a,b).doit()
yintegrate = integrate (dx) 
#Mostrando el resultado de la derivada 
print(Fore.RED + Style.BRIGHT + "Derivada: " +Style.RESET_ALL)
print(yprime)
print (Fore.GREEN + Style.BRIGHT + "Integración: ")
print (yintegrate)
print (Fore.BLUE + Style.BRIGHT+ "Resultado en base a todas las variables:")
simplify(dxderivate)
print (dxderivate) 