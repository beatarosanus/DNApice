from pulmao import Pulmao
from rins import Rins
from excretor import SistemaExcretor

class CorpoHumano:
    def __init__(self, nome):
        self.nome = nome
        self.ph = 7.4
        self.saturacao_oxigenio = 98.0
        self.pressao_arterial = 120.0
        self.hidratacao = 100.0
        self.volume_sanguineo = 5.0
        self.temperatura_corpo = 36.5
        self.bioma_atual = None
        self.temperatura_ambiente = None
        self.periodo = None
        self.volume_ml = None
        self.concentracao = None
        self.pulmao = Pulmao()
        self.rins = Rins()
        self.sistema_excretor = SistemaExcretor()

    def mostrar_status(self):
        if self.hidratacao < 0.0:
            self.hidratacao = 0.0
        if self.hidratacao > 100.0:
            self.hidratacao = 100.0

        if self.saturacao_oxigenio < 0.0:
            self.saturacao_oxigenio = 0.0
        if self.saturacao_oxigenio > 100.0:
            self.saturacao_oxigenio = 100.0

        print(f"Status -> Temp: {self.temperatura_corpo}°C | Hidratação: {self.hidratacao}% | Pressão: {self.pressao_arterial} | O2: {self.saturacao_oxigenio}%")

    def suar(self, esforco=False):
        temp = self.temperatura_ambiente

        if self.bioma_atual == "deserto":
            if temp >= 50.0:
                self.hidratacao -= 25.0
                if self.temperatura_corpo < 40.0:
                    self.temperatura_corpo = 40.0
                if self.pressao_arterial > 90.0:
                    self.pressao_arterial = 90.0
                print(f"[{self.nome}] Calor extremo no Deserto! O corpo sua para resfriar.")
            elif temp >= 40.0:
                self.hidratacao -= 12.0
                if self.temperatura_corpo < 38.5:
                    self.temperatura_corpo = 38.5
                if self.pressao_arterial > 105.0:
                    self.pressao_arterial = 105.0
                print(f"[{self.nome}] Calor forte! O corpo está suando muito.")
            elif temp >= 30.0:
                self.hidratacao -= 5.0
                if self.temperatura_corpo < 37.2:
                    self.temperatura_corpo = 37.2
                print(f"[{self.nome}] Calor normal. O corpo sua um pouquinho.")
            else:
                self.hidratacao -= 2.0
                print(f"[{self.nome}] Clima suave no deserto. Suor leve.")
            
            if esforco == True:
                self.hidratacao -= 5.0
                print("O esforço da corrida aumentou o suor.")

        elif self.bioma_atual == "tundra" or self.bioma_atual == "taiga":
            if esforco == True:
                self.hidratacao -= 5.0
            else:
                self.hidratacao -= 2.0
            print(f"[{self.nome}] O esforço faz o corpo suar um pouco, mesmo no frio.")
        else:
            print(f"[{self.nome}] Sem bioma definido. Corpo estável.")

        self.mostrar_status()

    def urinar(self):
        self.rins.filtrarSangue(self)

        temp = self.temperatura_ambiente

        if self.bioma_atual == "deserto":
            if self.hidratacao < 75.0:
                self.volume_ml = 0.0
                print(f"[{self.nome}] CUIDADO! Hidratação em {self.hidratacao}% (abaixo de 75%).")
                print("STATUS: Impossível urinar! Anúria: o corpo bloqueou a excreção.")
                self.sistema_excretor.esta_cheia(self)
                self.mostrar_status()
                return

            if temp >= 50.0:
                self.hidratacao -= 25.0
                self.volume_ml = 50.0
                self.concentracao = "Concentrada"
            elif temp >= 40.0:
                self.hidratacao -= 12.0
                self.volume_ml = 150.0
                self.concentracao = "Moderada"
            elif temp >= 30.0:
                self.hidratacao -= 5.0
                self.volume_ml = 300.0
                self.concentracao = "Diluída"
            else:
                self.hidratacao -= 2.0
                self.volume_ml = 200.0
                self.concentracao = "Normal"

            print(f"STATUS: Você urinou cerca de {self.volume_ml}ml --- Concentração: {self.concentracao}")

        elif self.bioma_atual == "tundra" or self.bioma_atual == "taiga":
            if temp <= -30.0:
                self.hidratacao -= 20.0
                self.volume_ml = 400.0
                self.concentracao = "Muito Diluída"
            elif temp <= -15.0:
                self.hidratacao -= 12.0
                self.volume_ml = 300.0
                self.concentracao = "Diluída"
            elif temp <= 0.0:
                self.hidratacao -= 6.0
                self.volume_ml = 200.0
                self.concentracao = "Normal"
            else:
                self.hidratacao -= 3.0
                self.volume_ml = 150.0
                self.concentracao = "Moderada"

            print(f"STATUS: Você urinou cerca de {self.volume_ml}ml --- Concentração: {self.concentracao}")

        else:
            print(f"[{self.nome}] Sem bioma definido.")

        self.sistema_excretor.esta_cheia(self)
        self.mostrar_status()

    def correr(self):
        temp = self.temperatura_ambiente

        if self.bioma_atual == "deserto":
            if temp >= 45.0:
                self.temperatura_corpo += 2.5
                self.saturacao_oxigenio -= 5.0
                self.pressao_arterial -= 20.0
                print(f"[{self.nome}] CORRIDA EXTREMA NO CALOR! Exaustão térmica iminente.")
            elif temp >= 30.0:
                self.temperatura_corpo += 1.5
                self.saturacao_oxigenio -= 3.0
                self.pressao_arterial -= 10.0
                print(f"[{self.nome}] Corrida intensa sob sol forte.")
            else:
                self.temperatura_corpo += 0.8
                self.saturacao_oxigenio -= 1.0
                print(f"[{self.nome}] Corrida no deserto com temperatura amena.")

        elif self.bioma_atual == "tundra":
            if temp <= -20.0:
                self.temperatura_corpo += 0.5
                self.saturacao_oxigenio -= 2.0
                self.pressao_arterial += 15.0
                print(f"[{self.nome}] Corrida MUITO GELADA! Ar frio machucando os pulmões.")
            else:
                self.temperatura_corpo += 0.3
                print(f"[{self.nome}] Corrida na Tundra com frio tranquilo.")

        elif self.bioma_atual == "taiga":
            if temp <= -10.0:
                self.temperatura_corpo += 0.4
                self.saturacao_oxigenio -= 1.0
                self.pressao_arterial += 10.0
                print(f"[{self.nome}] Corrida na Taiga muito fria.")
            else:
                self.temperatura_corpo += 0.3
                print(f"[{self.nome}] Corrida na Taiga com clima normal.")

        else:
            print(f"[{self.nome}] Nenhum bioma definido para a corrida.")
            return
        self.pulmao.verificarNivelOxigenio(self)
        self.pulmao.oxigenação(self)

        print("Após a corrida, o corpo começa a suar...")
        self.suar(esforco=True)
