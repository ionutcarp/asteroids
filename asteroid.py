import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        rnd_deg = random.uniform(20, 50)
        vector_1 = self.velocity.rotate(rnd_deg)
        vector_2 = self.velocity.rotate(-rnd_deg)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast_1.velocity = vector_1 * 1.2
        ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
        ast_2.velocity = vector_2 * 1.2
