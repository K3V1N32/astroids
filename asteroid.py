import random

import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_COLOR, LINE_WIDTH
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, LINE_COLOR, self.position, self.radius, LINE_WIDTH)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        asteroid1_vel = self.velocity.rotate(random_angle)
        asteroid2_vel = self.velocity.rotate(-random_angle)
        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid1.velocity = asteroid1_vel * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid2.velocity = asteroid2_vel * 1.2


    def update(self, dt: float) -> None:
        self.position += self.velocity * dt