class Pulmao:
    def __init__(self):
        self.estaSaudavel = 100.0

    def oxigenação(self, corpo):
        if corpo.saturacao_oxigenio < 90.0:
            self.estaSaudavel -= 15.0
            print(f"[{corpo.nome}] Alerta Pulmonar: Oxigenação baixa afetando a integridade dos pulmões!")
        else:
            print(f"[{corpo.nome}] Pulmões realizando trocas gasosas adequadamente.")

    def verificarNivelOxigenio(self, corpo):
        print(f"[{corpo.nome}] Pulmão - Nível de oxigênio monitorado: {corpo.saturacao_oxigenio}%")
        return corpo.saturacao_oxigenio
