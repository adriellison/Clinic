import mysql.connector

from configs.simple import *

def teste_cnx():
	cls()
	try:
		cnx = getConexao()
		print('\n\tConexão ativa!\n')
	except:
		print('\n\tConexão mal sucedida\n')

def getConexao():
	cnx = mysql.connector.connect(host='localhost', user='root', password='admin', database='clinica')
	return cnx