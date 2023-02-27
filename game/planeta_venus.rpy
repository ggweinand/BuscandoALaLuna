# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define ven = Character('Venus', color="#a7661b")

image venus = im.FactorScale("venus.png", 0.3, 0.3)

label planeta_venus:
    

    #historia con Venus
    
    scene bg space
    show mc at left
    with dissolve
    
    if persistent.venus:
        jump visited
    
    show venus:
        xalign 1.0
        yalign 0.5
    with dissolve
    
    i "Hola Venus."
    ven "¿Cómo sabés mi nombre?"
    i "Sos el planeta más luminoso del Sistema Solar, escuché hablar de vos."
    ven "Ay qué bueno, ¿cómo es tu nombre?"
    i "Mi nombre es Itatí. ¿Sabés algo de la Luna? Hoy miré al cielo y no pude encontrarla."
    ven "Esa Luna... de vez en cuando suele desaparecer..."
    ven "Mirá, hace tiempo que no sé nada de ella, pero una vez oí que desde la Tierra sólo se puede ver una de sus caras, esto se debe a que tarda lo mismo en girar sobre sí misma y en girar alrededor de la Tierra."
    i "¡Qué dato útil! Muchas gracias."

    #termina la historia
    $persistent.venus = True

    return
