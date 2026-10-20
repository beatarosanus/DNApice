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
        self.volume_ml = None
        self.concentracao = None

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

                elif temp >= 30.0:
                    self.temperatura_corpo = 37.2
                    self.hidratacao -= 5.0
                    self.pressao_arterial = 120.0
                    print(f"[{self.nome}] Calor forte! Temperatura corporal: {self.temperatura_corpo}°C | Pressão: {self.pressao_arterial}")

                else:
                    self.temperatura_corpo = 36.5
                    self.hidratacao -= 2.0
                    self.pressao_arterial = 120.
                    print(f"[{self.nome}] Clima ameno. Corpo estável.")

            except ValueError:
                print("Erro: Por favor, insira um número válido para a temperatura (ex: 42.5).")
            
            
        elif self.bioma_atual == "tundra" or self.bioma_atual == "taiga":
            self.temperatura_corpo = 35.0
            self.pressao_arterial = 140.0
            self.volume_sanguineo = 5.2
            self.hidratacao -= 5.0
            print(f"[{self.nome}] Frio extremo na {self.bioma_atual}! Vasoconstrição ativada.")
        
        else:
            print(f"[{self.nome}] Sem bioma definido. Corpo estável.")

        print(f"Status -> Temp: {self.temperatura_corpo}°C | Hidratação: {self.hidratacao}%\n")

def urinar(self):
    if self.bioma_atual == "deserto":
        try:
            base = (input("Informe a tempeperatura atual do deserto (°C):"))
            if base >= 30.0:
               self.hidratacao -= 05.0
               self.volume_ml = 300.0
               self.concentracao = "Diluída"
               print(f"[{self.nome}], sua hidratação está moderada")
               print(f"STATUS: Voce urinou cerca de {self.volume_ml}ml --- Sua concentração: {self.concentracao} ")
            elif base >= 40.0:
                 self.hidratacao -= 12.0:
                 self.volume_ml = 150.0
                 self.concentracao = "Moderada"
                 print(f"[{self.nome}],Atenção: Hidratação baixa. Urina muito concentrada. ")
                 print(f"STATUS:Voce urinou cerca de {self.volume.ml}ml --- Sua concentração: {self.concentracao}")
            elif base >= 50.0:
                self.hidratacao -= 25.0
                self.volume_ml = 50.0
                self.concentracao = "Concentrada"
                print(f"[{self.nome}] Hidratação crítica! Rins em retenção máxima.")
                print(f"STATUS(FIQUE ATENTO!!!) Voce urinou cerca de {self.volume_ml}ml --- Sua concentração: {self.concetracao}")
            if self.hidracao < 74.0:
                self.volume_ml = 0.0
                print(f"[{self.nome}] CUIDADO! Hidratação em {self.hidratacao}% (abaixo de 75%).")
                print("STATUS: Impossível urinar! Voce está passando por uma supressão da produção de urina(anúria) devido ao calor intenso e falta de hidratação. O corpo bloqueou a excreção para reter cada gota de água.")
            else:
                self.volume_ml = 200.0
                self.concentracao = "Normal"
                print(f"[{self.nome}], sua hidratação está estável.")
                print(f"STATUS: Voce urinou cerca de {self.concentracao_ml}ml --- Sua concentracao: {self.concentracao}")


    elif self.bioma_atual == "tundra":
         base = float(input("Informe a temperatura atual da Tundra (°C): "))
        
        if base <= -30.0:
            self.hidratacao -= 20.0
            self.volume_ml = 400.0
            self.concentracao = "Muito Diluída"
            print(f"[{self.nome}] Frio congelante extremo! Vasoconstrição intensa nos vasos.")
            print(f"STATUS: Você urinou cerca de {self.volume_ml}ml --- Sua concentração: {self.concentracao}")
            
        elif base <= -15.0:
            self.hidratacao -= 12.0
            self.volume_ml = 300.0
            self.concentracao = "Diluída"
            print(f"[{self.nome}], o frio severo está a acelerar a filtragem renal.")
            print(f"STATUS: Você urinou cerca de {self.volume_ml}ml --- Sua concentração: {self.concentracao}")
            
        elif base <= 0.0:
            self.hidratacao -= 6.0
            self.volume_ml = 200.0
            self.concentracao = "Normal"
            print(f"[{self.nome}], temperatura abaixo de zero. Metabolismo adaptado ao frio.")
            print(f"STATUS: Você urinou cerca de {self.volume_ml}ml --- Sua concentração: {self.concentracao}")
            
        else:
            self.hidratacao -= 3.0
            self.volume_ml = 150.0
            self.concentracao = "Moderada"
            print(f"[{self.nome}], tundra levemente mais amena (perto de 10°C).")
            print(f"STATUS: Você urinou cerca de {self.volume_ml}ml --- Sua concentração: {self.concentracao}")
    

    elif self.bioma_atual == "Tundra":
    base = float(input("Informe a temperatura atual da Tundra (°C): "))

    if base <= -30.0:
        self.hidratacao -= 20.0
        self.volume_ml = 400.0
        self.concentracao = "Muito Diluída"
        print(f"[{self.nome}] Frio congelante extremo! Vasoconstrição intensa nos vasos.")
        print(f"STATUS: Você urinou cerca de {self.volume_ml}ml --- Sua concentração: {self.concentracao}")

    elif base <= -15.0:
        self.hidratacao -= 12.0
        self.volume_ml = 300.0
        self.concentracao = "Diluída"
        print(f"[{self.nome}], o frio severo está a acelerar a filtragem renal.")
        print(f"STATUS: Você urinou cerca de {self.volume_ml}ml --- Sua concentração: {self.concentracao}")

    elif base <= 0.0:
        self.hidratacao -= 6.0
        self.volume_ml = 200.0
        self.concentracao = "Normal"
        print(f"[{self.nome}], temperatura abaixo de zero. Metabolismo adaptado ao frio.")
        print(f"STATUS: Você urinou cerca de {self.volume_ml}ml --- Sua concentração: {self.concentracao}")

    else:
        self.hidratacao -= 3.0
        self.volume_ml = 150.0
        self.concentracao = "Moderada"
        print(f"[{self.nome}], tundra levemente mais amena (perto de 10°C).")
        print(f"STATUS: Você urinou cerca de {self.volume_ml}ml --- Sua concentração: {self.concentracao}")
            

        print(f"Status -> Temp: {self.temperatura_corpo}°C | Hidratação: {self.hidratacao}%\n")
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
        self.volume_ml = None
        self.concentracao = None

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

                elif temp >= 30.0:
                    self.temperatura_corpo = 37.2
                    self.hidratacao -= 5.0
                    self.pressao_arterial = 120.0
                    print(f"[{self.nome}] Calor forte! Temperatura corporal: {self.temperatura_corpo}°C | Pressão: {self.pressao_arterial}")

                else:
                    self.temperatura_corpo = 36.5
                    self.hidratacao -= 2.0
                    self.pressao_arterial = 120.
                    print(f"[{self.nome}] Clima ameno. Corpo estável.")

            except ValueError:
                print("Erro: Por favor, insira um número válido para a temperatura (ex: 42.5).")
            
            
        elif self.bioma_atual == "tundra" or self.bioma_atual == "taiga":
            self.temperatura_corpo = 35.0
            self.pressao_arterial = 140.0
            self.volume_sanguineo = 5.2
            self.hidratacao -= 5.0
            print(f"[{self.nome}] Frio extremo na {self.bioma_atual}! Vasoconstrição ativada.")
        
        else:
            print(f"[{self.nome}] Sem bioma definido. Corpo estável.")

        print(f"Status -> Temp: {self.temperatura_corpo}°C | Hidratação: {self.hidratacao}%\n")

def urinar(self):
    if self.bioma_atual == "deserto":
        try:
            base = (input("Informe a tempeperatura atual do deserto (°C):"))
            if base >= 30.0:
               self.hidratacao -= 05.0
               self.volume_ml = 300.0
               self.concentracao = "Diluída"
               print(f"[{self.nome}], sua hidratação está moderada")
               print(f"STATUS: Voce urinou cerca de {self.volume_ml}ml --- Sua concentração: {self.concentracao} ")
            elif base >= 40.0:
                 self.hidratacao -= 12.0:
                 self.volume_ml = 150.0
                 self.concentracao = "Moderada"
                 print(f"[{self.nome}],Atenção: Hidratação baixa. Urina muito concentrada. ")
                 print(f"STATUS:Voce urinou cerca de {self.volume.ml}ml --- Sua concentração: {self.concentracao}")
            elif base >= 50.0:
                self.hidratacao -= 25.0
                self.volume_ml = 50.0
                self.concentracao = "Concentrada"
                print(f"[{self.nome}] Hidratação crítica! Rins em retenção máxima.")
                print(f"STATUS(FIQUE ATENTO!!!) Voce urinou cerca de {self.volume_ml}ml --- Sua concentração: {self.concetracao}")
            if self.hidracao < 74.0:
                self.volume_ml = 0.0
                print(f"[{self.nome}] CUIDADO! Hidratação em {self.hidratacao}% (abaixo de 75%).")
                print("STATUS: Impossível urinar! Voce está passando por uma supressão da produção de urina(anúria) devido ao calor intenso e falta de hidratação. O corpo bloqueou a excreção para reter cada gota de água.")
            else:
                self.volume_ml = 200.0
                self.concentracao = "Normal"
                print(f"[{self.nome}], sua hidratação está estável.")
                print(f"STATUS: Voce urinou cerca de {self.concentracao_ml}ml --- Sua concentracao: {self.concentracao}")


    elif self.bioma_atual == "tundra":
         base = float(input("Informe a temperatura atual da Tundra (°C): "))
        
        if base <= -30.0:
            self.hidratacao -= 20.0
            self.volume_ml = 400.0
            self.concentracao = "Muito Diluída"
            print(f"[{self.nome}] Frio congelante extremo! Vasoconstrição intensa nos vasos.")
            print(f"STATUS: Você urinou cerca de {self.volume_ml}ml --- Sua concentração: {self.concentracao}")
            
        elif base <= -15.0:
            self.hidratacao -= 12.0
            self.volume_ml = 300.0
            self.concentracao = "Diluída"
            print(f"[{self.nome}], o frio severo está a acelerar a filtragem renal.")
            print(f"STATUS: Você urinou cerca de {self.volume_ml}ml --- Sua concentração: {self.concentracao}")
            
        elif base <= 0.0:
            self.hidratacao -= 6.0
            self.volume_ml = 200.0
            self.concentracao = "Normal"
            print(f"[{self.nome}], temperatura abaixo de zero. Metabolismo adaptado ao frio.")
            print(f"STATUS: Você urinou cerca de {self.volume_ml}ml --- Sua concentração: {self.concentracao}")
            
        else:
            self.hidratacao -= 3.0
            self.volume_ml = 150.0
            self.concentracao = "Moderada"
            print(f"[{self.nome}], tundra levemente mais amena (perto de 10°C).")
            print(f"STATUS: Você urinou cerca de {self.volume_ml}ml --- Sua concentração: {self.concentracao}")
    

    elif self.bioma_atual == "Tundra":
    base = float(input("Informe a temperatura atual da Tundra (°C): "))

    if base <= -30.0:
        self.hidratacao -= 20.0
        self.volume_ml = 400.0
        self.concentracao = "Muito Diluída"
        print(f"[{self.nome}] Frio congelante extremo! Vasoconstrição intensa nos vasos.")
        print(f"STATUS: Você urinou cerca de {self.volume_ml}ml --- Sua concentração: {self.concentracao}")

    elif base <= -15.0:
        self.hidratacao -= 12.0
        self.volume_ml = 300.0
        self.concentracao = "Diluída"
        print(f"[{self.nome}], o frio severo está a acelerar a filtragem renal.")
        print(f"STATUS: Você urinou cerca de {self.volume_ml}ml --- Sua concentração: {self.concentracao}")

    elif base <= 0.0:
        self.hidratacao -= 6.0
        self.volume_ml = 200.0
        self.concentracao = "Normal"
        print(f"[{self.nome}], temperatura abaixo de zero. Metabolismo adaptado ao frio.")
        print(f"STATUS: Você urinou cerca de {self.volume_ml}ml --- Sua concentração: {self.concentracao}")

    else:
        self.hidratacao -= 3.0
        self.volume_ml = 150.0
        self.concentracao = "Moderada"
        print(f"[{self.nome}], tundra levemente mais amena (perto de 10°C).")
        print(f"STATUS: Você urinou cerca de {self.volume_ml}ml --- Sua concentração: {self.concentracao}")
            

        print(f"Status -> Temp: {self.temperatura_corpo}°C | Hidratação: {self.hidratacao}%\n")


        
        

