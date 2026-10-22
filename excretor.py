class SistemaExcretor:
    def __init__(self, capacidade_maxima_urina=400.0):
        self.capacidadeMaximaUrina = capacidade_maxima_urina

    def esta_cheia(self, corpo):
        if corpo.volume_ml >= self.capacidadeMaximaUrina:
            print(f"[{corpo.nome}] Sistema Excretor: Bexiga cheia! Capacidade máxima de {self.capacidadeMaximaUrina}ml atingida.")
            return True
        else:
            print(f"[{corpo.nome}] Sistema Excretor: Volume urinário dentro do limite da capacidade.")
            return False
