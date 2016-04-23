# Menu para los animales
init python:

    planetas = [
        ("planeta_mercurio", _("Observar Mercurio.")),
        ("planeta_venus", _("Observar Venus.")),
        ("planeta_marte", _("Observar Marte.")),
        ("planeta_jupiter", _("Observar Júpiter.")),
        ]

screen planetas:

    side "c r":
        area (250, 40, 548, 400)

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
                for label, name in planetas:
                    button:
                        action Return(label)
                        left_padding 20
                        xfill True

                        hbox:
                            text name style "button_text" min_width 420
                null height 20


        bar adjustment adj style "vscrollbar"



label submenu_telescopio:
    
    #escena
    #scene bg telescopio
    #show mc at left
    #with dissolve
    
    #inicializar
    if not persistent.telescopio_done:
        $persistent.telescopio_done = False
    
    if not persistent.venus:
        $persistent.venus = False
    
    if not persistent.marte:
        $persistent.marte = False
        
    if not persistent.mercurio:
        $persistent.mercurio = False
        
    if not persistent.jupiter:
        $persistent.jupiter = False
        
    #si ya lo hizo vuelve al menu principal
    if persistent.telescopio_done:
        jump telescopio_end
    

    $ planetas_adjustment = ui.adjustment()

    call screen planetas(adj=planetas_adjustment)

    call expression _return
    
    
    $ persistent.telescopio_done = persistent.mercurio and persistent.venus and persistent.marte and persistent.jupiter
    

    jump submenu_telescopio
    
label telescopio_end:
    $persistent.telescopio_done = True
    i "No creo que haya más información aquí..."
    jump menu_pr
