import pygame
import random

# Initialize Pygame jay
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set screen dimensions
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

# Set up screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Set up fonts
font = pygame.font.SysFont(None, 50)

# Set up clock
clock = pygame.time.Clock()

# Define bird class
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (100, SCREEN_HEIGHT // 2)
        self.velocity = 0
        self.gravity = 0.5

    def update(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def jump(self):
        self.velocity = -10

# Define pipe class
class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, random.randint(200, 400)))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        self.speed = 5

    def update(self):
        self.rect.x -= self.speed

# Set up groups
all_sprites = pygame.sprite.Group()
pipes = pygame.sprite.Group()

# Create bird object
bird = Bird()
all_sprites.add(bird)

# Set up game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    # Update game objects
    all_sprites.update()

    # Spawn pipes
    if random.randint(1, 100) == 1:
        pipe = Pipe()
        all_sprites.add(pipe)
        pipes.add(pipe)

    # Check for collisions
    if pygame.sprite.spritecollide(bird, pipes, False):
        running = False

    # Draw screen
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Draw score
    score_text = font.render(str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Set frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()

