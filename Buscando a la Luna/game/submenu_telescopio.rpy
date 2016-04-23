# Menu para los animales


label submenu_telescopio:

    i "hOi I'm tEmmi3"

    i "Features like saving, loading, changing preferences, and so on."

    i "One of the nice things about Ren'Py is that the engine provides many of these features for you. You can spend your time creating your game, and let us provide these things."

    i "While you're in the game, you can access the game menu by right clicking or hitting the escape key."

    show logo at topright
    
    i "When you first enter the game menu, you'll see the save screen. Clicking on a numbered slot will save the game."

    menu:

        i "Would you like to hear more about rollback?"

        "Yes.":

            jump asd

        "No.":

            jump asd


label asd:

    i "You can invoke a rollback by scrolling the mouse wheel up, or by pushing the page up key. That'll bring you back to the previous screen."

    i "While at a previous screen, you can roll forward by scrolling the mouse wheel down, or pushing the page down key."

    i "Rolling forward through a menu will make the same choice you did last time. But unlike other engines, Ren'Py's rollback system allows you to make a different choice."

    return
