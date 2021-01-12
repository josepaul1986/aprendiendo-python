class Player:

    def __init__(self, hit_points, mana, vocacion, hechizo="Puff"):
        self.hit_points = hit_points
        self.mana = mana
        self.vocacion = vocacion
        self.hechizo = hechizo

    def lanzar_hechizo(self):
        return self.hechizo