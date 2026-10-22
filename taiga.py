from bioma import Bioma


class Taiga(Bioma):
    def __init__(self, umidade, temperatura,
                 temperatura_media):

        super().__init__(
            "Taiga",
            "Coníferas",
            "Frio e subártico",
            "Alces e ursos",
            umidade,
            temperatura
        )

        self.temperatura_media = temperatura_media
