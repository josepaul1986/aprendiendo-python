import player

gnomo = player.Player(hit_points=15,mana=25)
sorcerer = player.Sorcerer(hit_points=40,mana=80)
knight = player.Knight(hit_points=80,mana=20)
paladin = player.Paladin(hit_points=100,mana=40)
druid = player.Druida(hit_points=60,mana=100)

print("\nEl jugador tiene vocacion {0} con {1} puntos de ataque. Puede lanzar el hechizo {2} y puede moverse a una velocidad {3}".format(gnomo.vocacion, 
                                                                                                                                        gnomo.hit_points,
                                                                                                                                        gnomo.lanzar_hechizo(), 
                                                                                                                                        gnomo.velocidad_movimiento))

print("\nEl jugador tiene vocacion {0} con {1} puntos de ataque. Puede lanzar el hechizo {2} y puede moverse a una velocidad {3}".format(sorcerer.vocacion, 
                                                                                                                                        sorcerer.hit_points,
                                                                                                                                        sorcerer.lanzar_hechizo(), 
                                                                                                                                        sorcerer.velocidad_movimiento))

print("\nEl jugador tiene vocacion {0} con {1} puntos de ataque. Puede lanzar el hechizo {2} y puede moverse a una velocidad {3}".format(knight.vocacion, 
                                                                                                                                        knight.hit_points,
                                                                                                                                        knight.lanzar_hechizo(), 
                                                                                                                                        knight.velocidad_movimiento))

print("\nEl jugador tiene vocacion {0} con {1} puntos de ataque. Puede lanzar el hechizo {2} y puede moverse a una velocidad {3}".format(paladin.vocacion, 
                                                                                                                                        paladin.hit_points,
                                                                                                                                        paladin.lanzar_hechizo(), 
                                                                                                                                        paladin.velocidad_movimiento))

print("\nEl jugador tiene vocacion {0} con {1} puntos de ataque. Puede lanzar el hechizo {2} y puede moverse a una velocidad {3}".format(druid.vocacion, 
                                                                                                                                        druid.hit_points,
                                                                                                                                        druid.lanzar_hechizo(), 
                                                                                                                                        druid.velocidad_movimiento))