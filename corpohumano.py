class CorpoHumano:
    def __init__(self, nome: str):
        self.nome = nome
        self.ph = 7.4
        self.saturacao_oxigenio = 98.0
        self.pressao_arterial = 120.0
        self.hidratação = 100.0
        self.volume_sanguineo = 5.0
        self.temperatura_corpo = 36.5

    def bioma_atual(self, bioma_atual):
        if bioma == "deserto":
            print(f"\n[{self.nome}] Entrou no Deserto (Calor)")
            self.temperatura_corpo = 39.0  
            self.hidratação -= 25.0        
            self.pressao_arterial -= 10.0  
            
        elif bioma in ["tundra", "taiga"]:
            print(f"\n[{self.nome}] Entrou no bioma {bioma} - (Frio Extremo!)")
            self.temperatura_corpo = 35.0 
            self.pressao_arterial = 140.0  #vasoconstrição
            self.volume_sanguineo = 5.2    
            self.hidratação -= 5.0        
            self.saturacao_oxigenio = 99.0 
            
        print(f"-> Temperatura: {self.temperatura_corpo}°C")
        print(f"-> Pressão Arterial: {self.pressao_arterial} mmHg")
        print(f"-> Hidratação: {self.hidratação}%")
        print(f"-> Volume Sanguíneo: {self.volume_sanguineo}L")
        print(f"-> Saturação de O2: {self.saturacao_oxigenio}%")
        
        

