# import pygame
# import time 
# import random

# WIDTH,HEIGHT=1000,800
# WIN=pygame.display.set_mode(100,100)
# pygame.display.set_caption("Space Dodge")

# def main():
#     run = True
    
#     while run:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run=False
#                 break
#     pygame.QUIT        



# if __name__=="__main__":
#     main()    /
import pygame
import time 
import random

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")
BG= pygame.transform.scale(pygame.image.load("pg.jpg"),(WIDTH,HEIGHT))

def draw():
    WIN.blit(BG,(0,0))
    pygame.display.update()
def main():
    pygame.init()  # Initialize Pygame
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw()    

        # Update display
        pygame.display.update()

    pygame.quit()  # Quit Pygame

if __name__ == "__main__":
    main()
