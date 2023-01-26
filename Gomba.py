class Gomba:
    def __init__(self, sor):
        adatok = sor.split("@").strip()
        self.neve = adatok[0]
        self.nemzettseg = adatok[1]
        self.evszak = adatok[2]
    def __str__(self):
        print(f"Neve: {self.neve}, Nemzettség:{self.nemzettseg}, Évszak: {self.evszak}")