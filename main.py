import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    #sets up game clock
    game_clock = pygame.time.Clock()
    dt = 0

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

        playa_1.draw(screen)
        playa_1.update(dt)

        pygame.display.flip()  
        dt = game_clock.tick(60)/1000
#       print(dt)

if __name__ == "__main__":
    main()
