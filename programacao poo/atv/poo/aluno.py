from poo.pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self,nome):
        super().__init__(nome)

    def setTurma(self,turma):
        self.turma= turma
    
    def __str__(self):
        return super().__str__() + ' - Aluno da turma ' + self.turma