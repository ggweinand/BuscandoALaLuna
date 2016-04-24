# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define cat = Character('Gato', color="#c8ffc8")
define rama = Character('Ramiro', color="#c8ffc8")

#IMAGESS
image gato = im.FactorScale("kitty-cat.png", 0.18, 0.18)
image bg downtown = im.FactorScale("dark-street.jpg",1,1)

label animal_gato:
    
    #historia con gato
    scene bg downtown
    show mc at left
    with dissolve
    
    if persistent.gato:
        jump visited
        
    centered "Nuestra compañera decide ir hacia el centro de su ciudad en busca de alguien que pueda ayudarla."
    centered "Durante su caminata a mitad de una cuadra, en un callejón, escucha ruidos raros. Itatí decide acercarse."
    centered "Desde las oscuras paredes del callejón aparece un gato."
    
    show gato at right
    with dissolve
    
    i "(¿Qué estará haciendo?)"
    i "¡Hola gatito!"
    cat "Hola pequeña humana, mi nombre es Ramiro, estoy buscando alimento. ¿Tenés idea de dónde hay tachos de basura con buena comida?"
    i "(¿Acaba de hablarme este gato? Debe ser amigo de Guillermo)"
    i "No lo sé, pero si querés, tengo algunas galletitas en mi mochila. ¿Si te las doy me responderías algunas preguntas?"
    rama "Por supuesto, dámelas y te respondo lo que sepa."
    i "¿Sabés por qué la Luna no está sobre el cielo esta noche?"
    rama "La verdad que no tengo la respuesta... Lo único que sé sobre la Luna, es que afecta de manera directa a la Tierra. Dependiendo de su ubicación hay marea alta o baja..."
    rama "...pero desconozco por qué esta noche no la podemos ver en el cielo. Puede ser que algunos amigos míos en la ciudad sepan algo al respecto."
    rama "Lo siento, suerte con tu búsqueda, ¡espero que puedas encontrar alguna respuesta!"
    i "Bueno, muchas gracias Ramiro, suerte a vos con la comida, ¡nos vemos!"


    
    #termina la historia
    $ persistent.gato = True    
    return
