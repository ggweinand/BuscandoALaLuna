# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define mar = Character('Marte', color="#c8ffc8")


label planeta_marte:

    #historia con Marte
    
    #show scene bg space
    #show mc at left
    #with dissolve
    
    if persistent.marte:
        jump visited
        
    i "Inclinando el telescopio, Itatí pudo divisar a Marte. Luego de saludarlo, siguió buscando información de la Luna."
    
    #show marte at right
    #with dissolve
    
    i "Marte, ¿podrías ayudarme?"
    i "Sigo sin poder encontrar a la Luna. ¿Tendrías algún dato que me ayude a ubicarla?"
    mar "No me digas... aún no ha aparecido, ¿verdad?"
    mar "No te preocupes demasiado, suele hacer esas cosas regularmente. Sobre ella puedo decir que fue formada hace más de 4000 millones de años, pero nada más." 
    i "No te preocupes, tarde o temprano podré averigüar donde está."
    i "¡Muchas gracias por tu ayuda! ¡Adiós!"
    
    #termina la historia
    $persistent.marte = True

    return
