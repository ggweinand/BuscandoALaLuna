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
        
    centered "Explorando un poco más con su telescopio, Itatí descubrió a Júpiter."
    
    show jupiter:
        xalign 1.0
        yalign 0.5
    with dissolve
    
    i "¡Júpiter! ¿Cómo estás?"
    jup "Muy bien. ¿Puedo ayudarte en algo?"
    i "No puedo encontrar la Luna..."
    jup "¿Sabías que uno de los primeros observadores de la Luna fue Galileo Galilei, con un telescopio en 1608? Ojalá que con el tuyo puedas encontrarla."
    i "¡Muchas Gracias! Hasta pronto."

    
    #termina la historia
    $persistent.jupiter = True
    
    return
