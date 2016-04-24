# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define abu = Character('Abuelo', color="#c8ffc8")

image abuelo = im.FactorScale("old-man.png", 0.18, 0.18)

label abuelo:
    
    play music "abuelo.mp3"
    
    #historia con abuelo
    scene bg downtown
    show mc at left
    with dissolve
    
    centered "Triste nuestra amiga por no descrubrir el por qué la luna no estaba sobre nuestro hermoso cielo esa noche, decide volver a casa, pero en el camino se encuentra con una persona muy especial y muy sabia, su abuelo."
    
    show abuelo:
        xalign 1.0
        yalign 0.5
    with dissolve
    
    abu "Itatí, querida. ¿Dónde andabas? ¿Qué estabas haciendo? Tus padres están buscándote por el barrio."
    i "Abuelito, perdón pero en serio quería saber por qué no podíamos ver a la Luna durante esta noche."
    abu "¿Por qué no me lo preguntaste a mí, hijita? Yo te lo puedo responder tranquilamente."
    i "(¿En serio viajé tanto para que al final me cuente todo mi abuelito...?)"
    i "Es que le había preguntado a papá y mamá, y ellos no sabían. Además vos estabas durmiendo, Abuelito."
    abu "Bueno, volvamos a casa y digámosle a tus padres que ya te encontramos. De paso te voy contando sobre las fases lunares..."
    abu "El ciclo lunar consta de varias fases lunares: en total son 8 que cambian cada tres días y medio. Te voy a explicar las 4 más importantes:"
    abu "Luna llena: es cuando la luna recibe la totalidad de la luz solar."
    abu "Cuarto Creciente y Cuarto Menguante: ocurren cuando la Luna sólo recibe la mitad de la luz solar por cierto lado."
    abu "Por último la Luna nueva ocurre cuando la cara que vemos no recibe luz solar... es por eso que no podemos ver hoy a la Luna, querida Itatí."
    i "¡Así que era eso! Gracias Abuelito, perdón por no tenerte en cuenta."
    abu "No pasa nada hijita, volvamos a casa a descansar, que mañana te cuento más sobre la luna..."
    i "Sí, ¡gracias Abuelito!"
    
    #termina la historia
    $ persistent.abuelo_disable = True 
    return
