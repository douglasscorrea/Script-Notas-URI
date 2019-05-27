# -*- coding: utf-8 -*-
import os
import re
import csv
import students
import unicodedata

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
		for name in students.m1:
			name = text_to_id(name)
			grades_m1[name] = []
	elif grad_class == "m2":
		for name in students.m2:
			name = text_to_id(name)
			grades_m2[name] = []
	elif grad_class == "m3":
		for name in students.m3:
			name = text_to_id(name)
			grades_m3[name] = []
	elif grad_class == "m4":
		for name in students.m4:
			name = text_to_id(name)
			grades_m4[name] = []
	else:
		print("Turma Inválida.")


def open_file(grad_class):
	""" 
	Try to open the csv file with the grades 
	Calls the parsing method
	"""
	try:
		number_files = next(os.walk("data"))[2]

		for i in range(1, len(number_files)):
			with open("data/lista_" + str(i) + ".csv") as fp:
				file_data = fp.readlines()
				parse_file(file_data, grad_class)
			fp.close()
	except IOError:
		print("O arquivo informado não é válido. Verificar caminho e nome.")
		print("O arquivo deve estar dentro do diretório data dentro da pasta do script. Informar somente o nome do arquivo.")
		exit()


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
		grade = round((float(row[7])/float(row[8]))*10, 2)

		save_grade(name, grade, grad_class)


def save_grade(name, grade, grad_class):
	"""	Save the student's grades if name is correctly informes """
	#print(name)
	#print(grade)
	if grad_class == "m1":
		if name in students.m1:
			grades_m1[name].append(grade)
	elif grad_class == "m2":
		if name in students.m2:
			grades_m2[name].append(grade)
	elif grad_class == "m3":
		if name in students.m3:
			grades_m3[name].append(grade)
	elif grad_class == "m4":
		if name in students.m4:
			grades_m4[name].append(grade)


def calculate_average(grad_class):
	""" 
	Calculates grade's average
	"""
	if grad_class == "m1":
		for name in grades_m1:
			if len(grades_m1[name]) > 0:
				grades_m1[name].append(round(sum(grades_m1[name])/len(grades_m1[name]), 2))
	elif grad_class == "m2":
		for name in grades_m2:
			if len(grades_m2[name]) > 0:
				grades_m2[name].append(round(sum(grades_m2[name])/len(grades_m2[name]), 2))
	elif grad_class == "m3":
		for name in grades_m3:
			if len(grades_m3[name]) > 0:
				grades_m3[name].append(round(sum(grades_m3[name])/len(grades_m3[name]), 2))
	elif grad_class == "m4":
		for name in grades_m4:
			if len(grades_m4[name]) > 0:
				grades_m4[name].append(round(sum(grades_m4[name])/len(grades_m4[name]), 2))


def write_grades_to_csv(grad_class):
	""" Write all the grades in the corresponding csv file. """
	number_files = next(os.walk("data"))[2]

	write_file = open("grades_" + grad_class + ".csv", 'w')
	write_file.write("AeP 2019/1 - " + grad_class + ";Notas\n")
	write_file.write("Nome;")
	for i in range(1, len(number_files)):
		write_file.write("Lista " + str(i) + ";")
	write_file.write("Media\n")

	if grad_class == "m1":
		print("------- Notas M1 -------")
		for name in grades_m1:
			print(name.title() + ": " + str(grades_m1[name]))
			write_file.write(name.title() + ";" + str(grades_m1[name])[1:-1].replace(", ", ";") + "\n")
	elif grad_class == "m2":
		print("------- Notas M2 -------")
		for name in grades_m2:
			print(name.title() + ": " + str(grades_m2[name]))
			write_file.write(name.title() + ";" + str(grades_m2[name])[1:-1].replace(", ", ";") + "\n")
	elif grad_class == "m3":
		print("------- Notas M3 -------")
		for name in grades_m3:
			print(name.title() + ": " + str(grades_m3[name]))
			write_file.write(name.title() + ";" + str(grades_m3[name])[1:-1].replace(", ", ";") + "\n")
	elif grad_class == "m4":
		print("------- Notas M4 -------")
		for name in grades_m4:
			print(name.title() + ": " + str(grades_m4[name]))
			write_file.write(name.title() + ";" + str(grades_m4[name])[1:-1].replace(", ", ";") + "\n")


def generate_grade(grad_class):
	""" 
	Write the name and grade of all students accordingly to the class 
	(m1, m2, m3, m4, all) 
	"""
	students.m1 = list_to_lower_case(students.m1)
	students.m2 = list_to_lower_case(students.m2)
	students.m3 = list_to_lower_case(students.m3)
	students.m4 = list_to_lower_case(students.m4)
		
	if grad_class == "all":
		generate_grade("m1")
		generate_grade("m2")
		generate_grade("m3")
		generate_grade("m4")
	else:
		create_dict(grad_class)
		open_file(grad_class)
		calculate_average(grad_class)
		write_grades_to_csv(grad_class)


def list_to_lower_case(list):
	""" Transform all items of a list to lower case """
	new_list = []
	for item in list:
		new_list.append(item.casefold())

	#print(new_list)
	return new_list

