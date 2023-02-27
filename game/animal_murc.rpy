# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define mur = Character('Murciélago', color="#035e60")
define agus = Character('Agustín', color="#035e60")

#IMAGENES
image bg parque = im.FactorScale("Park.jpg", 0.2, 0.2)
image murcielago = im.FactorScale("Crobat.png", 0.18, 0.18)


label animal_murc:
    
    #historia con murcielago
    scene bg parque
    show mc at left
    with dissolve
    
    if persistent.murcielago:
        jump visited
        
    centered "Itatí va al parque más grande de la ciudad en busca de alguna respuesta. Mirando al cielo ve una silueta negra que se le acerca..."
    
    show murcielago at right
    with dissolve
    
    i "Hola murciélago, me manda Guillermo."
    mur "Me llamo Agustín. ¿Qué andás buscando?"
    i "Me gustaría saber por qué no podemos ver a la Luna esta noche."
    agus "La verdad que no lo sé. Sólo sé que si estuvieras en la Luna podrías flotar y casi volar, como yo, porque la gravedad de la Luna es 6 veces menor a la de la Tierra."
    i "Gracias Agustín por tu información, seguiré buscando, ¡hasta luego!"
    agus "Nos vemos niña, suerte."

    
    #termina la historia
    $ persistent.murcielago = True    
    return
