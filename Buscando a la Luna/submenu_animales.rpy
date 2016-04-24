# Menu para los animales
init python:

    animals = [
        ("animal_murc", _("Ir al Parque.")),
        ("animal_gato", _("Ir al Centro.")),
        ("animal_puma", _("Ir a la Reserva Natural.")),
        ]

screen animals:

    side "c r":
        area (250, 40, 548, 400)

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
                for label, name in animals:
                    button:
                        action Return(label)
                        left_padding 20
                        xfill True

                        hbox:
                            text name style "button_text" min_width 420
                null height 20


#personajes
define lla = Character('Llama', color="#c8ffc8")
define gui = Character('Guillermo', color="#c8ffc8")

#IMAGENES
image llama = im.FactorScale("llamacornio.png", 0.18, 0.18)
image bg reserva = im.FactorScale("campo.jpg", 0.15, 0.15)


label submenu_animales:
    
    if not persistent.llama_disable:
        $ persistent.llama_disable = False
    
    if persistent.llama_disable:
        jump after_llama
    else:
        jump animal_llama
    
#la llama es compulsiva ahora    
label animal_llama:
    
    #historia con la llama
    play music "animals.mp3"
    
    scene bg reserva
    show mc at left
    with dissolve
    centered "Itatí decide tomar su mochila e ir a dar una vuelta por su ciudad."
    i "¿Dónde sería el mejor lugar para recopilar información sobre la Luna?"
    centered "Itatí decide ir a las afueras de la ciudad, pensando que tal vez pueda ver un cielo más estrellado, sin tantas luces de la ciudad."
    centered "En el vasto campo divisa una silueta extraña, se acerca a ésta y ve que es un animal que ella conoce, es una llama."
    
    show llama at right
    with dissolve
    i "Ay que lindo, ¡una llama!"
    lla "¿Hola?"
    i "(¿La llama habló? Debo estar alucinando...)"
    lla "Mi nombre es Guillermo. ¿Cuál es el tuyo? ¿Qué haces caminando a estas horas por acá? Es un poco peligroso y está muy oscuro ahora."
    i "Ehhh, mi nombre es Itatí, soy de esta ciudad, estoy buscando una respuesta del por qué la Luna no está presente esta noche." 
    gui "Mhm... Interesante pregunta, dejame pensar qué podría estar pasando."
    i "Sí, es que me da mucha curiosidad y no sé qué está pasando..."
    gui "Lo poco que sé de la Luna es su distancia con respecto a la Tierra."
    i "¿Cuál es?"
    gui "Su distancia son 20 murallas chinas o 20 veces Rusia de largo aproximadamente. Eso es lo único que se me ocurre en este momento."
    gui "Si querés saber más información sobre la Luna, podrías volver a la ciudad, tengo amigos que pueden saber algo, tendrías que buscarlos..."
    i "¡Uy, genial saber eso sobre nuestro satélite! Sí, me encantaría saber más."
    i "¡Iré en busca de tus amigos para saber qué está pasando! ¡Adiós y muchas gracias Guillermo!"
    gui "¡Dale, me alegro, mucha suerte en tu búsqueda, hasta pronto!"

    $ persistent.llama_disable = True
    
label after_llama:
    
    play music "animals.mp3"
    
    if not persistent.animales_done:
        $persistent.animales_done = False
    
    if not persistent.murcielago:
        $persistent.murcielago = False
    
    if not persistent.puma:
        $persistent.puma = False
    
    if not persistent.gato:
        $persistent.gato = False

    $ animals_adjustment = ui.adjustment()
    
    scene bg habitacion
    show mc at left
    with dissolve

    call screen animals(adj=animals_adjustment)
    
    call expression _return
    
    $ persistent.animales_done = persistent.puma and persistent.gato and persistent.murcielago
    
    if persistent.animales_done:
        jump animales_end
    
    else:
        jump after_llama

label animales_end:
    
    return
