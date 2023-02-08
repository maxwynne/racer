import pygame
from pygame.math import Vector2
import time
import math

def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)

# grass = scale_image(pygame.image.load("grass.jpg"), 2.5)
# track = scale_image(pygame.image.load("track.jpg"), 0.82)
# track_border = scale_image(pygame.image.load("track-border.jpg"), 0.9)

pygame.display.set_caption("Racer")
fps = 60
clock = pygame.time.Clock()

width = 1200
height = 720
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)

class Car:
    def __init__(self, x, y, angle):
        self.pos = Vector2(x,y)
        self.angle = angle
        self.speed = 0
        self.image = pygame.image.load("car.png")

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle += 0.2 * self.speed
        if keys[pygame.K_RIGHT]:
            self.angle -= 0.2 * self.speed
        if keys[pygame.K_UP]:
            self.speed += 0.1

        dir = Vector2(math.cos(math.radians(self.angle)), math.sin(math.radians(-self.angle)))
        self.pos += dir * self.speed
        self.speed *= 0.999

    def draw(self):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        screen.blit(rotated_image, self.pos - Vector2(rotated_image.get_width(), rotated_image.get_height())/2)

player = Car(200,300,0)

run = True
while run:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    player.update()

    # draw to screen
    screen.fill((0,0,0))
    player.draw()
    pygame.display.update()
