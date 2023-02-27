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
define lla = Character('Llama', color="#ff9a00")
define gui = Character('Guillermo', color="#ff9a00")

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
    
    centered "Itatí decide ir a las afueras de esa ciudad, pensando que tal vez pueda ver un cielo más estrellado y así encontrarla."
    
    show mc at left
    with dissolve
    centered "Mientras camina, se encuentra con una llama."
    
    show llama at right
    with dissolve
    i "¿Una llama acá?"
    
    scene bg habitacion
    show mc at left
    with dissolve
    i "(Seguramente va a poder ayudarme...)"
    
    scene bg reserva
    show mc at left
    show llama at right
    with dissolve
    
    i "¡Hola, llama!"
    lla "¡Hola, soy Guillermo! ¿Y vos?"
    i "Soy Itatí, vine a esta ciudad buscando una respuesta. ¿Sabés dónde está la Luna esta noche?" 
    gui "Mhm... interesante pregunta, dejame pensar..."
    gui "Lo poco que sé de la Luna es su distancia con respecto a la Tierra."
    i "¿Cuál es?"
    gui "Su distancia es igual a 20 murallas chinas o 20 veces Rusia de largo aproximadamente. Eso es todo lo que sé."
    gui "Si querés saber más sobre la Luna, regresá a la ciudad. Tengo amigos que podrán ayudarte. Buscalos."
    i "¡Uy, genial! ¡Iré a buscarlos!¡Adiós y muchas gracias, Guillermo!"
    gui "Mandales saludos de mi parte, ¡adiós Itatí!"

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
