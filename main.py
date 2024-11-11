@namespace
class SpriteKind:
    button = SpriteKind.create()
    monkey_type = SpriteKind.create()
def CtoF():
    global opcio_usuari
    opcio_usuari = game.ask_for_number("Enter temp in C", 4)
    return opcio_usuari * (5 / 9) + 32
def FtoC():
    global opcio_usuari
    opcio_usuari = game.ask_for_number("Enter temp in F", 4)
    return (opcio_usuari - 32) * (5 / 9)
def salutacio(opcio: number):
    CtoF()
    game.show_long_text("hola", DialogLayout.CENTER)
    if opcio == 1:
        game.show_long_text("hola", DialogLayout.TOP)
    elif opcio == 2:
        game.show_long_text("adéu", DialogLayout.TOP)
    else:
        game.show_long_text("Opció no vàlida", DialogLayout.BOTTOM)
def choose_level():
    global fire_plane2, forest_a, forest_b, setting_level
    chosen_level = 0
    tiles.set_tilemap(tilemap("""
        nivel1
    """))
    if setting_level == 1 and chosen_level == 0:
        game.splash("Benvingut a la calculadorra de temperatura")
        game.splash("Escull si passar de C a F", "o de F a C")
        game.show_long_text("Mou el personatje amb el cursor", DialogLayout.BOTTOM)
        forest_a = sprites.create(assets.image("""
            OptA
        """), SpriteKind.button)
        forest_b = sprites.create(assets.image("""
            OptB
        """), SpriteKind.button)
        forest_a.set_position(30, 70)
        forest_b.set_position(130, 70)
        fire_plane2.set_position(85, 70)
        fire_plane2.set_bounce_on_wall(True)
        fire_plane2.set_stay_in_screen(True)
        controller.move_sprite(fire_plane2)
    if chosen_level > 0:
        setting_level = 0
        sprites.destroy(forest_a)
        sprites.destroy(forest_b)


def on_on_overlap2(sprite, otherSprite):
    global chosen_level
    if setting_level == 1:
        otherSprite.start_effect(effects.halo, 4000)
        if otherSprite == forest_a:
            fire_plane2.say_text("Celsius a Farenhein", 10, False)
            if controller.A.is_pressed():
                chosen_level = 1
                effects.clear_particles(otherSprite)
                CtoF()
        elif otherSprite == forest_b:
            fire_plane2.say_text("Farenhein a Celsius", 10, False)
            if controller.A.is_pressed():
                chosen_level = 1
                effects.clear_particles(otherSprite)
                FtoC()
sprites.on_overlap(SpriteKind.player, SpriteKind.button, on_on_overlap2)

forest_b: Sprite = None
forest_a: Sprite = None
fire_plane2: Sprite = None
chosen_level = 0
opcio_usuari = 0
setting_level = 0
fire_plane2 = sprites.create(assets.image("""
        Cross
    """), SpriteKind.player)
setting_level = 1
choose_level()