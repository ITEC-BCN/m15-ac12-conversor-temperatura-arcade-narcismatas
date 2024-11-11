namespace SpriteKind {
    export const user = SpriteKind.create()
    export const option = SpriteKind.create()
}
function CtoF () {
    opcio_usuari = game.askForNumber("Enter temp in C", 4)
    let temp = Math.roundWithPrecision(opcio_usuari * (5 / 9) + 32, 2)
game.splash("" + opcio_usuari + " C = " + ("" + temp) + " F")
}
sprites.onOverlap(SpriteKind.user, SpriteKind.option, function (sprite, otherSprite) {
    otherSprite.startEffect(effects.starField, 1000)
    if (otherSprite == forest_a) {
        player.sayText("Celsius a Farenheit", 100, false)
        if (controller.A.isPressed()) {
            chosen_level2 = 1
            effects.clearParticles(otherSprite)
            player.setPosition(90, 90)
            CtoF()
        }
    } else if (otherSprite == forest_b) {
        player.sayText("Farenheit a Celsius", 100, false)
        if (controller.A.isPressed()) {
            chosen_level2 = 1
            effects.clearParticles(otherSprite)
            player.setPosition(90, 90)
            FtoC()
        }
    }
})
function FtoC () {
    opcio_usuari = game.askForNumber("Enter temp in F", 4)
    let temp2 = Math.roundWithPrecision((opcio_usuari - 32) * (5 / 9), 2)
game.splash("" + opcio_usuari + " C = " + ("" + temp2) + " C")
}
function choose_level () {
    scene.setBackgroundImage(assets.image`Background`)
    game.splash("Benvingut a la calculadora", "de temperatura")
    game.splash("Escull si passar", "de C a F o de F a C")
    game.showLongText("Mou el personatje amb el cursor", DialogLayout.Bottom)
    forest_a = sprites.create(assets.image`OptA`, SpriteKind.option)
    forest_b = sprites.create(assets.image`OptB`, SpriteKind.option)
    forest_a.setPosition(40, 90)
    forest_b.setPosition(120, 90)
    player.setPosition(80, 90)
    player.setBounceOnWall(true)
    player.setStayInScreen(true)
    controller.moveSprite(player)
}
let chosen_level2 = 0
let forest_b: Sprite = null
let forest_a: Sprite = null
let player: Sprite = null
let chosen_level = 0
let opcio_usuari = 0
player = sprites.create(assets.image`Cross`, SpriteKind.user)
let setting_level = 1
choose_level()
