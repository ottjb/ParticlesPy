import particle_utilities as pu
import pygame as pg
from settings import *

class Particle():
    def __init__(self, x: int, y: int, z: int, vel_x: int, vel_y: int):
        self.pos = [x, y]
        self.z = z # Will be used as brightness, and in distance calculation for brightness

        self.vel = [vel_x, vel_y]
        #self.acc = [0, 0]

    def update(self):
        self.pos = pu.addVector(self.pos, self.vel)
        if self.pos[0] > SCREEN_WIDTH:
            self.pos[0] = 0
        elif self.pos[0] < 0:
            self.pos[0] = SCREEN_WIDTH
        elif self.pos[1] > SCREEN_HEIGHT:
            self.pos[1] = 0
        elif self.pos[1] < 0:
            self.pos[1] = SCREEN_HEIGHT
    
    def display(self, screen: pg.Surface):
        particle_c = PARTICLE_COLOR.lerp(BACKGROUND_COLOR, 1 - (self.z / 100))
        pg.draw.circle(screen, particle_c, self.pos, PARTICLE_SIZE)

    def getCoordsXYZ(self):
        return (self.pos[0], self.pos[1], self.z)
    
    def getCoordsXY(self):
        return (self.pos[0], self.pos[1])
    
    