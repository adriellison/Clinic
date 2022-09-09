from configs.simple import *
from database.conexao import *

def testeUser():
	try:
		usuario = input('\tUsuário: ')
		if usuario == '':
			print('Necessário inserir usuário!')
			testeUser()
		else:
			cnx = getConexao()
			cursor = cnx.cursor()
			usuariobd = (f"SELECT nome FROM funcionario WHERE nome LIKE '%{usuario}%'")
			cursor.execute(usuariobd)
			for(nome) in cursor:
				nome
			cursor.close()
			cnx.close()
			
			user = nome[0].split(" ")[0]
			if(usuario == user):
				user
			else:
				userInvalido()
				testeUser()
		return user
	except:
		cls()
		espaco()
		userInvalido()
		testeUser()

def testeSenha():
	try:
		senha = input('\tMatricula: ')
		if senha == '':
			print('Necessário inserir matricula!')
			testeSenha()
		else:
			cnx = getConexao()
			cursor = cnx.cursor()
			senhabd = (f"SELECT idMatricula FROM funcionario WHERE idMatricula LIKE '%{senha}%'")
			cursor.execute(senhabd)
			for(idMatricula) in cursor:
				idMatricula[0]
			cursor.close()
			cnx.close()
			
			password = idMatricula[0].split(" ")[0]
			if(senha == password):
				password
			else:
				passInvalido()
				testeSenha()
		return password
	except:
		cls()
		espaco()
		passInvalido()
		testeSenha()

def validacao():
	cls()
	loginText()
	usuario = testeUser()
	senha = testeSenha()
	# print(usuario)
	# print(senha)
	cnx = getConexao()
	cursor = cnx.cursor()
	query = (f"SELECT nome, idMatricula FROM funcionario WHERE nome LIKE '%{usuario}%' and idMatricula = '{senha}'")
	cursor.execute(query)
	for nome, idMatricula in cursor:
		# print(nome, senha)
		cls()
		print(f'\n\t\tSeja bem vindo(a): {nome} ')
	print()
	cursor.close()
	cnx.close()


def accessControl():
	validacao()