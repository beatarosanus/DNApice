class Bioma:
    def __init__(self, nome, flora, clima, fauna,
                 estacao, umidade, temperatura):

        self.nome = nome
        self.flora = flora
        self.clima = clima
        self.fauna = fauna
        self.estacao = estacao
        self.umidade = umidade
        self.temperatura = temperatura

    def efeito_termico(self, corpo):
        corpo.bioma_atual = self.nome.lower()
        corpo.temperatura_ambiente = self.temperatura

        print(f"Bioma atual: {self.nome}")
        print(f"Flora: {self.flora}")
        print(f"Clima: {self.clima}")
        print(f"Fauna: {self.fauna}")
