class Veiculo:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.velocidade_atual = 0

    def acelerar(self, incremento):
        """Metodo para acelerar o veiculo"""
        self.velocidade_atual = min(self.velocidade_atual + incremento, self.max_speed)
        return self.velocidade_atual

    def desacelerar(self, decremento):
        """Metodo para reduzir a velocidade do veiculo"""
        self.velocidade_atual = max(self.velocidade_atual - decremento, 0)
        return self.velocidade_atual

    def __str__(self):
        return f"Veiculo: Velocidade maxima={self.max_speed}km/h, Quilometragem={self.mileage}km, Velocidade atual={self.velocidade_atual}km/h"


class Onibus(Veiculo):
    def __init__(self, max_speed, mileage, capacidade, tem_ar_condicionado=False):
        super().__init__(max_speed, mileage)
        self.capacidade = capacidade
        self.tem_ar_condicionado = tem_ar_condicionado
        self.passageiros = 0

    def embarcar(self, quantidade):
        """Metodo para embarcar passageiros"""
        if self.passageiros + quantidade <= self.capacidade:
            self.passageiros += quantidade
            return f"Embarcaram {quantidade} passageiros. Total: {self.passageiros}"
        return f"Capacidade excedida! So ha {self.capacidade - self.passageiros} vagas."

    def desembarcar(self, quantidade):
        """Metodo para desembarcar passageiros"""
        self.passageiros = max(self.passageiros - quantidade, 0)
        return f"Desembarcaram {quantidade} passageiros. Total: {self.passageiros}"

    def __str__(self):
        ar = "com" if self.tem_ar_condicionado else "sem"
        return f"onibus ({ar} ar-condicionado): Capacidade={self.capacidade}, Passageiros={self.passageiros}, {super().__str__()}"


class Carro(Veiculo):
    modelo = "Carro esportivo"  # Atributo de classe

    def __init__(self, max_speed, mileage, cor, marca="Generica"):
        super().__init__(max_speed, mileage)
        self.cor = cor
        self.marca = marca
        self.portas_trancadas = True

    @classmethod
    def descricao_geral(cls):

        """Metodo de classe que retorna uma descricao geral dos carros.
        Justificativa: Útil para obter informacões sobre a classe em geral,
        assim possibilitando ter a noção inicial do sera trbalhada nessa classe."""

        return f"{cls.modelo}, Veiculo motorizado para alta performance nas pistas."

    @staticmethod
    def combustivel_recomendado(ano):

        """Metodo estatico que recomenda o tipo de combustivel baseado no ano.
        Justificativa: Nao depende do estado da instância e pode ser usado
        independentemente de ter um objeto criado, sendo util para verificar o tipo de alimentação utilizada pelo veiculo de acordo com o seu ano."""

        if ano < 2010:
            return "Gasolina"
        elif 2010 <= ano < 2020:
            return "Flex (Gasolina/alcool)"
        else:
            return "Flex ou Eletrico"

    def trancar_portas(self):
        """Tranca as portas do carro"""
        self.portas_trancadas = True
        return "Portas trancadas"

    def destrancar_portas(self):
        """Destranca as portas do carro"""
        self.portas_trancadas = False
        return "Portas destrancadas"

    def __str__(self):
        return f"Carro {self.marca}: Cor={self.cor}, Portas={'trancadas' if self.portas_trancadas else 'destrancadas'}, {super().__str__()}"