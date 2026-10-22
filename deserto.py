from bioma import Bioma


class Deserto(Bioma):
    def __init__(self, estacao, umidade, temperatura,
                 amplitude_termica):

        super().__init__(
            "Deserto",
            "Cactos e arbustos",
            "Árido",
            "Répteis e roedores",
            estacao,
            umidade,
            temperatura
        )

        self.amplitude_termica = amplitude_termica
