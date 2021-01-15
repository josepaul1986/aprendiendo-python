class Player:
    vocacion = "Aldeano Valiente"
    hechizo = "Puff!"
    velocidad_movimiento = 50

    def __init__(self, **kwargs): #metodo constructor que recibe argumento multiple tipo diccionario
        self.name = input("Escribe tu nombre de jugador: ")
        self.hit_points = kwargs.get("hit_points",50)
        self.mana = kwargs.get("mana",50)

    def __str__(self): # metodo str sobreescrito para devolver el string por defecto del objeto.
        return "\nEl jugador con nombre {} tiene vocacion {} con {} puntos de ataque. Puede lanzar el hechizo {} y puede moverse a una velocidad {}".format(
                                                                                                                                        self.name,
                                                                                                                                        self.vocacion, 
                                                                                                                                        self.hit_points,
                                                                                                                                        self.lanzar_hechizo(), 
                                                                                                                                        self.velocidad_movimiento)

    def lanzar_hechizo(self):
        return self.hechizo

class Sorcerer(Player):
    vocacion="Sorcerer"
    hechizo = "Wing guardium leviousa!"
    velocidad_movimiento = 20

    def lanzar_hechizo(self):
        return "{} y Exura".format(self.hechizo)

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

    def lanzar_hechizo(self):
        return "{} y Expelermus".format(self.hechizo)