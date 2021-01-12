class Player:

    def __init__(self, **kwargs):
        self.hit_points = kwargs.get("hit_points",50)
        self.mana = kwargs.get("mana",50)
        self.vocacion = kwargs.get("vocacion","gnomo")
        self.hechizo = kwargs.get("hechizo","Puff!")

    def lanzar_hechizo(self):
        return self.hechizo