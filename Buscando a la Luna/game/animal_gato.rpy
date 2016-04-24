# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define cat = Character('Gato', color="#31dfac")
define rama = Character('Ramiro', color="#31dfac")

#IMAGESS
image gato = im.FactorScale("kitty-cat.png", 0.18, 0.18)
image bg downtown = im.FactorScale("dark-street.jpg",1,1)

label animal_gato:
    
    #historia con gato
    scene bg downtown
    show mc at left
    with dissolve
    
    if persistent.gato:
        jump visited
        
    centered "Itatí decide ir al centro de esa ciudad en busca de alguien que pueda ayudarla."
    centered "Mientras camina, ve un gato en un callejón y decide acercarse."
    
    show gato at right
    with dissolve
    
    i "¡Hola gatito! Me manda Guillermo."
    cat "Hola pequeña, mi nombre es Ramiro, estoy buscando alimento. ¿Sabés dónde puedo encontrar comida?"
    i "No lo sé, pero tengo algunas galletitas en mi mochila. ¿Las querés?"
    rama "Por supuesto, contame qué andás buscando vos."
    i "¿Sabés por qué la Luna no está sobre el cielo esta noche?"
    rama "La verdad que no... Lo único que sé sobre la Luna, es que afecta de manera directa a la Tierra. Dependiendo de su ubicación hay marea alta o baja..."
    rama "...pero desconozco por qué esta noche no está en el cielo."
    i "Bueno, ¡muchas gracias Ramiro!"
    rama "Ojalá encuentres la respuesta, ¡suerte!"
    i "Gracias, ¡suerte a vos con la comida!"

    
    #termina la historia
    $ persistent.gato = True    
    return
