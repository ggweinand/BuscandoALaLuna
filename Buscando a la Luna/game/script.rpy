# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define i = Character('Itati', color="#c8ffc8")


init python:

    tutorials = [
        ("submenu_animales", _("Salir a caminar.")),
        ("submenu_telescopio", _("Mirar por el telescopio.")),
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

                textbutton _("That's enough for now."):
                    xfill True
                    action Return(False)

        bar adjustment adj style "vscrollbar"



# The game starts here.
# - El juego comienza aquí.
label start:

    #end start
    scene bg office
    show logo at truecenter
    with dissolve

    # Start the background music playing.
    

    window show

    i "Yee"

    
    $ tutorials_adjustment = ui.adjustment()
    $ tutorials_first_time = True

    

label tutorials:
    
    
    show logo at left
    with move

    if tutorials_first_time:
        $ i(_("What would you like to see?"), interact=False)
    else:
        $ i(_("Is there anything else you'd like to see?"), interact=False)

    $ tutorials_first_time = False

    call screen tutorials(adj=tutorials_adjustment)
    
    if _return is False:
        jump end

    call expression _return

    return
