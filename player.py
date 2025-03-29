from circleshape import CircleShape
from shot import Shot
from constants import *
import pygame

class Player(CircleShape):

    def __init__(self, x,y):
        super().__init__(x,y, PLAYER_RADIUS )
        self.rotation = 0
        self.shot_timer = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(sefl, dt):
        sefl.rotation += PLAYER_TURN_SPEED * dt

    def move(sefl, dt):
        forward = pygame.Vector2(0, 1).rotate(sefl.rotation)
        sefl.position += forward * PLAYER_SPEED * dt

    def shoot(sefl):
        new_shoot = Shot(sefl.position.x, sefl.position.y)
        new_shoot.velocity = pygame.Vector2(0,1).rotate(sefl.rotation)*PLAYER_SHOOT_SPEED
        

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]: 
            if self.shot_timer <=0 :
                self.shoot()
                self.shot_timer = PLAYER_SHOOT_COOLDOWN
            self.shot_timer -= dt

