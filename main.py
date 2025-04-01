import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable, )
	Shot.containers = (updatable, drawable, shots)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		updatable.update(dt)

		

		for asteroid  in asteroids:
			collistion = player.check_collision(asteroid)
			if collistion:
				print('Game over!')
				
				sys.exit()
			for shot in shots:
				if shot.check_collision(asteroid):
					asteroid.split()
					shot.kill()
		screen.fill("black")

		for draw_obj in drawable:
			draw_obj.draw(screen)		
		pygame.display.flip() 

		# compute FPS
		dt = clock.tick(60)/1000

if __name__ == "__main__":
	main()
