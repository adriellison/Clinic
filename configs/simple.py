import os
import time

def cls():
	os.system('cls')

def carregar():
	lista = [
	'▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒0%',
	'█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒5%',
	'██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒10%',
	'███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒15%',
	'████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒20%',
	'█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒25%',
	'██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒30%',
	'███████▒▒▒▒▒▒▒▒▒▒▒▒▒35%',
	'████████▒▒▒▒▒▒▒▒▒▒▒▒40%',
	'█████████▒▒▒▒▒▒▒▒▒▒▒45%',
	'██████████▒▒▒▒▒▒▒▒▒▒50%',
	'███████████▒▒▒▒▒▒▒▒▒55%',
	'████████████▒▒▒▒▒▒▒▒60%',
	'█████████████▒▒▒▒▒▒▒65%',
	'██████████████▒▒▒▒▒▒70%',
	'███████████████▒▒▒▒▒75%',
	'████████████████▒▒▒▒80%',
	'█████████████████▒▒▒85%',
	'██████████████████▒▒90%',
	'███████████████████▒95%',
	'████████████████████100%']
	for i in lista:
		time.sleep(0.05),cls(),print('\n\n\n\n\n\n\n\t\t\t\tCarrengando sistema...\n\t\t\t\t',i)
	cls()

def espaco():
	print("\n" * 5)

def not_in():
	print('\n\tAinda não implementado')

def press():
	input('\n\t\tPressione qualquer tecla para continuar!\n')

def loginText():
	print('''\n
	---------------------
		LOGIN
	---------------------
	''')

def invalida():
	print('\n\tOpção inválida!')

def userInvalido():
	print('\n\tUsuário inválido!')

def passInvalido():
	print('\n\t Matrícula inválida!')

def campoBranco():
	cls()
	print("\n\tO campo não pode ficar em branco!\n")

def finalizar():
	cls()
	# print('\n\tFinalizando sistema!')
	lista = [
	'▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒0%',
	'██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒10%',
	'████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒20%',
	'██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒30%',
	'████████▒▒▒▒▒▒▒▒▒▒▒▒40%',
	'██████████▒▒▒▒▒▒▒▒▒▒50%',
	'████████████▒▒▒▒▒▒▒▒60%',
	'██████████████▒▒▒▒▒▒70%',
	'████████████████▒▒▒▒80%',
	'██████████████████▒▒90%',
	'████████████████████100%']
	for i in lista:	
		time.sleep(0.05),cls(),print('\n\n\n\n\n\n\n\t\t\t\tFinalizando sistema...\n\t\t\t\t',i)
	os.system('taskkill /IM cmd.exe')