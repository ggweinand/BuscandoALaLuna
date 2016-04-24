# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define mur = Character('Murciélago', color="#c8ffc8")
define agus = Character('Agustín', color="#c8ffc8")

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
        
    centered "Itatí va hacia el parque más grande de la ciudad en busca de alguna respuesta. En éste ve muchas siluetas negras volando alrededor de los árboles, y de repente una de ellas se le acerca..."
    
    show murcielago at right
    with dissolve
    
    mur "¿Qué tal, niña?"
    i "(Otro animal que habla...)" 
    i "Me asustaste... Hola señor Murciélago, soy Itatí. ¿Podría hacerle una pregunta?"
    mur "No me digas señor Murciélago, me llamo Agustín. ¿Qué andas buscando?"
    i "Me gustaría saber por qué no podemos ver a la Luna en esta noche."
    agus "La verdad que no lo sé. Lo que sé, es que si estuvieras en la Luna podrías flotar y casi volar, como yo, ya que la gravedad de la Luna es 6 veces menor a la de la Tierra. Siento no poder ayudarte con tus dudas."
    i "No pasa nada Agustín, ya lo descubriré, muchas gracias por la ayuda, ¡hasta luego!"
    agus "Nos vemos niña, suerte."

    
    #termina la historia
    $ persistent.murcielago = True    
    return
