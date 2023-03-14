
scene.set_background_color(7)


myPlayer = sprites.create(img("""
    . . . . . . f f f f . . . . . .
    . . . . f f f 2 2 f f f . . . .
    . . . f f f 2 2 2 2 f f f . . .
    . . f f f e e e e e e f f f . .
    . . f f e 2 2 2 2 2 2 e e f . .
    . . f e 2 f f f f f f 2 e f . .
    . . f f f f e e e e f f f f . .
    . f f e f b f 4 4 f b f e f f .
    . f e e 4 1 f d d f 1 4 e e f .
    . . f e e d d d d d d e e f . .
    . . . f e e 4 4 4 4 e e f . . .
    . . e 4 f 2 2 2 2 2 2 f 4 e . .
    . . 4 d f 2 2 2 2 2 2 f d 4 . .
    . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
    . . . . . f f f f f f . . . . .
    . . . . . f f . . f f . . . . .
"""), SpriteKind.player)
myPlayer.set_position(3, 3)
controller.move_sprite(myPlayer)

myItemSprite = sprites.create(img("""
    . . . . . . b b b b . . . . . .
    . . . . . . b 4 4 4 b . . . . .
    . . . . . . b b 4 4 4 b . . . .
    . . . . . b 4 b b b 4 4 b . . .
    . . . . b d 5 5 5 4 b 4 4 b . .
    . . . . b 3 2 3 5 5 4 e 4 4 b .
    . . . b d 2 2 2 5 7 5 4 e 4 4 e
    . . . b 5 3 2 3 5 5 5 5 e e e e
    . . b d 7 5 5 5 3 2 3 5 5 e e e
    . . b 5 5 5 5 5 2 2 2 5 5 d e e
    . b 3 2 3 5 7 5 3 2 3 5 d d e 4
    . b 2 2 2 5 5 5 5 5 5 d d e 4 .
    b d 3 2 d 5 5 5 d d d 4 4 . . .
    b 5 5 5 5 d d 4 4 4 4 . . . . .
    4 d d d 4 4 4 . . . . . . . . .
    4 4 4 4 . . . . . . . . . . . .
"""), SpriteKind.food)



def on_overlap(sprite, otherSprite):
    randNum = randint(1, 2)
    if randNum == 1:
        myItemSprite.set_image(img("""
            ...........fffffff...ccfff..........
            ..........fbbbbbbbffcbbbbf..........
            ..........fbb111bbbbbffbf...........
            ..........fb11111ffbbbbff...........
            ..........f1cccc1ffbbbbbcff.........
            ..........ffc1c1c1bbcbcbcccf........
            ...........fcc3331bbbcbcbcccf..ccccc
            ............c333c1bbbcbcbccccfcddbbc
            ............c333c1bbbbbbbcccccddbcc.
            ............c333c11bbbbbccccccbbcc..
            ...........cc331c11bbbbccccccfbccf..
            ...........cc13c11cbbbcccccbbcfccf..
            ...........c111111cbbbfdddddc.fbbcf.
            ............cc1111fbdbbfdddc...fbbf.
            ..............cccfffbdbbfcc.....fbbf
            ....................fffff........fff
        """))
        myPlayer.set_image(img("""
            . . . . . . 3 3 . . . . . . . .
            . . . . . . 3 1 3 . . . . . . .
            . . 3 3 . . 3 1 3 . . 3 3 . . .
            . . 3 1 3 . 3 1 3 2 3 1 3 . . .
            . . . 3 1 3 3 1 3 2 1 3 . . . .
            3 3 3 3 2 1 3 1 1 1 3 . . . . .
            3 1 1 1 1 1 1 1 1 2 3 3 3 3 3 3
            . 3 3 3 2 3 1 1 1 1 1 1 1 1 1 3
            . . . . . 2 1 1 1 3 3 2 3 3 3 .
            . . . . 3 1 3 1 3 1 2 . . . . .
            . . . 3 1 3 2 1 3 3 1 3 . . . .
            . . 3 1 3 . 2 1 3 . 3 1 3 . . .
            . . 3 3 . . 3 1 3 . . 3 3 . . .
            . . . . . . 3 1 3 . . . . . . .
            . . . . . . 3 1 3 . . . . . . .
            . . . . . . 3 3 . . . . . . . .
        """))
        pause(3000)
        myPlayer.set_image(img("""
            . . . . . . f f f f . . . . . .
            . . . . f f f 2 2 f f f . . . .
            . . . f f f 2 2 2 2 f f f . . .
            . . f f f e e e e e e f f f . .
            . . f f e 2 2 2 2 2 2 e e f . .
            . . f e 2 f f f f f f 2 e f . .
            . . f f f f e e e e f f f f . .
            . f f e f b f 4 4 f b f e f f .
            . f e e 4 1 f d d f 1 4 e e f .
            . . f e e d d d d d d e e f . .
            . . . f e e 4 4 4 4 e e f . . .
            . . e 4 f 2 2 2 2 2 2 f 4 e . .
            . . 4 d f 2 2 2 2 2 2 f d 4 . .
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
            . . . . . f f f f f f . . . . .
            . . . . . f f . . f f . . . . .
        """))
        
    elif randNum == 2:
        myItemSprite.set_image(img("""
            . . . . . . b b b b . . . . . .
            . . . . . . b 4 4 4 b . . . . .
            . . . . . . b b 4 4 4 b . . . .
            . . . . . b 4 b b b 4 4 b . . .
            . . . . b d 5 5 5 4 b 4 4 b . .
            . . . . b 3 2 3 5 5 4 e 4 4 b .
            . . . b d 2 2 2 5 7 5 4 e 4 4 e
            . . . b 5 3 2 3 5 5 5 5 e e e e
            . . b d 7 5 5 5 3 2 3 5 5 e e e
            . . b 5 5 5 5 5 2 2 2 5 5 d e e
            . b 3 2 3 5 7 5 3 2 3 5 d d e 4
            . b 2 2 2 5 5 5 5 5 5 d d e 4 .
            b d 3 2 d 5 5 5 d d d 4 4 . . .
            b 5 5 5 5 d d 4 4 4 4 . . . . .
            4 d d d 4 4 4 . . . . . . . . .
            4 4 4 4 . . . . . . . . . . . .
        """))
    
    otherSprite.set_position(randint(10, 110), randint(10, 110))
    
    



sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_overlap)

