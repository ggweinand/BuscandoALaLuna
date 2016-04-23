# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define jup = Character('Júpiter', color="#d8ca9d")


label planeta_jupiter:

    #historia con Jupiter
    
    #show scene bg space
    #show mc at left
    #with dissolve
    
    if persistent.jupiter:
        jump visited
        
    centered "Explorando un poco con su telescopio, Itatí divisó Júpiter."
    
    #show jupiter at right
    #with dissolve
    
    i "¡Jupiter! ¿Cómo estas?"
    jup "Muy bien Itatí, muchas gracias por preguntar. ¿Vos como estas?"
    i Todavia no pude encontrar a la Luna..
    jup Lo se, desde aquí puedo ver que todavia no hay rastros de ella
    i ¡Se que va a aparecer!
    i Cualquier informacion que tengas me sería de mucha utilidad
    jup Quedate tranquila, presta atencion, te voy a dar un dato interesante
    jup Uno de los primeros observadores de la luna con telescopio fue Galileo Galilei en 1608
    i Muchas Gracias

    
    #termina la historia
    $persistent.jupiter = True
    
    return
