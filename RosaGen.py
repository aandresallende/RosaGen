#!/usr/bin/python3
#-*-coding: utf-8-*-

"""Programa escrito por Andrés Allende
desde San Francisco de Campeche Campeche, sureste de México EK49ru"""

try:
	import platform
	import os
	import time
	import random
	import string
	import sys
except ImportError as ErrorDeImportacion:
	print("Se ha producido un error al importar los módulos requeridos para que el software funcione, por favor, revise las dependencias y resuelva las dependencias")

def numeros_aleatorios(elementos):
	return [random.randint(0, 255) for i in range(elementos)]

def no_imprimibles(elementos):
	no_print_char = list(range(0, 32)) + [127]
	return [random.choice(no_print_char) for i in range(elementos)]

def sistema_hexadecimal(datos):
	return [format(byte, '02x') for byte in datos]

def main():
	try:
		if platform.system() == 'Windows':
			print("RosaGen, software de generación de números y caracteres aleatorios\n")
			print("Genera datos aleatorios para usarlos en contraseñas seguras\n")
			time.sleep(5)
			os.system("cls")
			print("Este software es gratuito y Open Source (OSS), es por eso que se entrega \n TAL CUAL, SIN GARANTÍA ALGUNA \t continúa a los 5 segundos")
			time.sleep(5)
			os.system("cls")
			print("Se agradecen los donativos voluntarios que ayudan a mantener activo el proyecto")
			print("Si desea hacer un donativo, por favor, ponerse en contacto con el desarrollador a los números: \n +522712445269 y +529811034720\n o al correo: andresallende792@gmail.com\t Muchas gracias")
			time.sleep(5)
			os.system("cls")
		else:
			print("RosaGen, software de generación de números y caracteres aleatorios\n")
			print("Genera datos aleatorios para usarlos en contraseñas seguras\n")
			time.sleep(5)
			os.system("clear")
			print("Este software es gratuito y Open Source (OSS), es por eso que se entrega \n TAL CUAL, SIN GARANTÍA ALGUNA \t continúa a los 5 segundos")
			time.sleep(5)
			os.system("clear")
			print("Se agradecen los donativos voluntarios que ayudan a mantener activo el proyecto")
			print("Si desea hacer un donativo, por favor, ponerse en contacto con el desarrollador a los teléfonos: \n +522712445269 y +529811034720\n o al correo: andresallende792@gmail.com\t Muchas gracias")
			time.sleep(5)
			os.system("clear")
	except Exception as err1:
		print("Se ha producido el error: " + str(err1))
	try:
		elementos = int(input("Escriba por favor el número de caracteres a generar: "))
		tipo = input("¿Quieres generar números aleatorios (NUM) o caracteres aleatorios (CHAR)?: ")
		
		if tipo == 'NUM':
			datosAleatorios = numeros_aleatorios(elementos)
		elif tipo == 'CHAR':
			datosAleatorios = no_imprimibles(elementos)
		else:
			print("No existe la opcióin: " + tipo)
		
		hexadecimal_1 = sistema_hexadecimal(datosAleatorios)
		cadena = " ".join(hexadecimal_1)
		print("Datos Generados con salida hexadecimal: "  + cadena)
		print("\n\nPresione {ENTER} para salir")
		input()
		sys.exit()
	except Exception as err0:
		print("Los datos introducidos han producido in fallo grave del software, por favor, ingrese los datos correctos")
		sys.exit()
if __name__  == '__main__':
	main()
