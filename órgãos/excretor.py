class SistemaExcretor:
    def __init__(self):
        self.capacidade_Maxima_Urina = 500

    def esta_cheia(self):
        return self.capacidade_Maxima_Urina <= 0
