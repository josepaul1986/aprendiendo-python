class Player:
    vocacion = "Aldeano Valiente"
    hechizo = "Puff!"
    velocidad_movimiento = 50

    def __init__(self, **kwargs):
        self.hit_points = kwargs.get("hit_points",50)
        self.mana = kwargs.get("mana",50)

    def lanzar_hechizo(self):
        return self.hechizo

class Sorcerer(Player):
    vocacion="Sorcerer"
    hechizo = "Wing guardium leviousa!"
    velocidad_movimiento = 20

class Knight(Player):
    vocacion="Caballero"
    hechizo = "Expelermus!"
    velocidad_movimiento = 60

class Paladin(Player):
    vocacion="Caballero"
    hechizo = "Espectro Patronus!"
    velocidad_movimiento = 80

class Druida(Player):
    vocacion="Druida"
    hechizo = "Exori!"
    velocidad_movimiento = 45