from bioma import Bioma


class Tundra(Bioma):
    def __init__(self, umidade, temperatura,
                 altitude, velocidade_vento):

        super().__init__(
            "Tundra",
            "Musgos e líquens",
            "Polar",
            "Renas e raposas-do-ártico",
            umidade,
            temperatura
        )

        self.altitude = altitude
        self.velocidade_vento = velocidade_vento
