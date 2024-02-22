import sys
import random
import pygame


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        
        self.screen = screen

        self.width = 200
        self.height = 100
        self.speed = 300

        # initial position
        self.pos = pygame.Vector2(self.width/2+50, screen.get_height()/2)

        # TODO: I need to add surface and rect


    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pos.y -= self.speed  *dt
        if keys[pygame.K_s]:
            self.pos.y += self.speed*dt
        if keys[pygame.K_a]:
            self.pos.x -= self.speed*dt
        if keys[pygame.K_d]:
            self.pos.x += self.speed*dt

    def draw(self):
        body_rect = pygame.Rect(self.pos.x-(self.width/2), self.pos.y-(self.height/2), 
                                self.width, self.height)
        fire_rect = pygame.Rect(self.pos.x-(self.width/2)-self.width//4, self.pos.y-(self.height/2), 
                                self.width//3, self.height)
        pygame.draw.ellipse(self.screen, "green", body_rect)
        pygame.draw.ellipse(self.screen, "orange", fire_rect)


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, screen, asteroids=None):
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen
        width = random.randrange(100, 300)
        height = random.randrange(100, 300)
        y = random.randrange(width, self.screen.get_height()-height)
        self.rect = pygame.Rect(self.screen.get_width(), y,
                                width, height)
        self.speed = random.randrange(300, 600)

        self.image = pygame.Surface([width, height]) 

        # TODO: I need to add surface and rect

    def update(self, dt):
        self.rect = self.rect.move(-1*self.speed*dt, 0)
        if self.rect.right < 0:
            self.initialize()

    def draw(self):
        pygame.draw.ellipse(self.screen, "blue", self.rect)


def check_exit():
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]: # quit the game
        pygame.quit()
        sys.exit(0)


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((2048, 1080))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    ship = Spaceship(screen)
    asteroids = pygame.sprite.Group()
    for _ in range(random.randrange(3, 10)):
        asteroids.add(Asteroid(screen))

    while running:
        # poll for events
        check_exit()

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # update and draw the spaceship
        ship.update(dt)
        ship.draw()

        # update and draw the asteroid
        asteroids.update(dt)
        asteroids.draw()

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()


# main function
if __name__ == "__main__":
    main()
