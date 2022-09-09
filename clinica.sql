/*Cria o banco*/
create database clinica;
/*Usa o banco*/
use clinica;

/*Cria a tabela Paciente*/
create table Paciente(Cpf varchar(240) PRIMARY KEY, nomeCompleto varchar(240), filiacao varchar(240), dataNacimento date, naturalidade varchar(240), nacionalidade varchar(240), sexo varchar(240), estadoCivil varchar(240), profissão varchar(240), telefone varchar(240), email varchar(240), senha varchar(240));
/*Popula a tabela Paciente*/
INSERT INTO Paciente values(02563257852, 'Joao Vitor Maia', 'Maria Lucia Lima e Jose Luiz Maia', 19960215, 'russas', 'brasileiro', 'masculino', 'solteiro', 'estudante', '88996302570', 'joao10@gmail.com', 'joao123');
INSERT INTO Paciente values(00376869253, 'Larissa Silva', 'Lourival Carvalho e Brigida Silva', 20000829, 'parnamirim,', 'brasileiro', 'feminino', 'solteira', 'estudante', '85999017766', 'LarissaL@hotmail.com', 'larentaa1');
INSERT INTO Paciente values(01676869253, 'Matheus Souza', 'Caio Silveira e Rita Souza', 19610829, 'quixada', 'brasileiro', 'masculino', 'casado', 'engenheiro quimico', '88999007766', 'MatS@gmail.com', '12345');
INSERT INTO Paciente values(01686869253, 'Jake Carvalho', 'Sebastião Carvalho e Teresa Araujo', 19930829, 'Porto Velho', 'brasileiro', 'masculino', 'solteiro', 'vendendor', '69999007761', 'JatS@gmail.com', '123456');
INSERT INTO Paciente values(01696869253, 'Afonso Florencio', 'Romulo Florencio e Jeruza Pinto', 19430524, 'sobral', 'brasileiro', 'masculino', 'casado', 'aposentado', '85999007762', 'afonsof@gmail.com', '1234567');
INSERT INTO Paciente values(01666869253, 'Tales Paulino', 'Jose Carmo e Sueli Paulino', 20000601, 'fortaleza', 'brasileiro', 'masculino', 'solteiro', 'estudante', '88999007763', 'PaulinoP@gmail.com', '12345678');
INSERT INTO Paciente values(01656869253, 'Sueli Andrade', 'Vitor Lemos e Mariane Andrade', 19750829, 'Aracati', 'brasileira', 'feminino', 'casada', 'costureira', '88999007764', 'SuS@gmail.com', '123456789');
INSERT INTO Paciente values(01646869253, 'Neila Pauline', 'Jose Carmo e Sueli Paulino', 19970829, 'Fortaleza', 'brasileira', 'feminino', 'solteira', 'arquiteta', '88999007765', 'NeS@gmail.com', '12345678910');
INSERT INTO Paciente values(01636869253, 'João Nishimura', 'Guilherme Nishimura e Sara Luiz', 20000531, 'Fortaleza', 'brasileiro', 'masculino', 'solteiro', 'estudante', '88999007767', 'Nishi@gmail.com', '123456');
INSERT INTO Paciente values(01626869253, 'Doulgas Leto', 'Jared Leto e Amber Souza', 19850829, 'Rio de Janeiro', 'brasileiro', 'masculino', 'casado', 'desempregado', '88999007768', 'DouL@gmail.com', '12345');

/*Cria a tabela PacienteRG*/
create table PacienteRG(Cpf varchar(240) REFERENCES Paciente, numeroRG varchar(240), orgaoEmissor varchar(240), dataExpedição date);
/*Popula a tabela PacienteRG*/
INSERT INTO PacienteRG values(02563257852, 20275809097, 'sspds', 20060610);
INSERT INTO PacienteRG values(00376869253, 1175767, 'sspce', 20180910);
INSERT INTO PacienteRG values(01676869253, 1175705, 'sspqx', 19990201);
INSERT INTO PacienteRG values(01686869253, 1175704, 'ssppt', 19970302);
INSERT INTO PacienteRG values(01696869253, 1175703, 'sspso', 19980117);
INSERT INTO PacienteRG values(01666869253, 1175702, 'sspft', 20030517);
INSERT INTO PacienteRG values(01656869253, 1175701, 'sspac', 19930916);
INSERT INTO PacienteRG values(01646869253, 1175706, 'sspft', 20000117);
INSERT INTO PacienteRG values(01636869253, 1175707, 'sspft', 20050219);
INSERT INTO PacienteRG values(01626869253, 1175708, 'ssprj', 19911117);

/*Cria a tabela PacienteEndereço*/
create table PacienteEndereço(Cpf varchar(240) REFERENCES paciente, cep varchar(240) PRIMARY KEY, logradouroCEP varchar(240), ruaCEP varchar(240), cidadeCEP varchar(240), complementoCEP varchar(240), bairroCEP varchar(240), estadoCEP varchar(240));
/*Popula a tabela PacienteEndereço*/
INSERT INTO PacienteEndereço values(02563257852, '62871888', 'rua', 'joao fidelis maia', 'russas', 'prox ao posto de saude', 'centro', 'ceara');
INSERT INTO PacienteEndereço values(00376869253, '60176046', 'rua', 'arauja', 'parnamirim', 'mercado hiper', 'lonas', 'paraiba');
INSERT INTO PacienteEndereço values(01676869253, '80555546', 'rua', 'rio de janeiro', 'quixada', 'ufc', 'tanso', 'ceara');
INSERT INTO PacienteEndereço values(01686869253, '70555546', 'rua', 'rio de janeiro', 'Porto Velho', 'ufc', 'tanso', 'ceara');
INSERT INTO PacienteEndereço values(01696869253, '00555546', 'rua', 'rio de janeiro', 'sobral', 'ufc', 'tanho', 'ceara');
INSERT INTO PacienteEndereço values(01666869253, '20555546', 'rua', 'pereira de miranda', 'fortaleza', 'papicu', 'papicu', 'ceara');
INSERT INTO PacienteEndereço values(01656869253, '30555546', 'rua', 'rio de janeiro', 'aracati', 'unir', 'alem', 'ceara');
INSERT INTO PacienteEndereço values(01646869253, '40555546', 'rua', 'pereira de miranda', 'fortaleza', 'papicu', 'papicu', 'ceara');
INSERT INTO PacienteEndereço values(01636869253, '50555546', 'rua', 'rio', 'fortaleza', 'rio mar', 'castelao', 'ceara');
INSERT INTO PacienteEndereço values(01626869253, '10555546', 'rua',  '25 de março', 'Rio de Janeiro', 'ufrj', 'talacaia', 'Rio de Janeiro');

/*Cria a tabela Funcionario*/
create table Funcionario(idMatricula varchar(240) PRIMARY KEY, nome varchar(240), tipoFunc varchar(240), departamentoAtuação varchar(240), registroprofissional varchar(240),
nomeCompletoMed varchar(240), especialização varchar(240), conveniosAtendidos varchar(240), dataDisponivel date);
/*Popula a tabela Funcionario*/
INSERT INTO Funcionario(idMatricula, nome, tipoFunc, departamentoAtuação) values(15289, 'Larissa Nunes de Araújo', 'operacional', 'recepção');
INSERT INTO Funcionario values(82298, 'Lurdes Oliveira', 'médica', 'consultório medico', '225897', 'Lurdes Oliveira Miranda', 'obstreticia', 'unimed', 20210924);
INSERT INTO Funcionario(idMatricula, nome, tipoFunc, departamentoAtuação) values(88887,'Luiz Ruas', 'professional exames', 'Administrativo');
INSERT INTO Funcionario values(88888,'Ronaldo Custodio', 'médica', 'departamento medico', '222222', 'Ronaldo Custodio', 'ortopedista', 'unimed', 20211024);
INSERT INTO Funcionario(idMatricula, nome, tipoFunc, departamentoAtuação) values(88886,'Ana Carvalho', 'enfermeira', 'consultorio secundario');
INSERT INTO Funcionario values(88885,'Beatriz Lena', 'psicologa', 'psicologia', '333333', 'Beatriz Lena', 'infantil', '', 20211023);
INSERT INTO Funcionario(idMatricula, nome, tipoFunc, departamentoAtuação) values(88884,'Pablo Costa', 'Administrativo', 'Analista financeiro');
INSERT INTO Funcionario(idMatricula, nome, tipoFunc, departamentoAtuação) values(88883,'Rosineide Leite', 'operacional', 'recepção');
INSERT INTO Funcionario(idMatricula, nome, tipoFunc, departamentoAtuação) values(88882,'Márcio Carvalho', 'operacional', 'recepção');
INSERT INTO Funcionario(idMatricula, nome, tipoFunc, departamentoAtuação) values(88881,'Rodolfo Linho', 'Administrativo', 'profissional de exames');

/*Cria a tabela Exames*/
create table Exames(tipoExame varchar(240) PRIMARY KEY, horarioData date, idMatricula int REFERENCES Funcionario);
/*Popula a tabela Exames*/
INSERT INTO Exames(tipoExame, idMatricula) values('radiografia', 888887);
INSERT INTO Exames(tipoExame, horarioData) values('sangue', 20210815);
INSERT INTO Exames(tipoExame, idMatricula) values('tomografia', 888881);
INSERT INTO Exames(tipoExame, horarioData) values('mamagrafia', 20210816);
INSERT INTO Exames(tipoExame, idMatricula) values('ressonancia magnetica', 888887);
INSERT INTO Exames(tipoExame, horarioData) values('endoscopia', 20211124);
INSERT INTO Exames(tipoExame, idMatricula) values('hemograma', 888886);
INSERT INTO Exames(tipoExame, horarioData) values('ultrassom', 20211023);
INSERT INTO Exames(tipoExame, idMatricula) values('ecocardiograma', 888881);
INSERT INTO Exames(tipoExame, horarioData) values('ocular', 20210901);

/*Cria a tabela Pagamento*/
create table Pagamento(codPagamento int PRIMARY KEY, nomeConvenio  varchar(240), planos  varchar(240), bandeira  varchar(240), credito char(1) , debito char(1), numero varchar(240),
titular  varchar(240), CVV int, pix varchar(240), boleto double);
/*Popula a tabela Pagamento*/
INSERT INTO Pagamento(codPagamento, nomeConvenio, planos) values(2589, 'Unimed', 'plano mais');
INSERT INTO Pagamento(codPagamento, bandeira, credito, numero, titular, CVV) values(5274, 'Mastercard', 'C', '25897 6895 8916 5566', 'Larissa Silva', 875);
INSERT INTO Pagamento(codPagamento, pix) values(8596, 'joao10@gmail.com');
INSERT INTO Pagamento(codPagamento, nomeConvenio, planos) values(2555, 'hapvida', 'plano simples');
INSERT INTO Pagamento(codPagamento, nomeConvenio, planos) values(1000, 'unimed', 'plano geral');
INSERT INTO Pagamento(codPagamento, nomeConvenio, planos) values(1111, 'unimed', 'plano escapando da morte');
INSERT INTO Pagamento(codPagamento, nomeConvenio, planos) values(1010, 'Unimed', 'plano luxo');
INSERT INTO Pagamento(codPagamento, nomeConvenio, planos) values(0912, 'hapvida', 'plano americano');
INSERT INTO Pagamento(codPagamento, nomeConvenio, planos) values(2345, 'hapvida', 'plano simples');
INSERT INTO Pagamento(codPagamento, nomeConvenio, planos) values(1222, 'unimed', 'plano médio');
INSERT INTO Pagamento(codPagamento, nomeConvenio, planos) values(1223, 'hapvida', 'plano médio');
INSERT INTO Pagamento(codPagamento, nomeConvenio, planos) values(1224, 'unimed', 'plano médio');

/*Cria a tabela Consultas*/
create table Consultas(idMatricula int REFERENCES Funcionario, registroProfissional varchar(240) REFERENCES Funcionario, Cpf varchar(240) REFERENCES Paciente, horarioData date, receitaMedica varchar(240));
/*Popula a tabela Consultas*/
INSERT INTO Consultas values(82298, '225897', 02563257852, 20210810, 'paracetamol');
INSERT INTO Consultas values(82298, '225897', 00376869253, 20210821, 'omoxilina');
INSERT INTO Consultas values(88888, '222222', 01676869253, 20210911, 'buscopan');
INSERT INTO Consultas values(82298, '225897', 01696869253, 20211012, 'quacpan');
INSERT INTO Consultas values(88888, '222222', 01666869253, 20211016, 'tilenol');
INSERT INTO Consultas values(82298, '225897', 01656869253, 20211014, 'dipirona');
INSERT INTO Consultas values(88888, '222222', 01646869253, 20211015, 'morfina');
INSERT INTO Consultas values(82298, '225897', 01636869253, 20210811, 'dorflex');
INSERT INTO Consultas values(82298, '225897', 01626869253, 20210814, 'omega3');
INSERT INTO Consultas values(88888, '222222', 01686869253, 20210820, 'biomag');

/*Cria a tabela MedicoAtendeConvenio*/
create table MedicoAtendeConvenio(idMatricula int REFERENCES Funcionario, registroProfissional int REFERENCES Funcionario, nomeConvenio varchar(240) REFERENCES Pagamento,
Codpagamento varchar(240) REFERENCES Pagamento);
/*Popula a tabela MedicoAtendeConvenio*/
INSERT INTO MedicoAtendeConvenio values(82298, 225897, 'Unimed',  '2589');
INSERT INTO MedicoAtendeConvenio values(82298, 225897, 'Hapvida', '2555');
INSERT INTO MedicoAtendeConvenio values(88888, 222222, 'hapvida', '0912');
INSERT INTO MedicoAtendeConvenio values(88888, 222222, 'unimed', '1000');
INSERT INTO MedicoAtendeConvenio values(82298, 225897, 'unimed', '1111');
INSERT INTO MedicoAtendeConvenio values(88888, 222222, 'unimed', '1010');
INSERT INTO MedicoAtendeConvenio values(82298, 225897, 'hapvida', '0912');
INSERT INTO MedicoAtendeConvenio values(88888, 222222, 'hapvida', '2345');
INSERT INTO MedicoAtendeConvenio values(88888, 222222, 'unimed', '1222');
INSERT INTO MedicoAtendeConvenio values(82298, 225897, 'unimed', '1224');

/*Cria a tabela ConsultasPreescreverExames*/
create table ConsultasPreescreverExames(idMatricula int REFERENCES Funcionario, registroProfissional varchar(240) REFERENCES Funcionario, Cpf varchar(240) REFERENCES Paciente, tipoExame varchar(240) REFERENCES Exames);
/*Popula a tabela ConsultasPreescreverExame*/
INSERT INTO ConsultasPreescreverExames values(82298, '225897', 02563257852, 'sangue');
INSERT INTO ConsultasPreescreverExames values(82298, '225897', 01626869253, 'radiografia');
INSERT INTO ConsultasPreescreverExames values(88888, '222222', 01636869253, 'tomografia');
INSERT INTO ConsultasPreescreverExames values(88888, '222222', 01646869253, 'sangue');
INSERT INTO ConsultasPreescreverExames values(82298, '225897', 01656869253, 'ressonancia magnetica');
INSERT INTO ConsultasPreescreverExames values(88888, '222222', 01666869253, 'radiografia');
INSERT INTO ConsultasPreescreverExames values(82298, '225897', 01696869253, 'sangue');
INSERT INTO ConsultasPreescreverExames values(88888, '222222', 01686869253, 'Ultrassom');
INSERT INTO ConsultasPreescreverExames values(88888, '222222', 01676869253, 'sangue');
INSERT INTO ConsultasPreescreverExames values(82298, '225897', 00376869253, 'ocular');

/*Cria a tabela PacienteAssinaConvenio*/
create table PacienteAssinaConvenio(Cpf varchar(240) REFERENCES Paciente, nomeConvenio varchar(240) REFERENCES Pagamento, codPagamento int REFERENCES Pagamento);
/*Popula a tabela PacienteAssinaConvenio*/
INSERT INTO PacienteAssinaConvenio values(02563257852, 'Unimed', '2589');
INSERT INTO PacienteAssinaConvenio values(01626869253, 'hapvida', '2555');
INSERT INTO PacienteAssinaConvenio values(01636869253, 'hapvida', '0912');
INSERT INTO PacienteAssinaConvenio values(01646869253, 'unimed', '1000');
INSERT INTO PacienteAssinaConvenio values(01656869253, 'unimed', '1111');
INSERT INTO PacienteAssinaConvenio values(01666869253, 'unimed', '1010');
INSERT INTO PacienteAssinaConvenio values(01696869253, 'hapvida', '0912');
INSERT INTO PacienteAssinaConvenio values(01686869253, 'hapvida', '2345');
INSERT INTO PacienteAssinaConvenio values(01676869253, 'unimed', '1222');
INSERT INTO PacienteAssinaConvenio values(00376869253, 'unimed', '1224');

/*Cria a tabela ConsultaRealizaPagamento*/
create table ConsultaRealizaPagamento(idMatricula int REFERENCES Funcionario, registroProfissional varchar(240) REFERENCES Funcionario, Cpf varchar(240) REFERENCES Paciente, codPagamento int REFERENCES Pagamento);
/*Popula a tabela ConsultaRealizaPagamento*/
INSERT INTO ConsultaRealizaPagamento values(82298, '225897', 02563257852, 2589);
INSERT INTO ConsultaRealizaPagamento values(88888, '222222', 01626869253, 2555);
INSERT INTO ConsultaRealizaPagamento values(88888, '222222', 01636869253, 0912);
INSERT INTO ConsultaRealizaPagamento values(82298, '225897', 01646869253, 1000);
INSERT INTO ConsultaRealizaPagamento values(88888, '222222', 01656869253, 1111);
INSERT INTO ConsultaRealizaPagamento values(82298, '225897', 01666869253, 1010);
INSERT INTO ConsultaRealizaPagamento values(82298, '225897', 01696869253, 0912);
INSERT INTO ConsultaRealizaPagamento values(88888, '222222', 01686869253, 2345);
INSERT INTO ConsultaRealizaPagamento values(88888, '222222', 01676869253, 1222);
INSERT INTO ConsultaRealizaPagamento values(82298, '225897', 00376869253, 1224);

/*-----------Consultas simples-------------*/
/*Ver as tabelas existentes no banco*/
show tables;
/*Exibe todos os valores dentro de cada tabela com o nome respectivo*/
select * from paciente;
select * from PacienteRG;
select * from PacienteEndereço;
select * from Funcionario;
select * from Exames;
select * from Pagamento;
select * from Consultas;
select * from MedicoAtendeConvenio;
select * from ConsultasPreescreverExames;
select * from PacienteAssinaConvenio;
select * from ConsultaRealizaPagamento;
/*---------view consulta complexa---------*/
/*Cria as views*/
CREATE VIEW `infoBase` AS(select paciente.nomeCompleto, paciente.dataNacimento, paciente.sexo, paciente.telefone, pacienteRg.numeroRG from paciente join pacienteRG on paciente.Cpf = pacienteRG.Cpf);
CREATE VIEW `pacienteUnimed` AS(select paciente.nomeCompleto, paciente.cpf, PacienteAssinaConvenio.nomeConvenio  from paciente join PacienteAssinaConvenio on paciente.cpf = PacienteAssinaConvenio.cpf where PacienteAssinaConvenio.nomeConvenio = 'Unimed');
CREATE VIEW `pacienteHapvida` AS(select paciente.nomeCompleto, paciente.cpf, PacienteAssinaConvenio.nomeConvenio  from paciente join PacienteAssinaConvenio on paciente.cpf = PacienteAssinaConvenio.cpf where PacienteAssinaConvenio.nomeConvenio = 'hapvida');
CREATE VIEW `receitaPorProfissional` AS(select Funcionario.nome, Funcionario.registroprofissional, Consultas.receitaMedica from Funcionario join Consultas on Funcionario.registroprofissional = Consultas.registroprofissional order by Funcionario.registroprofissional);
CREATE VIEW `consultaMes` AS(select Paciente.nomeCompleto, Paciente.Cpf, Consultas.horarioData from Paciente join Consultas on Paciente.Cpf = Consultas.Cpf where MONTH(Consultas.horarioData) = '10');
CREATE VIEW `vacinaCovid` AS(select Paciente.nomeCompleto, Paciente.Cpf, PacienteEndereço.ruaCep, PacienteEndereço.cidadeCep  from Paciente join PacienteEndereço on Paciente.Cpf = PacienteEndereço.Cpf where PacienteEndereço.cidadeCep = 'fortaleza' order by Paciente.nomeCompleto);

/*----------Exibe os valores das views das consultas complexas----------*/
/*Exibe o valor da view, retornando os nomes dos pacientes, data de nascimento, sexo, telefone, RG*/
select * from infoBase;
/*Exibe o valor da view, retornando os nomes dos pacientes, CPF, nome do convenio que estão dentro do convenio Unimed*/
select * from pacienteUnimed;
/*Exibe o valor da view, retornando os nomes dos pacientes, CPF, nome do convenio que estão dentro do convenio Hapvida*/
select * from pacienteHapvida;
/*Exibe o valor da view, retornando os nomes dos funcionario, seus registros profissionais e receitas medicas que eles receitaram aos pacientes, onde estão ordenados pelo registro profissional*/
select * from receitaPorProfissional;
/*Exibe o valor da view, retornando os nomes dos pacientes, CPF e a data da consulta dos pacientes atendidos no mes 10*/
select * from consultaMes;
/*Exibe o valor da view, retornando nome dos pacientes, CPF, endereço e cidade dos pacientes que residem na cidade de Fortaleza*/
select * from vacinaCovid;
/*------------------------*/