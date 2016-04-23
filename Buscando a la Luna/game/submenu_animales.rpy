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

                textbutton _("That's enough for now."):
                    xfill True
                    action Return(False)

        bar adjustment adj style "vscrollbar"



label submenu_animales:
    
#la llama es compulsiva ahora    
label animal_llama:
    #historia con la llama
    
    
label after_llama:

    $ animals_adjustment = ui.adjustment()

    call screen animals(adj=animals_adjustment)
    
    if _return is False:
        jump end

    call expression _return

    return
