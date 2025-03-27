from poo.functions import *
from poo.classes import *

# 1. Produto ou soma
print(produto_ou_soma(50, 20))  
print(produto_ou_soma(30, 50))  
print(f"\n")

# 2. Remover caracteres
print(remover_caracteres("abcdef", 2)) 
print(f"\n")

# 3. Contar substrings
print(contar_substrings("banana", "ana"))  
print(f"\n")

# 4. Soma de 1 até k
print(soma_1_a_k(5)) 
print(f"\n")

# 5. Números primos
print(numeros_primos(10, 50)) 
print(f"\n")

# 6. Padrao invertido
padrao_invertido()
print(f"\n")

# 7. Soma variada
resultado = soma_variavel([1, 2, 3, 4])
print(resultado)  
print(f"\n")

# 8. Calculo de adicao e subtracao
adicao, subtracao = calculation(10, 5)
print(f"Adicao: {adicao}, Subtracao: {subtracao}")
print(f"\n")

# 9. Soma recursiva
print(soma_recursiva(5))  
print(f"\n")

# 10. Soma do maior e menor número da lista
print(soma_maior_menor([1, 2, 3, 4, 5])) 
print(f"\n")

# 11. Classe Veiculo
veiculo = Veiculo(120, 10000)
print("\n--- Teste da classe Veiculo ---")
print(veiculo)
veiculo.acelerar(50)
print("Acelerando:", veiculo)
veiculo.desacelerar(20)
print("Desacelerando:", veiculo)

# 12. Classe Ônibus
onibus = Onibus(80, 50000, 50, tem_ar_condicionado=True)
print("\n--- Teste da classe Onibus ---")
print(onibus)
print(onibus.embarcar(30))
print(onibus.embarcar(25))  # Deve exceder a capacidade
print(onibus.desembarcar(10))
print(onibus)

# 13. Classe Carro e polimorfismo
carro = Carro(180, 30000, "Vermelho", "Ferrari")
print("\n--- Teste da classe Carro ---")
print(carro)
print("Trancando portas:", carro.trancar_portas())
print("Combustivel recomendado para 2015:", Carro.combustivel_recomendado(2015))
print("Descricao geral:", Carro.descricao_geral())

# 13. Testando polimorfismo
print("\n--- Teste de polimorfismo ---")
veiculos = [
    Veiculo(150, 20000),
    Onibus(90, 100000, 60),
    Carro(200, 5000, "Azul", "BMW"),
    Onibus(85, 80000, 40),
    Carro(220, 10000, "Preto", "Tesla")
]

for veiculo in veiculos:
    # O polimorfismo permite chamar o mesmo método para diferentes classes
    print(f"\nTipo do objeto: {veiculo.__class__.__name__}")
    print(veiculo)
    veiculo.acelerar(30)
    print(f"Acelerando: Velocidade atual = {veiculo.velocidade_atual}km/h")
