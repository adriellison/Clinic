from security.accessControl import *

def listarPaciente(): # 1 = Busca por paciente #CPF 
	try:
		cls()
		print("\t__Informações básicas dos pacientes__\n")
		registro = input('\tInsira o CPF: ')
		cls()
		cnx = getConexao()
		cursor = cnx.cursor()
		query = (f"\tselect Cpf, nomeCompleto, filiacao, dataNacimento, naturalidade, nacionalidade, sexo, estadoCivil, profissão, telefone, email from paciente where cpf = '{registro}'")
		cursor.execute(query)
		for(Cpf, nomeCompleto, filiacao, dataNacimento, naturalidade, nacionalidade, sexo, estadoCivil, profissão, telefone, email) in cursor:
			print(f'''
		____INFORMAÇÕES DO PACIENTE____\n
		{Cpf}
		Nome: {nomeCompleto}\n
		Filiação: {filiacao}\n
		Data de nascimento: {dataNacimento}\n
		Sexo: {sexo}\n
		Profissão: {profissão}\n
		Estado civil: {estadoCivil}\n
		Naturalidade: {naturalidade}\n
		Nacionalidade: {nacionalidade}\n\n
		____INFORMAÇÕES DE CONTATO____\n
		Telefone: {telefone}\n
		E-mail: {email}
			''')
		cursor.close()
		cnx.close()
		press()
		cls()
	except:
		listarPaciente()

def listarTodosPacientes(): # 2 = Informações básicas dos pacientes
	try:
		cls()
		print("\t__Informações básicas dos pacientes__\n")
		cls()
		cnx = getConexao()
		cursor = cnx.cursor()
		query = (f"\tselect nomeCompleto, dataNacimento, sexo, telefone, numeroRG from clinica.infobase")
		cursor.execute(query)
		for(nomeCompleto, dataNacimento, sexo, telefone, numeroRG) in cursor:
			print(f'\n\tNOME: {nomeCompleto}\n\tDATA DE NASCIMENTO: {dataNacimento}\n\tSEXO: {sexo}\n\tTELEFONE: {telefone}\n\tRG: {numeroRG}\n')
		cursor.close()
		cnx.close()
		press()
		cls()
	except:
		listarTodosPacientes()

def consultaMes(): # 3 = Listar consultas por mês
	try:
		cls()
		print("\t__Consultas por mês__\n")
		mes = input('\tInsira o mês: ')
		cls()
		cnx = getConexao()
		cursor = cnx.cursor()
		query = (f"\tselect Paciente.nomeCompleto, Paciente.Cpf from Paciente join Consultas on Paciente.Cpf = Consultas.Cpf where MONTH(Consultas.horarioData) = '{mes}'")
		cursor.execute(query)
		print(f'\n\t\tPacientes atendidos no Mês ({mes})')
		for(nomeCompleto, Cpf) in cursor:
			print(f'\n\t\tNOME: {nomeCompleto}\n\t\tCPF: {Cpf}\n')
		cursor.close()
		cnx.close()
		press()
		cls()
	except:
		consultaMes()

def receitaPorProfissional(): # 4 = Listar receitas dos Médicos
	try:
		cls()
		print("\t__Consultas por mês__\n")
		registro = input('\tNúmero de registro do médico: ')
		cls()
		cnx = getConexao()
		cursor = cnx.cursor()
		query = (f"\tselect nome, registroprofissional, receitaMedica from receitaporprofissional where registroprofissional = '{registro}'")
		cursor.execute(query)
		for(nome, registroprofissional, receitaMedica) in cursor:
			print(f'\n\t\tNOME: {nome}\n\t\tNúmero de registro: {registroprofissional}\n\t\tReceita: {receitaMedica}\n')
		cursor.close()
		cnx.close()
		press()
		cls()
	except:
		receitaPorProfissional()

def editarPaciente(): # 5 = Editar pacientes
	cls()
	cnx = getConexao()
	cursor = cnx.cursor()
	query = (f"\tselect Cpf, nomeCompleto, dataNacimento from paciente\n")
	cursor.execute(query)
	print('\n\t\tINFORMAÇÕES DOS PACIENTES\n')
	for(Cpf, nomeCompleto, dataNacimento) in cursor:
		print(f'''
	Cpf: {Cpf}
	Nome: {nomeCompleto}
	Data de nascimento: {dataNacimento}
		''')
	cursor.close()
	cnx.close()
	
	Cpf = input('\t\tCpf do registro a ser editado?\n\t>: ')

	cls()
	if Cpf == '':
		print('Nenhum registro editado!')
		press()
	else:
		cnx = getConexao()
		cursor = cnx.cursor()
		query1 = (f"\nSELECT Cpf, nomeCompleto, filiacao, dataNacimento, naturalidade, nacionalidade, sexo, estadoCivil, profissão, telefone, email, senha FROM paciente WHERE Cpf = '{Cpf}'")
		cursor.execute(query1)
		for(Cpf, nomeCompleto, filiacao, dataNacimento, naturalidade, nacionalidade, sexo, estadoCivil, profissão, telefone, email, senha) in cursor:
			print(f'''
		____INFORMAÇÕES DO PACIENTE____\n
		Cpf: {Cpf}\n
		Nome: {nomeCompleto}\n
		Filiação: {filiacao}\n
		Data de nascimento: {dataNacimento}\n
		Naturalidade: {naturalidade}\n
		Nacionalidade: {nacionalidade}\n\n
		Sexo: {sexo}\n
		Estado civil: {estadoCivil}\n
		Profissão: {profissão}\n
		____INFORMAÇÕES DE CONTATO____\n
		Telefone: {telefone}\n
		E-mail: {email}
		Senha: {senha}
			''')
		cursor.close()
		cnx.close()
		print("\n\n\t\t__ O que deseja fazer? __\n\t\t1 - editar\t 2 - nova busca\t 3 - cancelar")
		choice = int(input(">: "))
		if(choice == 1):
			print('\n\n')
			novo_Cpf = input('\tNovo cpf [{}]: '.format(Cpf))
			novo_nomeCompleto = input('\tNovo nome [{}]: '.format(nomeCompleto))
			novo_filiacao = input('\tNovo filiação [{}]: '.format(filiacao))
			novo_dataNacimento = input('\tNova data de nascimento [{}]: '.format(dataNacimento))
			novo_naturalidade = input('\tNovo naturalidade[{}]: '.format(naturalidade))
			novo_nacionalidade = input('\tNova nacionalidade[{}]: '.format(nacionalidade))
			novo_sexo = input('\tNovo sexo[{}]: '.format(sexo))
			novo_estadoCivil = input('\tNovo estado civil[{}]: '.format(estadoCivil))
			novo_profissão = input('\tNova profissão[{}]: '.format(profissão))
			novo_telefone = input('\tNovo telefone[{}]: '.format(telefone))
			novo_email = input('\tNovo e-mail[{}]: '.format(email))
			novo_senha = input('\tNova senha[{}]: '.format(senha))

			if novo_Cpf == '':
				novo_Cpf = Cpf
			if novo_nomeCompleto == '': 	
				novo_nomeCompleto = nomeCompleto
			if novo_filiacao == '': 	
				novo_filiacao = filiacao
			if novo_dataNacimento == '': 	
				novo_dataNacimento = dataNacimento
			if novo_naturalidade == '': 	
				novo_naturalidade = naturalidade
			if novo_nacionalidade == '': 	
				novo_nacionalidade = nacionalidade
			if novo_sexo == '': 	
				novo_sexo = sexo
			if novo_estadoCivil == '': 	
				novo_estadoCivil = estadoCivil
			if novo_profissão == '': 	
				novo_profissão = profissão
			if novo_telefone == '': 	
				novo_telefone = telefone
			if novo_email == '': 	
				novo_email = email
			if novo_senha == '': 	
				novo_senha = senha

			cls()
			print(f'''\n\n
			<< Dados que serão alterados >>\n
			Cpf: {novo_Cpf}\n
			Nome: {novo_nomeCompleto}\n
			Filiação: {novo_filiacao}\n
			Data de nascimento: {novo_dataNacimento}\n
			Naturalidade: {novo_naturalidade}\n
			Nacionalidade: {novo_nacionalidade}\n
			Sexo: {novo_sexo}\n
			Estado civil: {novo_estadoCivil}\n
			Profissão: {novo_profissão}\n
			____INFORMAÇÕES DE CONTATO____\n
			Telefone: {novo_telefone}\n
			E-mail: {novo_email}
			Senha: {novo_senha}\n

			__ O que deseja fazer? __
			1 - salvar\t 2 - editar\t 3 - cancelar
				''')
			choice2 = int(input("\n\t\t>: "))
			if(choice2 == 1):
				cnx = getConexao()
				cursor = cnx.cursor()
				# atualizar = 'UPDATE Paciente SET Cpf = %s, nomeCompleto = %s, filiacao = %s, dataNacimento = %s, naturalidade = %s, nacionalidade = %s, sexo = %s, estadoCivil = %s, profissão = %s, telefone = %s, email = %s WHERE id = %s'
				atualizar = (f"UPDATE Paciente SET Cpf = '{novo_Cpf}', nomeCompleto = '{novo_nomeCompleto}', filiacao = '{novo_filiacao}', dataNacimento = '{novo_dataNacimento}', naturalidade = '{novo_naturalidade}', nacionalidade = '{novo_nacionalidade}', sexo = '{novo_sexo}', estadoCivil = '{novo_estadoCivil}', profissão = '{novo_profissão}', telefone = '{novo_telefone}', email = '{novo_email}', senha = '{novo_senha}' WHERE Cpf = '{Cpf}'")
				# cursor.execute(atualizar,(novo_Cpf, novo_nomeCompleto, novo_filiacao, novo_dataNacimento, novo_naturalidade, novo_nacionalidade, novo_sexo, novo_estadoCivil, novo_profissão, novo_telefone, novo_email))
				cursor.execute(atualizar)
				cnx.commit()
				cursor.close()
				cnx.close()
				print('\n\t\tDados alterados com sucesso!')
				press()
			elif(choice2 == 2):
				editarPaciente()
			else:
				cls()
		elif(choice == 2):
			editarPaciente()
		else:
			cls()
		cls()

def editarFuncionario():# 6 = Editar funcionario
	not_in()

def editarExame(): # 7 = Editar exame
	not_in()

def pacienteHapvida(): # 8 = Verificar paciente Hapvida
	not_in()

def pacienteUnimed(): # 9 = Verificar paciente Unimed,f\
	not_in()

def deletarPaciente(): # 10 = Apagar paciente
	# try:
	# -------------------- mostrar todos os registros
	cls()
	print("\t__Apagar registro de paciente__\n")
	cnx = getConexao()
	cursor = cnx.cursor()
	query = (f"\tselect Cpf, nomeCompleto, dataNacimento, senha from paciente order by nomeCompleto") #where cpf = '{registro}'
	cursor.execute(query)
	for(Cpf, nomeCompleto, dataNacimento, senha) in cursor:
		print(f'''
	____INFORMAÇÕES DO PACIENTE____\n
	Cpf: {Cpf}\tSenha {senha}
	Nome: {nomeCompleto}\n
	Data de nascimento: {dataNacimento}\n
		''')
	cursor.close()
	cnx.close()

	# -------------------- selecionar apenas um registro
	Cpf = input("\n\t\tCpf do registro a ser excluido: \n\n\t>: ")
	cls()
	cnx = getConexao()
	cursor = cnx.cursor()
	query = (f"\tselect Cpf, nomeCompleto, dataNacimento, senha from paciente where Cpf = '{Cpf}'")
	cursor.execute(query)
	for(Cpf, nomeCompleto, dataNacimento, senha) in cursor:
		print(f'''
		INFORMAÇÕES DO PACIENTE\n
	Cpf: {Cpf}\t
	Senha {senha}
	Nome: {nomeCompleto}\n
	Data de nascimento: {dataNacimento}\n
		''')
	cursor.close()
	cnx.close()

	# -------------------- pegar registro para exclusão
	if Cpf == '':
		print('\n\tNenhum registro selecionado!\n')
	else:
		print('''\n
		__ O que deseja fazer? __
			1 - Excluir\t 2 - Selecionar outro registro\t 3 - Cancelar
		''')
		decisao = int(input("\n\t>: "))
		if(decisao == 1):
			cnx = getConexao()
			cursor = cnx.cursor()
			deletar = (f"delete from Paciente where Cpf = '{Cpf}'")
			cursor.execute(deletar)
			cnx.commit()
			cursor.close()
			cnx.close()
			print('\n\tRegistro excluido com sucesso!\n')
		elif(decisao == 2):
			deletarPaciente()
		else:
			cls()
	# except:
	# 	listarPaciente()

def deletarFuncionario(): # 11 = Apagar funcionario
	# -------------------- mostrar todos os registros
	cls()
	print("\t__Apagar registro de paciente__\n")
	cnx = getConexao()
	cursor = cnx.cursor()
	query = (f"\tselect Cpf, nomeCompleto, dataNacimento, senha from paciente order by nomeCompleto") #where cpf = '{registro}'
	cursor.execute(query)
	for(Cpf, nomeCompleto, dataNacimento, senha) in cursor:
		print(f'''
	____INFORMAÇÕES DO PACIENTE____\n
	Cpf: {Cpf}\tSenha {senha}
	Nome: {nomeCompleto}\n
	Data de nascimento: {dataNacimento}\n
		''')
	cursor.close()
	cnx.close()

	# -------------------- selecionar apenas um registro
	Cpf = input("\n\t\tCpf do registro a ser excluido: \n\n\t>: ")
	cls()
	cnx = getConexao()
	cursor = cnx.cursor()
	query = (f"\tselect Cpf, nomeCompleto, dataNacimento, senha from paciente where Cpf = '{Cpf}'")
	cursor.execute(query)
	for(Cpf, nomeCompleto, dataNacimento, senha) in cursor:
		print(f'''
		INFORMAÇÕES DO PACIENTE\n
	Cpf: {Cpf}\t
	Senha {senha}
	Nome: {nomeCompleto}\n
	Data de nascimento: {dataNacimento}\n
		''')
	cursor.close()
	cnx.close()

	# -------------------- pegar registro para exclusão
	if Cpf == '':
		print('\n\tNenhum registro selecionado!\n')
	else:
		print('''\n
		__ O que deseja fazer? __
			1 - Excluir\t 2 - Selecionar outro registro\t 3 - Cancelar
		''')
		decisao = int(input("\n\t>: "))
		if(decisao == 1):
			cnx = getConexao()
			cursor = cnx.cursor()
			deletar = (f"delete from Paciente where Cpf = '{Cpf}'")
			cursor.execute(deletar)
			cnx.commit()
			cursor.close()
			cnx.close()
			print('\n\tRegistro excluido com sucesso!\n')
		elif(decisao == 2):
			deletarPaciente()
		else:
			cls()
	# except:
	# 	listarPaciente()