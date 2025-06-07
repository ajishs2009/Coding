import pygame
pygame.init()
white = (255,255,255)
clock = pygame.time.Clock()
display_surface = pygame.display.set_mode((400,500))
pygame.display.set_caption('Ronaldo')
image = pygame.image.load('motivation.jpg')
DEFAULT_IMG_SIZE = (200,200)
image = pygame.transform.scale(image,DEFAULT_IMG_SIZE)
DEFAULT_IMG_POSITION = (150,150)
while True:
    display_surface.fill(white)
    display_surface.blit(image, DEFAULT_IMG_POSITION)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.flip()
    clock.tick(15)
