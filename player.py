from circleshape import *
from constants import *
from bullet import *

class Player(CircleShape):
    def __init__(self, x, y):
        # call the CircleShape class's constructor
        super().__init__(x, y, PLAYER_RADIUS)
        # initializes rotation field
        self.rotation = 0
        self.timer = 0
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        new_rotation = PLAYER_TURN_SPEED * dt
        self.rotation += new_rotation

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def shoot(self, dt):
        # creates a shot instance at the location of the player
        if self.timer > 0:
            return
        else:
            shot = Shot(self.position.x, self.position.y)
            # gives the shot movement and the direction of the player
            forward = pygame.Vector2(0,1).rotate(self.rotation)
            shot.velocity = forward * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.timer > 0:
            self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-1 * dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-1*dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)