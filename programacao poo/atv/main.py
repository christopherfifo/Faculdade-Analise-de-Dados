from poo.pessoa import Pessoa
from poo.aluno import Aluno
from poo.sala_de_aula import SalaDeAula

sala = SalaDeAula("2024.1A", 30)

nomes_idades = [("João", 2005), ("Maria", 2004), ("Pedro", 2005)]

for nome, ano in nomes_idades:
    aluno = Aluno(nome)
    aluno.setIdade(ano)
    sala.adicionar_aluno(aluno)

professor = Pessoa("Dr. Silva")
professor.setIdade(1980)
sala.definir_professor(professor)

print(sala)
print("\nProfessor:", professor)
sala.listar_alunos()