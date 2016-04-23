# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define p = Character('Puma', color="#c8ffc8")
define nico = Character('Nicolás', color="#c8ffc8")


label animal_puma:
    
    #historia con puma
    #show scene bg reserva
    #show mc at left
    #with dissolve
    
    if persistent.puma:
        jump visited
        
    centered "Ahora, nuestra aventurera decide caminar cerca de una reserva natural y de los pastizales sale un felino."
    
    #show puma at right
    #with dissolve
    
    p "No deberías andar por acá a estas horas..."
    i "(Genial, ahora un gato enorme...)" 
    i "Disculpame, pero es que tengo una duda que me carcome el cerebro. Por cierto, soy Itatí."
    p "Es inseguro que andes por ahí sola, tenés suerte de que en esta reserva no nos guste la violencia."
    p "Me presento, mi nombre es Nicolás, y pertenezco a esta reserva desde que nací. ¿Cuál es tu duda?"
    i "Hola Nicolás, me gustaría saber por qué la Luna no se encuentra en el cielo en este momento. ¿Sabés por qué pasa esto?"
    nico "Qué raro que una Luna no se vea, ya que su diámetro es como 12 veces la Torre Eiffel."
    nico "No sabría decirte por qué no la podemos ver. Siento no poder explicar eso, pero lo mejor que podés hacer es volver a tu hogar ya que es muy tarde."
    i "Bueno Nico, voy a volver a casa... aunque estoy muy triste... ¡en serio quería saber! Me despido, ¡hasta pronto!"
    nico "Hasta luego niña, ¡cuidado en el camino!"
    
    #termina la historia
    $ persistent.puma = True    
    return
