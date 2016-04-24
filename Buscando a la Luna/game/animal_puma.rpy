# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define p = Character('Puma', color="#31dfac")
define nico = Character('Nicolás', color="#31dfac")

#IMAGENESSS
image bg reserva = im.FactorScale("campo.jpg", 0.15, 0.15)
image puma = im.FactorScale("big-cat.png", 0.18, 0.18)


label animal_puma:
    
    #historia con puma
    scene bg reserva
    show mc at left
    with dissolve
    
    if persistent.puma:
        jump visited
        
    centered "Ahora, nuestra aventurera decide caminar cerca de una reserva natural y se encuentra con un puma."
    
    show puma at right
    with dissolve
    
    i "¡Hola puma! Me manda Guillermo."
    p "Hola, mi nombre es Nicolás. ¿Qué estás buscando?"
    i "Hola Nicolás, me gustaría saber por qué la Luna no se encuentra en el cielo en este momento. ¿Sabés por qué pasa esto?"
    nico "Qué raro que una Luna no se vea, ya que su diámetro es como 12 veces la Torre Eiffel."
    i "Gracias Nico, seguiré buscando una respuesta. Me despido, ¡hasta pronto!"
    nico "¡Hasta luego niña!"
    
    #termina la historia
    $ persistent.puma = True    
    return
