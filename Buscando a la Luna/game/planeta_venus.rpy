# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define ven = Character('Venus', color="#c8ffc8")


label planeta_venus:
    

    #historia con Venus
    
    #show scene bg space
    #show mc at left
    #with dissolve
    
    if persistent.venus:
        jump visited
    
    i "Creo que si pongo mucha atención, puedo ver a Venus."
    
    #show venus at right
    #with dissolve
    
    i "Hola Venus."
    ven "¿Cómo sabés mi nombre?"
    i "Sos el planeta más luminoso del Sistema Solar, escuché hablar de vos."
    ven "Me halagás, pequeña. ¿Cómo es tu nombre?"
    i "Mi nombre es Itatí, y sólo quería molestarte un momento para hacerte unas preguntas." 
    i "¿Sabés algo de la Luna? Hoy miré al cielo y no pude encontrarla."
    ven "Esa Luna... de vez en cuando suele desaparecer..."
    ven "Mirá, hace tiempo que no sé nada de ella, pero una vez oí que desde la Tierra sólo se puede ver una de sus caras, esto se debe a que tarda lo mismo en girar sobre sí misma y en girar alrededor de la Tierra."
    i "Muchas gracias, cada dato es útil."

    #termina la historia
    $persistent.venus = True

    return
