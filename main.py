import sys
import generate_grades as gg

if len(sys.argv) == 1:
	print("Para gerar as notas utilizar os seguintes formatos:")
	print("\t python3 script.py <turma>")
	print("\t Para gerar notas de todas as turmas usar o argumento \"all\"")
	exit();
elif sys.argv[1] == "-help":
	print("Para gerar as notas utilizar os seguintes formatos:")
	print("\t python3 script.py <turma>")
	print("\t Para gerar as notas de todas as turmas usar o argumento \"all\"")
	exit();
elif len(sys.argv) == 2 and sys.argv[1] in ("m1", "m2", "m3", "m4", "all"):
	gg.generate_grade(sys.argv[1])
else:
	print("Argumentos invalidos. Utilizar os seguintes formatos:")
	print("\t python3 script.py <turma>")
	print("\t Para gerar notas de todas as turmas usar o argumento \"all\"")
	exit();