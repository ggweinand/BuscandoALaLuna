# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define mar = Character('Marte', color="#ff0000")


label planeta_marte:

    #historia con Marte
    
    scene bg space
    show mc at left
    with dissolve
    
    if persistent.marte:
        jump visited
        
    centered "Inclinando el telescopio, Itatí pudo ver a Marte. Luego de saludarlo, le preguntó:"
    
    show marte:
        xalign 1.0
        yalign 0.5
    with dissolve
    
    i "Marte, ¿podrías ayudarme a encontrar a la Luna? Hace rato que la estoy buscando y no logro verla."
    mar "No te preocupes demasiado, suele hacer esas cosas regularmente. Sobre ella puedo decir que fue formada hace más de 4000 millones de años, pero nada más." 
    i "¡Muchas gracias por tu ayuda! ¡Adiós!"
    
    #termina la historia
    $persistent.marte = True

    return
