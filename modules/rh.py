from security.accessControl import *

def tiposExame():
	cls()
	print("\t__Tipos de exames__\n") # Exames disponiveis da clinica
	cnx = getConexao()
	cursor = cnx.cursor()
	query = (f"\tSELECT tipoExame FROM exames")
	cursor.execute(query)
	for(tipoExame) in cursor:
		exames = tipoExame[0].split(" ")[0]
		print(f'\t{exames}')
	cursor.close()
	cnx.close()

def historicoExames():
	try:
		cls()
		print("\t__Todos os exames__\n")
		registro = input('\tInsira o CPF: ')
		cls()
		cnx = getConexao()
		cursor = cnx.cursor()
		query = (f"\tselect nomeCompleto, Cpf, horarioData from consultames where Cpf = '{registro}' order by horarioData")
		cursor.execute(query)
		for(nomeCompleto, Cpf, horarioData) in cursor:
			# exames = tipoExame[0].split(" ")[0]
			print(f'\n\t\t   Nome: {nomeCompleto}\n\t\t    Cpf: {Cpf}\n\tUltima consulta: {horarioData}')
		cursor.close()
		cnx.close()
	except:
		historicoExames()

def cadastrarExame():
	try:
		cls()
		print("\t__Cadastrar exame__\n")
		exame = input("Exame: ")
		if(exame == ''):
			print("O campo não pode ser vazio")
			press()
			cadastrarExame()
		nome = input("Madricula: ")
		matricula = input("Madricula: ")
	except:
		cadastrarExame()


def adicionarFuncionario():
	not_in()
	try:
		cls()
		print("\t__Cadastrar Funcionário__\n")
		matricula = input("Matricula: ")
		if(matricula == ''):
			print("O campo não pode ser vazio")
			press()
			cadastrarExame()
		nome = input("Madricula: ")
		matricula = input("Madricula: ")
	except:
		cadastrarExame()