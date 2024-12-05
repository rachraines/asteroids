from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def split(self, dt):
        # removes the original asteroid from the game
        self.kill()
        
        # if the asteroid was the smallest size, it is just destroyed, not split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # asteroid splits into 2 new smaller asteroids that go in random directions
        else:
            # creates smaller radius
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            # creates a random split angle and applies to the two new asteroids
            new_angle = random.uniform(20, 50)
            rotate_one = self.velocity.rotate(new_angle)
            rotate_two = self.velocity.rotate(-new_angle)

            # creates two new instances of asteroids
            asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)

            # creates new velocities using the new angles:
            asteroid_one.velocity = rotate_one * 1.2
            asteroid_two.velocity = rotate_two
  
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)