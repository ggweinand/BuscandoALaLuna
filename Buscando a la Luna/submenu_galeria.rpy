# Menu para los animales
init python:

    galerias = [
        ("fotos_mercurio", _("Mercurio")),
        ("fotos_venus", _("Venus")),
        ("fotos_tierra", _("Tierra")),
        ("fotos_marte", _("Marte")),
        ("fotos_jupiter", _("Júpiter")),
        ("fotos_saturno", _("Saturno")),
        ("fotos_urano", _("Urano")),
        ("fotos_neptuno", _("Neptuno")),
        ]

screen galerias:

    side "c r":
        area (250, 40, 548, 400)

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
                for label, name in galerias:
                    button:
                        action Return(label)
                        left_padding 20
                        xfill True

                        hbox:
                            text name style "button_text" min_width 420
                null height 20
                
                textbutton _("Volver"):
                    xfill True
                    action Return(False)


        bar adjustment adj style "vscrollbar"



label submenu_galeria:
    
    
    $ galerias_adjustment = ui.adjustment()

    call screen galerias(adj=galerias_adjustment)
    
    if _return is False:
        return

    call expression _return

    jump submenu_galeria
    