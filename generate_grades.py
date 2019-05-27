# -*- coding: utf-8 -*-
import re
import csv
import sys
import unicodedata

if len(sys.argv) < 4:
	print("\tArgumentos incorretos. Utilizar o formato: python3 script.py <arquivo_com_notas.csv> <turma> <pontuacao_maxima>")
	print("\tExemplo: python3 script.py notas.csv m1 1400")
	print("\tA pontuação máxima está disponível no URI no fim da página principal da disciplina")
	exit();

m1 = [	"Alejandro Tomas Reyes Alberoni", "Alessandra Rosa Galvao", "Bruno Silva Volcan", "Bruno Ramos Martins",
		"Diulia Justin Deon", "Douglas Henrique Santos Lima", "Edilayne Samara Santos Tavares Caetano",
		"Frederico Dal Soglio Reckziegel", "Gabriela Lucena Fernandes", "Gabriele da Silva Lucas", 
		"Guilherme dos Santos Vahl", "Guilherme Goulart Quincozes", "Henrique Morales do Carmo",
		"Italo Teixeira da Silveira", "Joao Antonio Neves Soares",  "Joao Pedro de Morais da Silveira", 
		"Joao Pedro Pires Medeiros", "Joao Vitor Dias Masquevite", "Joao Vitor Lima Araujo da Silva", 
		"Kaio Ferordi Mazza", "Kayara da Silveira Pereira", "Leandro Weber Tavares", "Lenon Rodrigues Koperek",
		"Leonardo dos Santos Guths"]
m2 = [	"Eduardo Weymar Garcia", "Hiago Schroder Mulling", "Lucas Lima", "Lucas Viscardi Marques", 
		"Lucas Wotter Olive Leite", "Marcelo da Silva Dias", "Marcelo Pereira Vargas Rodrigues", 
		"Murillo Aleixo Motta", "Nicolas Costa Goncalves", "Pedro da Luz Kaster", "Pedro Zanchin Baldissera", 
		"Rafael Machado Candia", "Rafael Montagna Copes", "Renata Torres Abib Bertacco", "Rogerio Faria Otto", 
		"Thiago Nunes Batista", "Vinicius Caldas Wrege", "Vitoria da Silva Mota", "Yuri de Melo Zorzoli Nunes"]
m3 = [	"Aline Conceicao da Silva", "Andre Pereira Rodrigues", "Artur Machado de Souza", "Arthur Varga Teles",
		"Arthur Weirich", "Caua Avila da Silva", "Dionata Bergmann Podewils", "Douglas Souza Gomes",
		"Eduardo dos Santos Montenegro Barbosa", "Eduardo Nicoletti Borges", "Eloisa Leal Barros", 
		"Erik Silveira Braga", "Gabriel Sodre de Moura", "Glauco Soares Pantoni", "Gustavo Tessmer Loper", 
		"Hector Hudson Diniz Fernandes", "Igor Henrique Deon da Rosa", "Igor Yuji Ishihara Sakuma", 
		"Joao Lucas da Costa Fagundes", "Joao Pedro Valejo dos Santos", "Julia Manoela Pereira Jambeiro",
		"Leonardo Antonietti Ferreira", "Matheus Oliveira da Rosa"]
m4 = [	"Gabriel Ferreira Amaral", "Hyhickle Ryozo Umetsubo Goncalves", "Klaus Wagner Irion", 
		"Lucas Dias dos Santos", "Lucas Jose do Prado Souza", "Lucas Seidy Ribeiro dos Santos Ikenoue", 
		"Luis Artur Mendes Garcez", "Lyandra da Cruz de Souza", "Maicon Roberto da Luz Coimbra", 
		"Matheus Silva Menezes", "Mauricio Carvalho Mucci", "Pablo Leitzke Norenberg", 
		"Rafael Carvalho Somenzari Ginjas Camargo Muniz", "Rafael Grimmler da Rocha", "Thiago Souza Oliveira", 
		"Vitor de Melo Mandowski", "Willian do Espirito Santo Rodrigues", "Yasmin Rodrigues Martins"]

max_grade = int(sys.argv[3])
grades_m1 = {}
grades_m2 = {}
grades_m3 = {}
grades_m4 = {}

def strip_accents(text):
	""" Strip accents from input String """
	try:
		text = unicode(text, 'utf-8')
	except (TypeError, NameError): # unicode is a default on python 3 
		pass

	text = unicodedata.normalize('NFD', text)
	text = text.encode('ascii', 'ignore')
	text = text.decode("utf-8")

	return str(text)

def text_to_id(text):
    """ Convert input text to id """
    text = strip_accents(text.lower())
    text = re.sub('[^0-9a-zA-Z_-]', ' ', text)

    return text

def create_dict(grad_class):
	""" Creat dictionary for each class with all students names """
	if grad_class == "m1":
		for name in m1:
			name = text_to_id(name)
			grades_m1[name] = 0
	elif grad_class == "m2":
		for name in m2:
			name = text_to_id(name)
			grades_m2[name] = 0
	elif grad_class == "m3":
		for name in m3:
			name = text_to_id(name)
			grades_m3[name] = 0
	elif grad_class == "m4":
		for name in m4:
			name = text_to_id(name)
			grades_m4[name] = 0
	else:
		print("Turma Inválida.")

def open_file(file_name, grad_class):
	""" 
	Try to open the csv file with the grades 
	Calls the parsing method
	"""
	try:
		file_name = file_name.split("/")[1]
		with open("data/" + file_name) as fp:
			file_data = fp.readlines()
			#print rows
	except IOError:
		print("O arquivo informado não é válido. Verificar caminho e nome.")
		print("O arquivo deve estar dentro do diretório data dentro da pasta do script. Informar somente o nome do arquivo.")
		exit()

	parse_file(file_data, grad_class)

def parse_file(file_data, grad_class):
	"""
	Parse the file with the grades
	Get the student name and grade
	Calls the method to save grade
	"""
	for row in file_data[1:]:
		# row[2] = nome
		# row[7] = nota
		row = row.split(";")
		name = text_to_id((str(row[2]).replace('"', '')).casefold())
		grade = round((float(row[7])/max_grade)*10, 2)

		save_grade(name, grade, grad_class)

def save_grade(name, grade, grad_class):
	"""	Save the student's grade if name is correctly informes """
	#print(name)
	#print(grade)
	if grad_class == "m1":
		if name in m1:
			grades_m1[name] = grade
	elif grad_class == "m2":
		if name in m2:
			grades_m2[name] = grade
	elif grad_class == "m3":
		if name in m3:
			grades_m3[name] = grade
	elif grad_class == "m4":
		if name in m4:
			grades_m4[name] = grade
	

def generate_grade(file_name, grad_class):
	""" 
	Main function
	Write the name and grade of all students accordingly to the class (m1, m2, m3, m4)
	"""
	global m1, m2, m3, m4

	m1 = list_to_lower_case(m1)
	m2 = list_to_lower_case(m2)
	m3 = list_to_lower_case(m3)
	m4 = list_to_lower_case(m4)

	if grad_class == "m1":
		create_dict(grad_class)
		open_file(file_name, grad_class)
		write_file = open('notas_m1.csv', 'w')
		write_file.write("AeP 2019/1 - M1\n")
		write_file.write("Nome;Nota (Lista 1 + Lista 2)\n")
		for name in grades_m1:
			write_file.write(name.title() + ";" + str(grades_m1[name]) + "\n")
			print(name.title() + ": " + str(grades_m1[name]))
	elif grad_class == "m2":
		create_dict(grad_class)
		open_file(file_name, grad_class)
		write_file = open('notas_m2.csv', 'w')
		write_file.write("AeP 2019/1 - M2\n")
		write_file.write("Nome;Nota (Lista 1 + Lista 2)\n")
		for name in grades_m2:
			write_file.write(name.title() + ";" + str(grades_m2[name]) + "\n")
			print(name.title() + ": " + str(grades_m2[name]))
	elif grad_class == "m3":
		create_dict(grad_class)
		open_file(file_name, grad_class)
		write_file = open('notas_m3.csv', 'w')
		write_file.write("AeP 2019/1 - M3\n")
		write_file.write("Nome;Nota (Lista 1 + Lista 2)\n")
		for name in grades_m3:
			write_file.write(name.title() + ";" + str(grades_m3[name]) + "\n")
			print(name.title() + ": " + str(grades_m3[name]))
	elif grad_class == "m4":
		create_dict(grad_class)
		open_file(file_name, grad_class)
		write_file = open('notas_m4.csv', 'w')
		write_file.write("AeP 2019/1 - M4\n")
		write_file.write("Nome;Nota (Lista 1 + Lista 2)\n")
		for name in grades_m4:
			write_file.write(name.title() + ";" + str(grades_m4[name]) + "\n")
			print(name.title() + ": " + str(grades_m4[name]))
	else:
		print("Turma informada inválida.")

def list_to_lower_case(list):
	""" Transform all items of a list to lower case """
	new_list = []
	for item in list:
		new_list.append(item.casefold())

	#print(new_list)
	return new_list

generate_grade(sys.argv[1], sys.argv[2])

