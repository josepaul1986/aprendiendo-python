class Player:
    vocacion = "Aldeano Valiente"
    hechizo = "Puff!"
    velocidad_movimiento = 50

    def __init__(self, **kwargs): #metodo constructor que recibe argumento multiple tipo diccionario
        self.hit_points = kwargs.get("hit_points",50)
        self.mana = kwargs.get("mana",50)

    def __str__(self): # metodo str sobreescrito para
        return "\nEl jugador tiene vocacion {0} con {1} puntos de ataque. Puede lanzar el hechizo {2} y puede moverse a una velocidad {3}".format(self.vocacion, 
                                                                                                                                        self.hit_points,
                                                                                                                                        self.lanzar_hechizo(), 
                                                                                                                                        self.velocidad_movimiento)

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