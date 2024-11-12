import pygame.image

class Menu:
    def __init__(self, window):
        self.window = window
        #load image
        self.surf = pygame.image.load('./asset/MenuBg.png')
        #create rect
        self.rect = self.surf.get_rect(left = 0, top = 0)

    def run(self):
        #display image on rect
        self.window.blit(source=self.surf, dest=self.rect)
        #update display
        pygame.display.flip()
        pass
