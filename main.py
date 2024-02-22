import sys
import random
import pygame
from pygame.locals import *
import time

pygame.init()

# sets randomly if the enemy will move left or right
LeftOrRight = random.randint(0, 1)
last_random_number_time = time.time()

# light blue color
LightBlue = (66, 179, 245)
Red = (255, 0, 0)

# set the frames per second on the screen
FramesPerSecond = pygame.time.Clock()
FramesPerSecond.tick(60)
FPS = 60

# set the height and width of the screen
ScreenWidth = 600
ScreenHeight = 600

# set the display
GameDisplay = pygame.display.set_mode((ScreenHeight, ScreenWidth))
GameDisplay.fill(LightBlue)
pygame.display.set_caption("Game")

# the left enemy


class EnemyLeft(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Flip-flop.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, 150), 0)

    # the movement of the left enemy down
    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom > 800:
            self.rect.top = 0
            self.rect.center = (random.randint(50, 150), 0)

    # the drawing of the left enemy on the screen
    def draw(self, surface):
        surface.blit(self.image, self.rect)

# the right enemy


class EnemyRight(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Flip-flop.png")
        self.FlippedImage = pygame.transform.flip(self.image, True, False)
        self.rect = self.FlippedImage.get_rect()
        self.rect.center = (random.randint(450, 550), 0)

    # the movement of the right enemy down
    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom > 800:
            self.rect.top = 0
            self.rect.center = (random.randint(450, 550), 0)

    # the drawing of the right enemy on the screen
    def draw(self, surface):
        surface.blit(self.FlippedImage, self.rect)

# the player


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.PlayerImage = pygame.image.load("Cockroach.png")
        self.rect = self.PlayerImage.get_rect()
        self.rect.center = (300, 500)

    #   take the keys input and move the player by them
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-7, 0)
        if self.rect.right < ScreenWidth:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(7, 0)
        if self.rect.top < ScreenHeight:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -7)
        if self.rect.bottom > 0:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 7)

    #   the drawing of the player on the screen
    def draw(self, surface):
        surface.blit(self.PlayerImage, self.rect)

# create instances of Player and EnemyLeft/EnemyRight


P1 = Player()
E1 = EnemyLeft()
E2 = EnemyRight()

# Create sprite groups for enemies and all sprites
enemies = pygame.sprite.Group()
enemies.add(E1)
enemies.add(E2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(E2)


while True:
    # quit the in case of losing
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # if Player collides with EnemyLeft/EnemyRight the Player losing
    if pygame.sprite.spritecollideany(P1, enemies):
        GameDisplay.fill(Red)
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    # change the movement of the EnemyLeft/EnemyRight each 1 second randomly
    current_time = time.time()
    if current_time - last_random_number_time >= 1:
        LeftOrRight = random.randint(0, 1)
        last_random_number_time = current_time

    # moving and updating the game screen
    P1.update()
    if LeftOrRight == 0 and E2.rect.top == -204:
        E1.move()
    elif LeftOrRight == 1 and E1.rect.top == -204:
        E2.move()
    else:
        E2.rect.top = -204
        E1.rect.top = -204
    GameDisplay.fill(LightBlue)
    P1.draw(GameDisplay)
    if LeftOrRight == 0:
        E1.draw(GameDisplay)
    else:
        E2.draw(GameDisplay)
    pygame.display.update()
    FramesPerSecond.tick(FPS)
