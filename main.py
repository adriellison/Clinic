# Bibliotecas
from os import system
import mysql.connector
# import os
# import random
# import time
# from colorconsole import terminal

# Funções
from configs.logo import *
from configs.simple import *
from database.conexao import *
from guide.help import *
from security.accessControl import *

# Acessando módulos
import modules.adm
import modules.recepcao
import modules.rh
import modules.outros
import guide.help

# Menu de acesso aos módulos
def entrarAdm():
	try:
		cls()
		print('''\n
		+-----------------------------------------------------------------------+
		|        M  O  D  O        A  D  M  I  N  I  S  T  R  A  T  O  R        |
		|-----------------------------------------------------------------------|
		|  1 = Busca por paciente #CPF                                          |
		|-----------------------------------------------------------------------|
		|  2 = Informações básicas dos pacientes   |  5 = Editar pacientes      |
		|  3 = Listar consultas por mês            |  6 = Editar funcionario    |
		|  4 = Listar receitas dos Médicos         |  7 = Editar exame          |
		|-----------------------------------------------------------------------|
		|  8 = Verificar paciente Hapvida          | 10 = Apagar paciente       |
		|  9 = Verificar paciente Unimed           | 11 = Apagar funcionario    |
		|-----------------------------------------------------------------------|
		|                               0 = Sair                                |
		+-----------------------------------------------------------------------+
	''')
		opcao = int(input('\t>:  '))
		if opcao == 1:
			modules.adm.listarPaciente()
			entrarAdm()
		elif opcao == 2:
			modules.adm.listarTodosPacientes()
			entrarAdm()
		elif opcao == 3:
			modules.adm.consultaMes()
			entrarAdm()
		elif opcao == 4:
			modules.adm.receitaPorProfissional()
			entrarAdm()
		elif opcao == 5:
			modules.adm.editarPaciente()
			entrarAdm()
		elif opcao == 6:
			not_in()
		elif opcao == 7:
			not_in()
		elif opcao == 8:
			not_in()
		elif opcao == 9:
			not_in()
		elif opcao == 10:
			modules.adm.deletarPaciente()
			entrarAdm()
		elif opcao == 11:
			not_in()
		elif opcao == 0:
			inicio()
		else:
			cls()
			invalida()
	except:
		entrarAdm()

def entrarRecepcao():
	try:
		print('''\n
		+----------------------------------+
		|          -- RECEPÇÃO --          |
		|----------------------------------|
		|  1 = Tipos de exames             |
		|  2 = Historico de exames #todos  |
		|  3 = Marcar exame #cpf           |
		|  4 = Cadastrar paciente          |
		|----------------------------------|
		|             0 = Sair             |
		+----------------------------------+
''')
		opcao = int(input('\t>:  '))
		if opcao == 1:
			modules.recepcao.tiposExame()
			entrarRecepcao()
		elif opcao == 2:
			modules.recepcao.historicoExames()
			entrarRecepcao()
		elif opcao == 3:
			modules.recepcao.marcarExame()
			entrarRecepcao()
		elif opcao == 4:
			modules.recepcao.cadastrarPaciente()
			entrarRecepcao()
		elif opcao == 0:
			inicio()
		else:
			cls()
			invalida()
	except:
		entrarRecepcao()

def entrarRh():
	try:
		print('''\n
		+----------------------------------+
		|      -- Recursos Humanos --      |
		|----------------------------------|
		|  1 = Adicionar exames            |
		|  2 = Adicionar funcionário       |
		|----------------------------------|
		|             0 = Sair             |
		+----------------------------------+
	''')
		opcao = int(input('\t>:  '))
		if opcao == 1:
			modules.rh.cadastrarExame()
		elif opcao == 2:
			modules.rh.adicionarFuncionario()
		elif opcao == 0:
			inicio()
		else:
			cls()
			invalida()
	except:
		entrarRh()

def entrarOpcoes():
	cls()
	not_in()

def entrarInstrucoes():
	cls()
	not_in()

# programa
def inicio():
	os.system('color 3');
	cls()
	while True:
		print('''\n
		+----------------------------------+
		|       -- Menu Principal --       |
		|----------------------------------|
		|                                  |
		|---  SELECIONE O DEPARTAMENTO  ---|
		|                                  |
		|  1 = Administração               |
		|  2 = Recepção                    |
		|  3 = Recursos humanos            |
		|  4 = Opções - Não implementado   |
		|  5 = Instruções                  |
		|----------------------------------|
		|             0 = Sair             |
		+----------------------------------+
	''')
		opcao = int(input('\t>:  '))
		if opcao == 1:
			# accessControl()
			entrarAdm()
		elif opcao == 2:
			# accessControl()
			entrarRecepcao()
		elif opcao == 3:
			# accessControl()
			entrarRh()
		elif opcao == 4:
			entrarOpcoes()
		elif opcao == 5:
			entrarInstrucoes()
		elif opcao == 0:
			os.system('color a');
			finalizar()
		else:
			cls()
			invalida()

os.system('color a');
logo()
os.system('color a');
accessControl()
press()
inicio()