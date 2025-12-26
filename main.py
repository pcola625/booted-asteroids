import pygame
from logger import log_state
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    #sets up game clock
    game_clock = pygame.time.Clock()
    dt = 0

    #setting up groups
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    assField = pygame.sprite.Group()
    
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    
    assField_1 = AsteroidField()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #playa 1
    playa_1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    #main loop
    while True:
	# make the close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()

        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)
     
        for thing in updatable:
            thing.update(dt)
        
        pygame.display.flip()  
        dt = game_clock.tick(60)/1000
#       print(dt)

if __name__ == "__main__":
    main()
