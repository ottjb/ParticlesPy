import pygame as pg
from settings import *
import particle_utilities as pu

pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Particles")
clock = pg.time.Clock()
running = True

particles = pu.initializeParticles()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    screen.fill(BACKGROUND_COLOR)

    pu.drawLines(particles, screen)
    for p in particles:
        p.display(screen)
        p.update()

    pg.display.flip()
    clock.tick(60)
pg.quit()