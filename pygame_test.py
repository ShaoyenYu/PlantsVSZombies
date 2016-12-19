import pygame as pg
from utils import animation

pg.init()
scale_ratio_x, scale_ratio_y = 2, 2
display_width = 512 * scale_ratio_x
display_height = 384 * scale_ratio_y
x, y = display_width * .5, display_height * .5
delta_x = 0
delta_y = 0

resolution = (display_width, display_height)
black, white, red = (0, 0, 0), (255, 255, 255), (255, 0, 0)
img_coneheadzombie = pg.image.load("src/zombies/ConeheadZombieAttack.gif")

# img_zombie = pg.image.load("src/zombies/Zombie.gif")
img_zombie = animation.SunFlower()
img_bucketheadzombie = pg.image.load("src/zombies/BucketheadZombie.gif")
img_sunshinezombie = pg.image.load("src/zombies/SunshineZombie.gif")
img_rj = pg.transform.scale(pg.image.load("src/plantscard/RjFlower.png"), (100, 120))
img_sunflower = pg.transform.scale(pg.image.load("src/plantscard/TwinsSunflower.png"), (100, 120))

img_icon = pg.image.load("src/icon.png")
img_grass = pg.image.load("src/background/grass.png")


# pg.transform()
# Surface
def image_display(img, x, y):
    window.blit(img, (x, y))

# DISPLAY

window = pg.display.set_mode(resolution, pg.RESIZABLE)
pg.display.set_caption("Plants v.s Zombie(DEV)")
pg.display.set_icon(img_icon)

clock = pg.time.Clock()

gameover = False

key_down = {k: False for k in ["LEFT", "RIGHT", "UP", "DOWN"]}

while not gameover:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameover = True
        if event.type == pg.KEYDOWN:
            if event.key in (pg.K_LEFT, pg.K_a):
                key_down["LEFT"] = True
                delta_x = -5
            if event.key in (pg.K_RIGHT, pg.K_d):
                key_down["RIGHT"] = True
                delta_x = 5
            if event.key in (pg.K_UP, pg.K_w):
                key_down["UP"] = True
                delta_y = -5
            if event.key in (pg.K_DOWN, pg.K_s):
                key_down["DOWN"] = True
                delta_y = 5
            if event.key == pg.K_1:
                pg.transform.scale(img_sunflower, (10, 10))
                print(pg.Surface.get_size(window), pg.display.get_surface().get_height())

        if event.type == pg.KEYUP:
            if event.key in (pg.K_LEFT, pg.K_a):
                key_down["LEFT"] = False
                if key_down["RIGHT"]:
                    delta_x = 5
                else:
                    delta_x = 0
            if event.key in (pg.K_RIGHT, pg.K_d):
                key_down["RIGHT"] = False
                if key_down["LEFT"]:
                    delta_x = -5
                else:
                    delta_x = 0
            if event.key in (pg.K_UP, pg.K_w):
                key_down["UP"] = False
                if key_down["DOWN"]:
                    delta_y = 5
                else:
                    delta_y = 0
            if event.key in (pg.K_DOWN, pg.K_s):
                key_down["DOWN"] = False
                if key_down["UP"]:
                    delta_y = -5
                else:
                    delta_y = 0

            if event.key == pg.K_ESCAPE:
                pg.quit()
                quit()

        if event.type == pg.VIDEORESIZE:
            print(event.size)

    # print(event)

    x += delta_x
    y += delta_y

    window.fill(white)
    image_display(img_grass, 0, 0)
    image_display(img_sunflower, 60, 30)
    image_display(img_rj, 60, 150)
    image_display(img_zombie, x, y)
    image_display(img_bucketheadzombie, x + 100, y + 135)
    image_display(img_sunshinezombie, x + 150, y + 270)
    pg.display.update()  # pg.display.flip()
    clock.tick(60)

pg.quit()
