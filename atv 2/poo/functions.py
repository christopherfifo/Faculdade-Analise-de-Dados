def produto_ou_soma(a, b):
    produto = a * b
    if produto <= 1000:
        return produto
    else:
        return a + b

def remover_caracteres(s, n):
    return s[n:]

def contar_substrings(s, substr):
    count = 0
    len_sub = len(substr)
    for i in range(len(s) - len_sub + 1):
        if s[i:i+len_sub] == substr:
            count += 1
    return count

def soma_1_a_k(k):
    return sum(range(1, k + 1))

def numeros_primos(intervalo_inicial, intervalo_final):
    primos = []
    for num in range(intervalo_inicial, intervalo_final + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primos.append(num)
    return primos

def padrao_invertido():
    for i in range(1, 6):
        print('* ' * i)
    for i in range(4, 0, -1):
        print('* ' * i)
        
def soma_variavel(numeros):
    return sum(numeros)

def calculation(a, b):
    adicao = a + b
    subtracao = a - b
    return adicao, subtracao

def soma_recursiva(n):
    if n == 0:
        return 0
    else:
        return n + soma_recursiva(n - 1)

def soma_maior_menor(lista):
    return min(lista) + max(lista)
