namespace SpriteKind {
    export const button = SpriteKind.create()
    export const monkey_type = SpriteKind.create()
}

function CtoF() {
    
    opcio_usuari = game.askForNumber("Enter temp in C", 4)
    return opcio_usuari * (5 / 9) + 32
}

function FtoC(): number {
    
    opcio_usuari = game.askForNumber("Enter temp in F", 4)
    return (opcio_usuari - 32) * (5 / 9)
}

function salutacio(opcio: number) {
    CtoF()
    game.showLongText("hola", DialogLayout.Center)
    if (opcio == 1) {
        game.showLongText("hola", DialogLayout.Top)
    } else if (opcio == 2) {
        game.showLongText("adéu", DialogLayout.Top)
    } else {
        game.showLongText("Opció no vàlida", DialogLayout.Bottom)
    }
    
}

function choose_level() {
    
    let chosen_level = 0
    tiles.setTilemap(tilemap`
        nivel1
    `)
    if (setting_level == 1 && chosen_level == 0) {
        game.splash("Benvingut a la calculadorra de temperatura")
        game.splash("Escull si passar de C a F", "o de F a C")
        game.showLongText("Mou el personatje amb el cursor", DialogLayout.Bottom)
        forest_a = sprites.create(assets.image`
            OptA
        `, SpriteKind.button)
        forest_b = sprites.create(assets.image`
            OptB
        `, SpriteKind.button)
        forest_a.setPosition(30, 70)
        forest_b.setPosition(130, 70)
        fire_plane2.setPosition(85, 70)
        fire_plane2.setBounceOnWall(true)
        fire_plane2.setStayInScreen(true)
        controller.moveSprite(fire_plane2)
    }
    
    if (chosen_level > 0) {
        setting_level = 0
        sprites.destroy(forest_a)
        sprites.destroy(forest_b)
    }
    
}

sprites.onOverlap(SpriteKind.Player, SpriteKind.button, function on_on_overlap2(sprite: Sprite, otherSprite: Sprite) {
    
    if (setting_level == 1) {
        otherSprite.startEffect(effects.halo, 4000)
        if (otherSprite == forest_a) {
            fire_plane2.sayText("Celsius a Farenhein", 10, false)
            if (controller.A.isPressed()) {
                chosen_level = 1
                effects.clearParticles(otherSprite)
                CtoF()
            }
            
        } else if (otherSprite == forest_b) {
            fire_plane2.sayText("Farenhein a Celsius", 10, false)
            if (controller.A.isPressed()) {
                chosen_level = 1
                effects.clearParticles(otherSprite)
                FtoC()
            }
            
        }
        
    }
    
})
let forest_b : Sprite = null
let forest_a : Sprite = null
let fire_plane2 : Sprite = null
let chosen_level = 0
let opcio_usuari = 0
let setting_level = 0
fire_plane2 = sprites.create(assets.image`
        Cross
    `, SpriteKind.Player)
setting_level = 1
choose_level()
