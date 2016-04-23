# Menu para los animales
init python:

    animals = [
        ("animal_murc", _("Ir al Parque.")),
        ("animal_gato", _("Ir al Centro.")),
        ("animal_puma", _("Ir al Zoo.")),
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

        bar adjustment adj style "vscrollbar"



label submenu_animales:
    
#la llama es compulsiva ahora    
label animal_llama:
    #historia con la llama
    
    
label after_llama:
    
    if not persistent.animales_done:
        $persistent.animales_done = False
    
    if not persistent.murcielago:
        $persistent.murcielago = False
    
    if not persistent.puma:
        $persistent.puma = False
    
    if not persistent.gato:
        $persistent.gato = False

    $ animals_adjustment = ui.adjustment()

    call screen animals(adj=animals_adjustment)
    
    call expression _return
    
    $ persistent.animales_done = persistent.puma and persistent.gato and persistent.marte and persistent.murcielago
    
    if persistent.animales_done:
        jump animales_end
    
    else:
        jump after_llama

label animales_end:
    
    return
