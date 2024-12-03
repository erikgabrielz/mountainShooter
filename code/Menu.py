import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_WIDTH, C_ORANGE, C_WHITE, C_YELLOW, MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        #load image
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        #create rect
        self.rect = self.surf.get_rect(left = 0, top = 0)

    def run(self):
        menu_option = 0
        # load music
        pygame.mixer_music.load('./asset/Menu.mp3')
        # play music
        pygame.mixer_music.play(-1)
        while True:
            # display image on rect
            self.window.blit(source=self.surf, dest=self.rect)
            #create text title
            self.menu_text(50, "Mountain", C_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", C_ORANGE, ((WIN_WIDTH / 2), 100))

            #create optiton text
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))


            self.menu_text(14, "ALUNO: ERIK GABRIEL ZANOVELLO", C_WHITE, ( 90, 305))
            self.menu_text(14, "RU: 4573354", C_WHITE, (33, 315))
            # update display
            pygame.display.flip()

            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close Window
                    quit()  # end pygame

                if event.type == pygame.KEYDOWN: #down key
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP: #up key
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN: #enter
                        return MENU_OPTION[menu_option]


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)