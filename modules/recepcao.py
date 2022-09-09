from security.accessControl import *

def tiposExame(): #1
	cls()
	print("\t\t__Tipos de exames__\n") # Exames disponiveis da clinica
	cnx = getConexao()
	cursor = cnx.cursor()
	query = (f"\t\tSELECT tipoExame FROM exames")
	cursor.execute(query)
	for(tipoExame) in cursor:
		exames = tipoExame[0].split(" ")[0]
		print(f'\t{exames}')
	cursor.close()
	cnx.close()

def historicoExames(): #4
	try:
		cls()
		print("\t\t__Todos os exames__\n") # historico por paciente CPF
		registro = input('\tInsira o CPF: ')
		cls()
		cnx = getConexao()
		cursor = cnx.cursor()
		query = (f"\tselect nomeCompleto, Cpf, horarioData from consultames where Cpf = '{registro}' order by horarioData")
		cursor.execute(query)
		for(nomeCompleto, Cpf, horarioData) in cursor:
			print(f'\n\t\t   Nome: {nomeCompleto}\n\t\t    Cpf: {Cpf}\n\tUltima consulta: {horarioData}')
		cursor.close()
		cnx.close()
	except:
		historicoExames()

def marcarExame(): #5
	cls()
	print("\t_Marcar exame_\n") # marcar exame CPF(Verifica se tem cadastro) DATA
	not_in()

# Cadastrar Paciente ---------------------------------------
def cadastrarPaciente_cpf():
	print("\t_Cadastrar paciente_\n")
	Cpf = input("\tCpf: ")
	if(Cpf == ''):
		campoBranco()
		cadastrarPaciente_cpf()
	else:
		cls()
		return Cpf

def cadastrarPaciente_nome():
	print("\t_Cadastrar paciente_\n")
	nomeCompleto = input("\tNome completo: ")
	if(nomeCompleto == ''):
		campoBranco()
		cadastrarPaciente_nome()
	else:
		cls()
		return nomeCompleto

def cadastrarPaciente_filiacao():
	print("\t_Cadastrar paciente_\n")
	filiacao = input("\tFiliação: ")
	if(filiacao == ''):
		campoBranco()
		cadastrarPaciente_filiacao()
	else:
		cls()
		return filiacao

def cadastrarPaciente_dataNacimento():
	print("\t_Cadastrar paciente_\n")
	print("\tData de nascimento\n")
	dia = input("\tDia: ")
	mes = input("\tMÊs: ")
	ano = input("\tAno: ")
	dataNacimento = ano + mes + dia
	if(dataNacimento == ''):
		campoBranco()
		cadastrarPaciente_dataNacimento()
	else:
		cls()
		return dataNacimento

def cadastrarPaciente_naturalidade():
	print("\t_Cadastrar paciente_\n")
	naturalidade = input("\tNaturalidade: ")
	if(naturalidade == ''):
		campoBranco()
		cadastrarPaciente_naturalidade()
	else:
		cls()
		return naturalidade

def cadastrarPaciente_nacionalidade():
	print("\t_Cadastrar paciente_\n")
	nacionalidade = input("\tNacionalidade: ")
	if(nacionalidade == ''):
		campoBranco()
		cadastrarPaciente_nacionalidade()
	else:
		cls()
		return nacionalidade

def cadastrarPaciente_sexo():
	print("\t_Cadastrar paciente_\n")
	sexo = input("\tSexo: ")
	if(sexo == ''):
		campoBranco()
		cadastrarPaciente_sexo()
	else:
		cls()
		return sexo

def cadastrarPaciente_estadoCivil():
	print("\t_Cadastrar paciente_\n")
	estadoCivil = input("\tEstado civil: ")
	if(estadoCivil == ''):
		campoBranco()
		cadastrarPaciente_estadoCivil()
	else:
		cls()
		return estadoCivil

def cadastrarPaciente_profissao():
	print("\t_Cadastrar paciente_\n")
	profissão = input("\tProfissão: ")
	if(profissão == ''):
		campoBranco()
		cadastrarPaciente_profissao()
	else:
		cls()
		return profissão

def cadastrarPaciente_telefone():
	print("\t_Cadastrar paciente_\n")
	telefone = input("\tTelefone: ")
	if(telefone == ''):
		campoBranco()
		cadastrarPaciente_telefone()
	else:
		cls()
		return telefone

def cadastrarPaciente_email():
	print("\t_Cadastrar paciente_\n")
	email = input("\tE-mail: ")
	if(email == ''):
		campoBranco()
		cadastrarPaciente_email()
	else:
		cls()
		return email

def cadastrarPaciente_senha():
	print("\t_Cadastrar paciente_\n")
	senha = input("\tSenha: ")
	if(senha == ''):
		campoBranco()
		cadastrarPaciente_senha()
	else:
		cls()
		return senha

def cadastrarPaciente():
	cls()
	print("\t\t__Cadastrar Paciente__\n")
	Cpf = cadastrarPaciente_cpf()
	nomeCompleto = cadastrarPaciente_nome()
	filiacao = cadastrarPaciente_filiacao()
	dataNacimento = cadastrarPaciente_dataNacimento()
	naturalidade = cadastrarPaciente_naturalidade()
	nacionalidade = cadastrarPaciente_nacionalidade()
	sexo = cadastrarPaciente_sexo()
	estadoCivil = cadastrarPaciente_estadoCivil()
	profissão = cadastrarPaciente_profissao()
	telefone = cadastrarPaciente_telefone()
	email = cadastrarPaciente_email()
	senha = cadastrarPaciente_senha()

	print(f"Cpf: {Cpf}")
	print(f"Nome Completo: {nomeCompleto}")
	print(f"Filiação: {filiacao}")
	print(f"Data de nascimento: {dataNacimento}")
	print(f"Naturaldiade: {naturalidade}")
	print(f"Nacionalidade: {nacionalidade}")
	print(f"Sexo: {sexo}")
	print(f"Estado Civil: {estadoCivil}")
	print(f"Profissão: {profissão}")
	print(f"Telefone: {telefone}")
	print(f"E-mail: {email}")
	print(f"Senha: {senha}")

	print('''\n
		__ O que deseja fazer? __
			1 - Cadastrar\t 2 - Criar novo registro\t 3 - Cancelar
		''')
	decisao = int(input("\n\t>: "))
	if(decisao == 1):
		adicionar = (f"insert into Paciente(Cpf, nomeCompleto, filiacao, dataNacimento, naturalidade, nacionalidade, sexo, estadoCivil, profissão, telefone, email, senha) values('{Cpf}', '{nomeCompleto}', '{filiacao}', '{dataNacimento}', '{naturalidade}', '{nacionalidade}', '{sexo}', '{estadoCivil}', '{profissão}', '{telefone}', '{email}', '{senha}')")
		cnx = getConexao()
		cursor = cnx.cursor()
		cursor.execute(adicionar)
		cnx.commit()
		cursor.close()
		cnx.close()
		print(f"\n\t\tPaciente {nomeCompleto}\n\t\tCadastrado com sucesso!")
		cls()
	elif(decisao == 2):
		cadastrarPaciente()
	else:
		cls()