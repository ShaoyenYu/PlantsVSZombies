import pygame as pg

pg.init()

display_height = 384 * 1
display_width = 512 * 1
x, y = display_width * .5, display_height * .5
delta_x = 0
delta_y = 0

resolution = (display_width, display_height)
black, white, red = (0, 0, 0), (255, 255, 255), (255, 0, 0)
img_zombie = pg.image.load("src/ConeheadZombieAttack.gif")
img_sunflower = pg.image.load("src/images_sunflower.png")
img_icon = pg.image.load("src/icon.png")


# DISPLAY

window = pg.display.set_mode((0, 0), pg.RESIZABLE)
pg.display.set_caption("Plants v.s Zombie(DEV)")
pg.display.set_icon(img_icon)

# Surface
def image_display(img, x, y):
    window.blit(img, (x, y))


clock = pg.time.Clock()

crashed = False

key_down = {k: False for k in ["LEFT", "RIGHT", "UP", "DOWN"]}

while not crashed:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            crashed = True
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
    image_display(img_sunflower, 10, 10)
    image_display(img_zombie, x, y)

    pg.display.update()  # pg.display.flip()
    clock.tick(60)



pg.quit()
