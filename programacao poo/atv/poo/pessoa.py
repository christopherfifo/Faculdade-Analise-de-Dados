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