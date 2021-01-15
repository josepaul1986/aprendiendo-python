import player

# sorcerer = Player(15,25,"gnomo","hey ho! hey ho!")
#gnomo = Player(15,25,"gnomo")
gnomo = player.Player(hit_points=15,mana=25)
# print("\nEl gnomo tiene:")
""" print(gnomo.hit_points)
print(gnomo.mana)
print(gnomo.vocacion)
print(gnomo.lanzar_hechizo())
print(gnomo.velocidad_movimiento) """
print("\nEl jugador tiene vocacion {0} con {1} puntos de ataque. Puede lanzar el hechizo {2} y puede moverse a una velocidad {3}".format(gnomo.vocacion, 
                                                                                                                                        gnomo.hit_points,
                                                                                                                                        gnomo.lanzar_hechizo(), 
                                                                                                                                        gnomo.velocidad_movimiento))

sorcerer = player.Sorcerer(hit_points=40,mana=80)
""" print("\nEl Sorcerer tiene:")
print(sorcerer.hit_points)
print(sorcerer.mana)
print(sorcerer.vocacion)
print(sorcerer.lanzar_hechizo())
print(sorcerer.velocidad_movimiento) """
print("\nEl jugador tiene vocacion {0} con {1} puntos de ataque. Puede lanzar el hechizo {2} y puede moverse a una velocidad {3}".format(sorcerer.vocacion, 
                                                                                                                                        sorcerer.hit_points,
                                                                                                                                        sorcerer.lanzar_hechizo(), 
                                                                                                                                        sorcerer.velocidad_movimiento))

knight = player.Knight(hit_points=80,mana=20)
""" print("\nEl Knight tiene:")
print(knight.hit_points)
print(knight.mana)
print(knight.vocacion)
print(knight.lanzar_hechizo())
print(knight.velocidad_movimiento) """
print("\nEl jugador tiene vocacion {0} con {1} puntos de ataque. Puede lanzar el hechizo {2} y puede moverse a una velocidad {3}".format(knight.vocacion, 
                                                                                                                                        knight.hit_points,
                                                                                                                                        knight.lanzar_hechizo(), 
                                                                                                                                        knight.velocidad_movimiento))

paladin = player.Paladin(hit_points=100,mana=40)
""" print("\nEl paladin tiene:")
print(paladin.hit_points)
print(paladin.mana)
print(paladin.vocacion)
print(paladin.lanzar_hechizo())
print(paladin.velocidad_movimiento) """
print("\nEl jugador tiene vocacion {0} con {1} puntos de ataque. Puede lanzar el hechizo {2} y puede moverse a una velocidad {3}".format(paladin.vocacion, 
                                                                                                                                        paladin.hit_points,
                                                                                                                                        paladin.lanzar_hechizo(), 
                                                                                                                                        paladin.velocidad_movimiento))

druid = player.Druida(hit_points=60,mana=100)
""" print("\nEl druid tiene:")
print(druid.hit_points)
print(druid.mana)
print(druid.vocacion)
print(druid.lanzar_hechizo())
print(druid.velocidad_movimiento) """
print("\nEl jugador tiene vocacion {0} con {1} puntos de ataque. Puede lanzar el hechizo {2} y puede moverse a una velocidad {3}".format(druid.vocacion, 
                                                                                                                                        druid.hit_points,
                                                                                                                                        druid.lanzar_hechizo(), 
                                                                                                                                        druid.velocidad_movimiento))
