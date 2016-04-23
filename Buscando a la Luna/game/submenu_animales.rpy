# Menu para los animales
init python:

    animals = [
        ("submenu_animales", _("Salir a caminar.")),
        ("submenu_telescopio", _("Mirar por el telescopio.")),
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

    $ animals_adjustment = ui.adjustment()

    call screen animals(adj=animals_adjustment)
    
    if _return is False:
        jump end

    call expression _return

    return
    return
