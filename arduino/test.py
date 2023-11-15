import serial
import pygame, math
import time


pygame.init()
screen = pygame.display.set_mode((400, 300))
font = pygame.font.Font(None, 36)

screen.fill((255, 255, 255))

# Render the moving average number to the screen
text = font.render(f"3.342 +/- 1.05 [cm]", True, (0, 0, 0))
screen.blit(text, (50, 50))
pygame.display.flip()

time.sleep(1000)
