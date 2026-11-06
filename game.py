import pygame
import math
pygame.init()

print("Pygame is working!")

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Game")

x = 375

y = 275

running = True
while running:
    vel = 0.5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and keys[pygame.K_LEFT] or keys[pygame.K_LEFT] and keys[pygame.K_UP] or keys[pygame.K_RIGHT] and keys[pygame.K_UP] or keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
        vel = vel/math.sqrt(2)
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0,0,225), (x, y, 50,50))
    pygame.display.flip()


    if x < 0:
        x = 0

    
    if y < 0:
        y = 0

    if x > 750:
        x = 750

    if y > 550:
        y = 550

pygame.quit()