from circleshape import CircleShape
from constants import *
import pygame
import random
class Asteroid(CircleShape):

    def __init__(self, x,y, radius):
        super().__init__(x,y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position, self.radius,2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()

        if self.radius > ASTEROID_MIN_RADIUS:
            
            random_angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid1.velocity = self.velocity.rotate(random_angle) * 1.2 #= asteroid1.velocity.rotate(random_angle)

            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = self.velocity.rotate(-random_angle) * 1.2 

