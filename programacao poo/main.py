from poo.pessoa import Pessoa
from poo.aluno import Aluno

p1 = Pessoa('Maria')
p1.setIdade(2006)
p2 = Pessoa('Jose')

print(p1)
print(Pessoa.planeta)

a1 = Aluno('Pedro')
a1.setTurma('4°B')
a1.setIdade(2001)
print(a1)