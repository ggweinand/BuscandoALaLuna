# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define i = Character('Itatí', color="#c8ffc8")


init python:

    tutorials = [
        ("submenu_animales", _("Emprender caminata.")),
        ("submenu_telescopio", _("Mirar por el telescopio.")),
        ("submenu_galeria", _("Galería de Imágenes.")),
        ("submenu_datos", _("Datos sobre la Luna.")),
        ]

screen tutorials:

    side "c r":
        area (250, 40, 548, 400)

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
                for label, name in tutorials:
                    button:
                        action Return(label)
                        left_padding 20
                        xfill True

                        hbox:
                            text name style "button_text" min_width 420
                null height 20

                textbutton _("Reset data."):
                    xfill True
                    action Return(False)

        bar adjustment adj style "vscrollbar"



# The game starts here.
# - El juego comienza aquí.
label start:
    
    if not persistent.abuelo_disable:
        $ persistent.abuelo_disable = False
    
    #intro
    centered "Una noche como cualquier otra, una pequeña niña llamada Itatí, descubrió que en esa noche estrellada, no había rastros de la Luna."
    centered "Al ver que esto no era común, se preocupó, y tomó la decisión de investigar sobre este misterio."
    centered "Sus padres no supieron aclarar sus dudas, así que decidió seguir por su cuenta."
    
    
    $ tutorials_adjustment = ui.adjustment()
    $ menu_first_time = True

label menu_pr:
    
    
    if ((not persistent.abuelo_disable) and persistent.telescopio_done and persistent.animales_done):
        call abuelo
    
    #scene bg habitacion
    #show mc at left
    
    if menu_first_time:
        $ i(_("¿Dónde debería comenzar a buscar?"), interact=False)
    else:
        $ i(_("Debería seguir buscando..."), interact=False)

    $ tutorials_first_time = False

    call screen tutorials(adj=tutorials_adjustment)
    
    if _return is False:
        jump reset

    call expression _return
    
    jump menu_pr



label reset:
    $ persistent.telescopio_done = persistent.mercurio = persistent.marte = persistent.venus = persistent.jupiter = False
    jump menu_pr