import pygame
from pygame.math import Vector2
import time
import math

def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)

# grass = scale_image(pygame.image.load("grass.jpg"), 2.5)
# track = scale_image(pygame.image.load("track.png"), 0.82)
# track_border = scale_image(pygame.image.load("track-border.jpg"), 0.9)


pygame.display.set_caption("Racer")
fps = 60
clock = pygame.time.Clock()

width = 1200
height = 1000
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)

# CAR = pygame.transform.scale(pygame.image.load(r"images/car.png"),
#                              (50, 50)).convert_alpha()

class Car:
    def __init__(self, x, y, angle):
        self.pos = Vector2(x,y)
        self.angle = angle
        self.speed = 0
        self.image = pygame.image.load(r"images/car.png")


class Player(Car):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle += 0.2 * self.speed
        if keys[pygame.K_RIGHT]:
            self.angle -= 0.2 * self.speed
        if keys[pygame.K_UP]:
            self.speed += 0.1
        if keys[pygame.K_DOWN]:
            self.speed -= 0.2
            if self.speed < 0:
                self.speed = 0

        dir = Vector2(math.cos(math.radians(self.angle)), math.sin(math.radians(-self.angle)))
        self.pos += dir * self.speed
        self.speed *= 0.999

    def draw(self):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        self.image = pygame.transform.scale(self.image, (50, 30))
        # self.pos - Vector2(rotated_image.get_width(), rotated_image.get_height())/2
        screen.blit(rotated_image, (width//2 - rotated_image.get_width()//2, height//2 - rotated_image.get_height()//2))


class NPC(Car):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.speed = 4

    def update(self):
        self.angle -= 0.2 * self.speed
        dir = Vector2(math.cos(math.radians(self.angle)), math.sin(math.radians(-self.angle)))
        self.pos += dir * self.speed

    def draw(self):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        bg_screen.blit(rotated_image, self.pos - Vector2(rotated_image.get_width(), rotated_image.get_height())/2)


player = Player(200,300,0)
npc = NPC(400, 400, 0)

bg = pygame.image.load(r"images/track.png")
bg = pygame.transform.scale(bg, (1200, 1000))

bg_screen = pygame.Surface(screen_size) # bg.get_size())
run = True
while run:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    player.update()
    npc.update()



    # draw to screen
    screen.fill((0,0,0))
    bg_screen.fill((0, 0, 255))
    print(player.pos)
    # [800, 800]
    # draw image on the screen
    # draw image at [-400, -400]

    bg_screen.blit(bg, (0, 0))
    draw_image_at = [width // 2 - player.pos[0], height // 2 - player.pos[1]]
    npc.draw()
    screen.blit(bg_screen, draw_image_at)
    player.draw()

    pygame.display.update()
