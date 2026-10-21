class Rins:
    def __init__(self):
        self.filtracao = True

    def filtrarSangue(self, corpo) -> bool:
        if corpo.hidratacao > 0:
            corpo.hidratacao -= 1
            return True
        return False
