class Pessoa():
    planeta = 'Terra'

    def __init__(self,nome):
        self.nome = nome

    def __str__(self):
        return 'Meu nome é ' + self.nome + ', tenho ' + str(self.idade) + ' anos'
    
    def setIdade(self, ano):
        self.idade = 2025 - ano

    def setEndereco(self, endereco):
        self.endereco = endereco

class Aluno(Pessoa):
    def __init__(self,nome):
        super().__init__(nome)

    def setTurma(self,turma):
        self.turma= turma
    
    def __str__(self):
        return super().__str__() + ' - Aluno da turma ' + self.turma

class SalaDeAula():
    def __init__(self, codigo, capacidade):
        self.codigo = codigo
        self.capacidade = capacidade
        self.alunos = []
        self.professor = None

    def adicionar_aluno(self, aluno):
        if len(self.alunos) < self.capacidade:
            self.alunos.append(aluno)
            aluno.setTurma(self.codigo)
            return True
        return False

    def definir_professor(self, professor):
        self.professor = professor

    def listar_alunos(self):
        print(f"\nAlunos da sala {self.codigo}:\n")
        for aluno in self.alunos:
            print(f"- {aluno}")

    def __str__(self):
        return f"\n\nSala {self.codigo} - Capacidade: {self.capacidade} alunos - Ocupação: {len(self.alunos)} alunos" 

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