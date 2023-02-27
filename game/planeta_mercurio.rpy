# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define mer = Character('Mercurio', color="#f0bc11")

#IMAGENESS
image bg space = "noche.jpg"

label planeta_mercurio:
    
    
    #historia con Mercurio
    scene bg space
    show mc at left
    with dissolve
    
    if persistent.mercurio:
        jump visited
        
    i "Desde aquí puedo ver a Mercurio, voy a preguntarle si me puede ayudar a encontrar a la Luna."
    
    show mercurio:
        xalign 1.0
        yalign 0.5
    with dissolve
    
    i "Hola Mercurio, soy Itatí."
    mer "Hola Itatí, ¿cómo estás?"
    i "Estoy bien, sólo que un poco confundida. No logro encontrar la Luna en ningún lado. ¿Sabés algo de ella?"
    mer "Lo único que puedo decirte es que el hombre llegó a ella por primera vez el 20 de julio de 1969, a bordo del Apollo 11."
    
    #termina la historia
    $persistent.mercurio = True

    return
