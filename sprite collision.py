import pygame
import random
SCREEN_WIDTH, SCREEN_HEIGHT = 500,400
MOVEMENT_SPEED = 5
FONT_SIZE = 72
pygame.init()
background_image = pygame.transform.scale(pygame.image.load(''),(SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont('Times new Roman', FONT_SIZE)
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('dodgerblue'))
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect = self.image.get_rect()
    def move(self,x_change,y_change):
        self.rext.x = max(min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width),0)
        self.rext.y = max(min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height),0)
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Sprite Collision')
all_sprites = pygame.sprite.Group()
sprite_1 = Sprite(pygame.Color('black'),20,30)
sprite_1.rect.x, sprite_1.rect.y = random.randint(0, SCREEN_WIDTH - sprite_1.rect.width), random.randint(0,SCREEN_HEIGHT - sprite_1.rect.height)
all_sprites.add(sprite_1)
sprite_2 = Sprite(pygame.Color('red'),20,30)
sprite_2.rect.x, sprite_1.rect.y = random.randint(0, SCREEN_WIDTH - sprite_1.rect.width), random.randint(0,SCREEN_HEIGHT - sprite_1.rect.height)
all_sprites.add(sprite_2)
running, won = True, Falseclock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False
    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT]- keys[pygame.K_LEFT]) * MOVEMENT_SPEED
        y_change = (keys[pygame.K_DOWN]- keys[pygame.K_UP]) * MOVEMENT_SPEED
        sprite_1.move(x_change, y_change)
        
        if sprite_1.rect.colliderect(sprite_2.rect):
            all_sprites.remove(sprite_2)
            won = True
    screen