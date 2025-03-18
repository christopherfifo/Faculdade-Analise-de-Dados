class SalaDeAula:
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
        print(f"Alunos da sala {self.codigo}:")
        for aluno in self.alunos:
            print(f"- {aluno}")

    def __str__(self):
        return f"Sala {self.codigo} - Capacidade: {self.capacidade} alunos - Ocupação: {len(self.alunos)} alunos" 