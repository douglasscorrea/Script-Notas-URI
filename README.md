
# Script para cálculo de notas para listas do URI

O script calcula a nota de cada aluno para cada lista de exercício feitaspelo site [URI Online Judge](https://www.urionlinejudge.com.br/).

#  Pré-requisitos
Os arquivos com a avaliação dos alunos para cada lista pode ser exportada diretamente pelo site [https://www.urionlinejudge.com.br/academic/pt/login] entrando nas listas desejadas e clicando em **EXPORTAR CSV**.
As listas devem ser colocadas na pasta **data** dentro da pasta do script e nomeadas no seguinte padrão:
```
lista_1.csv
lista_2.csv
...
lista_n.csv
```
# Como utilizar
Para melhor entendimento o script foi separado em 3 arquivos: **main.py**, **generate_grades.py** e **students.py**.
O arquivo **main.py** é responsável por verificar os argumentos colocados na linha de comando e por rodar o script para gerar as notas. 
O arquivo **generate_grades.py** contem as funções utilizadas para gerar as notas. 
O arquivo **students.py** contem a lista de turmas com os respectivos alunos para verificação de nome feita pelo script.

## Como rodar o script
O script necessita do *python* na versão 3 para ser utilizado. Para rodar, executar o seguinte comando:
``` 
python3 main.py <arg>
```

## Parâmetros aceitos
O argumento **arg** corresponde a qual turma terá a nota gerada. Os seguintes argumentos são aceitos:

 - m1: gerar as notas para a turma m1
 - m2: gerar as notas para a turma m2
 - m3: gerar as notas para a turma m3
 - m4: gerar as notas para a turma m4
 - all: gerar as notas para todas as turmas
 - -help: mostra instruções de uso

Cada turma será as notas gravadas no arquivo *grades_turma.csv* na mesma pasta do script.