import pygame
pygame.init()
#create display
window = pygame.display.set_mode((400,400))
#give display a color
window.fill((255,255,255))
#define color
GREEN = (0,255,0)
#solid circle
pygame.draw.circle(window, GREEN, (300, 300), 50)
#draw outlined circle
pygame.draw.circle(window, GREEN, (100,100),50,3 )
#to draw obj on screen
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()