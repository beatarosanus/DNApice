class Bioma:

    def __init__(self, nome, flora, clima, fauna, temperatura_ambiente,
                 umidade_relativa, horario=None):
        self.nome = nome
        self.flora = flora
        self.clima = clima
        self.fauna = fauna
        self.umidade_relativa = self._validar_umidade(umidade_relativa)
        self.temperatura_ambiente = float(temperatura_ambiente)
        self.estacao = self._estimar_estacao(self.temperatura_ambiente)
        self.horario = (self._estimar_horario(self.temperatura_ambiente)
                        if horario is None else self._validar_horario(horario))

    @staticmethod
    def _validar_umidade(valor):
        valor = float(valor)
        if not 0 <= valor <= 100:
            raise ValueError("A umidade deve estar entre 0 e 100%.")
        return valor

    @staticmethod
    def _validar_horario(valor):
        valor = float(valor)
        if not 0 <= valor < 24:
            raise ValueError("O horário deve estar entre 0 e 24.")
        return valor

    @staticmethod
    def _estimar_estacao(temp):
        if temp <= 10:
            return "Inverno"
        if temp <= 18:
            return "Outono"
        if temp <= 25:
            return "Primavera"
        return "Verão"

    @staticmethod
    def _estimar_horario(temp):
        if temp <= 10:
            return 4.0
        if temp <= 20:
            return 9.0
        if temp <= 30:
            return 16.0
        return 12.0

    def atualizar_temperatura(self, temperatura, horario=None):
        self.temperatura_ambiente = float(temperatura)
        self.estacao = self._estimar_estacao(self.temperatura_ambiente)
        self.horario = (self._estimar_horario(self.temperatura_ambiente)
                        if horario is None else self._validar_horario(horario))

    def umidade(self):
        return self.umidade_relativa

    def temperatura(self):
        return self.temperatura_ambiente

    @property
    def momento_do_dia(self):
        if self.horario < 6 or self.horario >= 19:
            return "Madrugada/noite"
        if self.horario < 12:
            return "Manhã"
        if self.horario < 18:
            return "Tarde"
        return "Noite"

    @property
    def horário(self):
        return self.horario

    @horário.setter
    def horário(self, valor):
        self.horario = self._validar_horario(valor)

    @property
    def estação(self):
        return self.estacao

    @estação.setter
    def estação(self, valor):
        self.estacao = str(valor)

    def __str__(self):
        return self.nome

    def __eq__(self, outro):
        if isinstance(outro, str):
            return self.nome.casefold() == outro.strip().casefold()
        if isinstance(outro, Bioma):
            return self.nome.casefold() == outro.nome.casefold()
        return NotImplemented

    __hash__ = None

    @staticmethod
    def _perder_hidratacao(corpo, quantidade):
        corpo.hidratacao = max(0.0, min(100.0, corpo.hidratacao - quantidade))

    @staticmethod
    def _perder_oxigenio(corpo, quantidade):
        if hasattr(corpo, "saturacao_oxigenio"):
            corpo.saturacao_oxigenio = max(
                0.0, corpo.saturacao_oxigenio - quantidade
            )


class Deserto(Bioma):

    def __init__(self, temperatura_ambiente=35.0, temp_dia=42.0,
                 temp_noite=12.0, amplitude_termica=None, horario=None):
        self.temp_noite = float(temp_noite)
        self.amplitude_termica = (
            abs(float(temp_dia) - self.temp_noite)
            if amplitude_termica is None else float(amplitude_termica)
        )
        if self.amplitude_termica < 0:
            raise ValueError("A amplitude térmica não pode ser negativa.")
        self.temp_dia = self.temp_noite + self.amplitude_termica
        super().__init__("Deserto", "Cactos e arbustos resistentes à seca",
                         "Árido e seco", "Répteis e pequenos mamíferos",
                         temperatura_ambiente, 10.0, horario)

    def calcular_temp(self, horario=None, temperatura_informada=None):
        if temperatura_informada is not None:
            self.atualizar_temperatura(temperatura_informada, horario)
            return self.temperatura()
        if horario is not None:
            self.horario = self._validar_horario(horario)
        temp = self.temp_dia if 6 <= self.horario < 18 else self.temp_noite
        self.atualizar_temperatura(temp, self.horario)
        return self.temperatura()

    def efeito_termico(self, corpo, temperatura=None):
        if temperatura is not None:
            self.atualizar_temperatura(temperatura)
        temp = self.temperatura()
        if temp >= 45:
            self._perder_hidratacao(corpo, 10)
            corpo.temperatura_corpo = 39.5
            corpo.pressao_arterial = 100.0
            self._perder_oxigenio(corpo, 2)
            return "Calor extremo: risco elevado de desidratação e exaustão térmica."
        if temp >= 30:
            self._perder_hidratacao(corpo, 5)
            corpo.temperatura_corpo = 38.0
            corpo.pressao_arterial = 110.0
            return "Calor intenso: o corpo perde água para ajudar a se resfriar."
        if temp <= 10:
            self._perder_hidratacao(corpo, 1)
            corpo.temperatura_corpo = 36.0
            return "Noite fria no deserto."
        self._perder_hidratacao(corpo, 2)
        corpo.temperatura_corpo = 36.8
        return "Temperatura moderada no deserto."


class Taiga(Bioma):

    def __init__(self, temperatura_ambiente=None, temperatura_media=-5.0,
                 horario=None):
        temp = self.temperatura_Media if temperatura_ambiente is None else temperatura_ambiente
        super().__init__("Taiga", "Coníferas, como pinheiros e abetos",
                         "Frio continental/subártico", "Alces, lobos e ursos",
                         temp, 45.0, horario)

    @property
    def temperatura_media(self):
        return self.temperatura_Media

    def efeito_termico(self, corpo, temperatura=None):
        if temperatura is not None:
            self.atualizar_temperatura(temperatura)
        temp = self.temperatura()
        if temp <= -10:
            self._perder_hidratacao(corpo, 4)
            corpo.temperatura_corpo = 35.5
            corpo.pressao_arterial = 135.0
            self._perder_oxigenio(corpo, 1)
            return "Frio intenso na taiga: vasoconstrição e conservação de calor."
        if temp <= 5:
            self._perder_hidratacao(corpo, 2)
            corpo.temperatura_corpo = 36.2
            corpo.pressao_arterial = 125.0
            return "Frio moderado na taiga: o corpo precisa conservar calor."
        self._perder_hidratacao(corpo, 1)
        corpo.temperatura_corpo = 36.7
        return "Condições relativamente amenas para a taiga."


class Tundra(Bioma):

    def __init__(self, temperatura_ambiente=-15.0, altitude_Metros=0.0,
                 velocidade_vento_kmh=25.0, horario=None):
        self.altitude_Metros = float(altitude_Metros)
        self._velocidade_vento_kmh = float(velocidade_vento_kmh)
        if self.altitude_Metros < 0 or self._velocidade_vento_kmh < 0:
            raise ValueError("Altitude e velocidade do vento não podem ser negativas.")
        super().__init__("Tundra", "Musgos, líquens e pequenos arbustos",
                         "Polar, com inverno rigoroso", "Renas e raposas-do-ártico",
                         temperatura_ambiente, 50.0, horario)

    def velocidade_vento(self):
        return self._velocidade_vento_kmh

    def efeito_termico(self, corpo, temperatura=None):
        if temperatura is not None:
            self.atualizar_temperatura(temperatura)
        sensacao = self.temperatura() - min(15.0, self.velocidade_vento() * 0.2)
        if sensacao <= -20:
            self._perder_hidratacao(corpo, 5)
            corpo.temperatura_corpo = 35.0
            corpo.pressao_arterial = 140.0
            self._perder_oxigenio(corpo, 2)
            mensagem = "Frio extremo na tundra: o vento aumenta a perda de calor."
        elif sensacao <= 0:
            self._perder_hidratacao(corpo, 3)
            corpo.temperatura_corpo = 36.0
            corpo.pressao_arterial = 130.0
            mensagem = "Frio intenso na tundra: o corpo precisa conservar calor."
        else:
            self._perder_hidratacao(corpo, 1)
            corpo.temperatura_corpo = 36.7
            mensagem = "Condições menos rigorosas para a tundra."
        if self.altitude_Metros >= 2000:
            self._perder_oxigenio(corpo, 2)
            mensagem += " A altitude elevada também pode reduzir a oxigenação."
        return mensagem
