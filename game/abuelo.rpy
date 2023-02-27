# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define abu = Character('Abuelo', color="#c8ffc8")

image abuelo = im.FactorScale("old-man.png", 0.18, 0.18)

label abuelo:
    
    scene bg habitacion
    show mc at left
    with dissolve
    
    i "Hm, debería seguir buscando..."
    
    play music "abuelo.mp3"
    
    #historia con abuelo
    
    show abuelo:
        xalign 1.0
        yalign 0.5
    with dissolve
    
    abu "Itatí, querida. ¿Qué estas haciendo con mis libros?"
    i "¡Abuelito! Quería saber por qué no podemos ver la Luna esta noche."
    abu "¿Por qué no me lo preguntaste a mí, hijita? Yo te lo puedo responder."
    i "¿En serio Abuelito? Busqué tanto en este cuento..."
    abu "Itatí, ¿sabés lo que son las fases lunares?"
    i "No..."
    abu "Entonces empecemos por el principio."
    abu "El ciclo lunar consta de varias fases: en total son 8. Cambian cada tres días y medio. Te voy a explicar las 4 más importantes:"
    abu "Luna llena: es cuando toda la Luna recibe luz solar."
    abu "Cuarto Creciente y Cuarto Menguante: ocurren cuando sólo la mitad de la Luna está iluminada por la luz solar."
    abu "Por último la Luna nueva ocurre cuando la cara que vemos no recibe luz solar... es por eso que hoy no podemos verla, querida Itatí."
    i "¡Así que era eso! Gracias, Abuelito."
    abu "Es tarde, vamos a descansar. Mañana te cuento más sobre la luna..."
    i "Sí, ¡hasta mañana Abuelito!"
    
    #termina la historia
    $ persistent.abuelo_disable = True 
    return
