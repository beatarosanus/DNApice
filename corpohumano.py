class CorpoHumano:
    def __init__(self, nome: str):
        self.nome = nome
        self.ph = 7.4
        self.saturacao_oxigenio = 98.0
        self.pressao_arterial = 120.0
        self.hidratacao = 100.0
        self.volume_sanguineo = 5.0
        self.temperatura_corpo = 36.5
        self.bioma_atual = None  

def suar(self):
        if self.bioma_atual == "deserto":
            try:
                temp = float(input("Informe a temperatura atual: "))
                
                if temp >= 50.0:
                    self.temperatura_corpo = 40.0
                    self.hidratacao -= 25.0
                    self.pressao_arterial = 90.0
                    print(f"[{self.nome}] Calor extremo no Deserto! Temperatura corporal: {self.temperatura_corpo}°C | Pressão: {self.pressao_arterial}. O corpo sua para resfriar e a pressão caiu por desidratação. TOME CUIDADO!")
                    
                elif temp >= 40.0:
                    self.temperatura_corpo = 38.5
                    self.hidratacao -= 12.0  
                    self.pressao_arterial = 105.0
                    print(f"[{self.nome}] Calor forte! Temperatura corporal: {self.temperatura_corpo}°C | Pressão: {self.pressao_arterial}. O corpo está a suar intensamente.")
                    
            except ValueError:
                print("Erro: Por favor, insere um número válido para a temperatura (ex: 42.5).")
            
            
        elif self.bioma_atual in ["tundra", "taiga"]:
            self.temperatura_corpo = 35.0
            self.pressao_arterial = 140.0
            self.volume_sanguineo = 5.2
            self.hidratacao -= 5.0
            print(f"[{self.nome}] Frio extremo na {self.bioma_atual}! Vasoconstrição ativada.")
        
        else:
            print(f"[{self.nome}] Sem bioma definido. Corpo estável.")

        print(f"Status -> Temp: {self.temperatura_corpo}°C | Hidratação: {self.hidratacao}%\n")
        
        else:
            print(f"[{self.nome}] Sem bioma definido. Corpo estável.")

        print(f"Status -> Temp: {self.temperatura_corpo}°C | Hidratação: {self.hidratacao}%\n")
        
        

