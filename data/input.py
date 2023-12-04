import pygame
import pygame_gui
import sys

pygame.init()

manager = pygame_gui.UIManager((850,650))

text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((175, 275), (500, 50)), manager=manager,
                                               object_id='#main_text_entry')

clock = pygame.time.Clock()

def inputIn(mainSurface):
    while True:
        UI_REFRESH_RATE = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry'):
                return event.text
            
            manager.process_events(event)
        
        font=pygame.font.Font("Genshin.ttf", 30)
        text=font.render("Your nickname:", True, (200,0,0))

        manager.update(UI_REFRESH_RATE)

        mainSurface.fill("white")
        mainSurface.blit(text, (10,10))

        manager.draw_ui(mainSurface)

        pygame.display.update()