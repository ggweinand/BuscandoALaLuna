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


#IMAGENESSSSS
image mc = im.FactorScale("Terra.png", 0.18, 0.18)
image bg habitacion = im.FactorScale("ventana.jpg", 0.5, 0.5)


init python:

    tutorials = [
        ("submenu_animales", _("Salir a caminar.")),
        ("submenu_telescopio", _("Mirar por el telescopio.")),
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

                textbutton _("Borrar datos guardados."):
                    xfill True
                    action Return(False)


# The game starts here.
# - El juego comienza aquí.
label main_menu:
label start:
    
    if not persistent.abuelo_disable:
        $ persistent.abuelo_disable = False
    scene noche
    with dissolve
    
    #intro
    play music "moonphases.mp3"

    centered "Una noche estrellada como cualquier otra, una pequeña niña llamada Itatí descubrió que no se veía la Luna."
    centered "Buscó, miró y miró, y al no encontrarla decidió investigar este misterio."
    centered "En la biblioteca del abuelo encontró un libro sobre la Luna."
    
    
    $ tutorials_adjustment = ui.adjustment()
    if not persistent.menu_first_time_disable:
        $ persistent.menu_first_time_disable = False

label menu_pr:
    
    play music "mprincipal.mp3"
    
    if ((not persistent.abuelo_disable) and persistent.telescopio_done and persistent.animales_done):
        call abuelo
    
    scene bg habitacion
    show mc at center
    with dissolve
    
    if persistent.abuelo_disable:
        show mc at left
        with move
        $ i(_("¡Ahora podés ver datos sobre la Luna!"), interact=False)
    else:
        if persistent.menu_first_time_disable:
            i "¡Qué divertido va a ser esto! Puedo elegir distintos caminos para encontrar a la Luna."
            show mc at left
            with move
            $ i(_("¿Por dónde empiezo a buscar?"), interact=False)
            $ persistent.menu_first_time_disable = True
        else:
            i "Seguro que la respuesta está en otro capítulo..."
            show mc at left
            with move
            $ i(_("Debería seguir buscando..."), interact=False)

    

    call screen tutorials(adj=tutorials_adjustment)
    
    if _return is False:
        jump reset

    call expression _return
    
    jump menu_pr



label reset:
    $ persistent.telescopio_done = persistent.mercurio = persistent.marte = persistent.venus = persistent.jupiter = False
    $ persistent.animales_done = persistent.puma = persistent.murcielago = persistent.gato = persistent.llama_disable = False
    $ persistent.abuelo_disable = False
    $ persistent.menu_first_time_disable = True
    jump menu_pr