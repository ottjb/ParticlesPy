from settings import *
from particle import Particle
import random as r
import math as m
import pygame as pg

def addVector(v1: list, v2: list):
    return [v1[0] + v2[0], v1[1] + v2[1]]

def multiplyVector(vec: list, num: int):
    return [vec[0] * num, vec[1] * num]

def initializeParticles():
    particles = []
    for _ in range(MAX_PARTICLES):
        x = r.randint(0, SCREEN_WIDTH)
        y = r.randint(0, SCREEN_HEIGHT)
        z = r.randint(20, 100)

        vel_x = ((r.random() * 2) - 1) * SPEED_SCALAR
        vel_y = ((r.random() * 2) - 1) * SPEED_SCALAR

        particles.append(Particle(x, y, z, vel_x, vel_y))
    return particles

def calcDistance(particle1: Particle, particle2: Particle):
    x1, y1, z1 = particle1.getCoordsXYZ()
    x2, y2, z2 = particle2.getCoordsXYZ()
    x = (x1 - x2) ** 2
    y = (y1 - y2) ** 2
    z = (z1 - z2) ** 2
    presqrt = x + y + z
    return m.sqrt(presqrt)

def line(p1: Particle, p2: Particle, screen: pg.Surface, distance: float):
        line_color = PARTICLE_COLOR.lerp(BACKGROUND_COLOR, distance)

        x1, y1 = p1.getCoordsXY()
        x2, y2 = p2.getCoordsXY()

        dx = x2 - x1
        dy = y2 - y1
        length = m.sqrt(dx**2 + dy**2)

        unit_vector = (dx / length, dy / length)
        start_point = (x1 + unit_vector[0] * PARTICLE_SIZE, y1 + unit_vector[1] * PARTICLE_SIZE)
        end_point = (x2 - unit_vector[0] * PARTICLE_SIZE, y2 - unit_vector[1] * PARTICLE_SIZE)

        pg.draw.aaline(screen, line_color, start_point, end_point)

def drawLines(particles: list, screen: pg.surface):
        for i, p1 in enumerate(particles):
            for p2 in particles[i + 1:]:
                distance = calcDistance(p1, p2)
                if distance <= 100:
                    line(p1, p2, screen, (distance / 100))