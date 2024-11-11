@namespace
class SpriteKind:
    user = SpriteKind.create()
    option = SpriteKind.create()
def CtoF():
    global opcio_usuari
    opcio_usuari = game.ask_for_number("Enter temp in C", 4)
    temp = Math.round_with_precision(opcio_usuari * (5 / 9) + 32, 2)
    game.splash("" + str(opcio_usuari) + " C = " + ("" + str(temp)) + " F")

def on_on_overlap(sprite, otherSprite):
    global chosen_level2
    otherSprite.start_effect(effects.star_field, 1000)
    if otherSprite == forest_a:
        player.say_text("Celsius a Farenheit", 100, False)
        if controller.A.is_pressed():
            chosen_level2 = 1
            effects.clear_particles(otherSprite)
            player.set_position(90, 90)
            CtoF()
    elif otherSprite == forest_b:
        player.say_text("Farenheit a Celsius", 100, False)
        if controller.A.is_pressed():
            chosen_level2 = 1
            effects.clear_particles(otherSprite)
            player.set_position(90, 90)
            FtoC()
sprites.on_overlap(SpriteKind.user, SpriteKind.option, on_on_overlap)

def FtoC():
    global opcio_usuari
    opcio_usuari = game.ask_for_number("Enter temp in F", 4)
    temp2 = Math.round_with_precision((opcio_usuari - 32) * (5 / 9), 2)
    game.splash("" + str(opcio_usuari) + " C = " + ("" + str(temp2)) + " C")
def choose_level():
    global forest_a, forest_b
    scene.set_background_image(assets.image("""
        Background
    """))
    game.splash("Benvingut a la calculadora", "de temperatura")
    game.splash("Escull si passar", "de C a F o de F a C")
    game.show_long_text("Mou el personatje amb el cursor", DialogLayout.BOTTOM)
    forest_a = sprites.create(assets.image("""
        OptA
    """), SpriteKind.option)
    forest_b = sprites.create(assets.image("""
        OptB
    """), SpriteKind.option)
    forest_a.set_position(40, 90)
    forest_b.set_position(120, 90)
    player.set_position(80, 90)
    player.set_bounce_on_wall(True)
    player.set_stay_in_screen(True)
    controller.move_sprite(player)
chosen_level2 = 0
forest_b: Sprite = None
forest_a: Sprite = None
player: Sprite = None
opcio_usuari = 0
chosen_level = 0
player = sprites.create(assets.image("""
    Cross
"""), SpriteKind.user)

setting_level = 1
choose_level()