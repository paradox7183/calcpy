#enconding: utf-8
#Autor:  GrayFox
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
#Input para poder expresar la funcion 
dx = parse_expr(input(Fore.GREEN + Style.BRIGHT +"Introduce la funcion>" + Style.RESET_ALL))
#Empezando a derivar e integrar 
yprime = dx.diff(x)
sndv = dx.diff(x,x)
thdv = dx.diff(x,x,x)
yintegrate = integrate (dx) 
#Mostrando el resultado de la primera, segunda, tercera derivada y de la integral
print(Fore.RED + Style.BRIGHT + "Derivada: " +Style.RESET_ALL)
print(yprime)
print (Fore.YELLOW + Style.BRIGHT +"Segunda Derivada de la funcion:")
print (sndv)
print (Fore.CYAN + Style.BRIGHT +"Tercera derivada de la funcion:")
print (thdv)
print (Fore.GREEN + Style.BRIGHT + "Integral: ")
print (yintegrate)
