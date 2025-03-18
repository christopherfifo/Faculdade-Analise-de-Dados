from poo.pessoa import Pessoa
from poo.aluno import Aluno
from poo.endereco import Endereco

p1 = Pessoa('Maria')
p1.setIdade(2006)
p2 = Pessoa('Jose')

print(p1)
print(Pessoa.planeta)

a1 = Aluno('Pedro')
a1.setTurma('4°B')
a1.setIdade(2001)
print(a1)

end = Endereco()
end.setLogradouro('Armenia')
end.setNumero(100)
end.setBairro('Centro')
end.setCidade('São Paulo')
end.setEstado('SP')
a1.setEndereco(end)

print(a1)

print(a1.__dict__)

print(a1.endereco)