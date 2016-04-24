# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define jup = Character('Júpiter', color="#d8ca9d")


label planeta_jupiter:

    #historia con Jupiter
    
    
    scene bg space
    show mc at left
    with dissolve
    
    if persistent.jupiter:
        jump visited
        
    centered "Explorando un poco con su telescopio, Itatí divisó Júpiter."
    
    show jupiter:
        xalign 1.0
        yalign 0.5
    with dissolve
    
    i "¡Jupiter! ¿Cómo estas?"
    jup "Muy bien Itatí, muchas gracias por preguntar. ¿Vos como estas?"
    i "Todavia no pude encontrar a la Luna..."
    jup "Lo sé, desde aquí puedo ver que todavía no hay rastros de ella"
    i "¡Sé que va a aparecer!"
    i "Cualquier información que tengas me sería de mucha utilidad."
    jup "Quedate tranquila, prestá atencion, te voy a dar un dato interesante..."
    jup "Uno de los primeros observadores de la Luna fue Galileo Galilei, con un telescopio en 1608."
    i "¡Muchas Gracias!"

    
    #termina la historia
    $persistent.jupiter = True
    
    return
