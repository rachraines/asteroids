import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from bullet import *
from asteroidfield import *
from circleshape import *
import sys
 
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # makes Player class and Asteroid class to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # instantiate the player object in the middle of the screen
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            # exits the game when x is clicked
            if event.type == pygame.QUIT:
                return
    
        # displays black screen
        screen.fill(000)

        # draws the player
        for obj in updatable:
            obj.update(dt)
        for asteroid in asteroids:
            # ends game if player hits an asteroid
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()
            # destroys asteroids if collision with a shot
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split(dt)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()