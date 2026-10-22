class Rins:
    def __init__(self):
        self.filtracao = True

    def filtrarSangue(self, corpo):
        if corpo.hidratacao < 75.0:
            self.filtracao = False
            print(f"[{corpo.nome}] Rins: Hidratação abaixo de 75%. Filtração reduzida (retenção de líquidos).")
        else:
            self.filtracao = True
            print(f"[{corpo.nome}] Rins: Sangue filtrado com sucesso.")
        return self.filtracao
