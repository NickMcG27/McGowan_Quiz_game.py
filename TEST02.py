import pygame
pygame.init()
screen = pygame.display.set_mode((1200, 800))
screen.fill((0,0,0))

def button(screen, position, text):
    font = pygame.font.SysFont("Segoe UI", 33)
    text_render = font.render(text, 1, (255, 215, 0))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w, h))
    return screen.blit(text_render, (x, y))


def start():
    while True:
        screen = pygame.display.set_mode((1200, 800))
        screen.fill((80,150,255))
        b3 = button(screen, (40, 250), " A ")
        b4 = button(screen, (40, 300), " B ")
        b5 = button(screen, (40, 350), " C ")
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b3.collidepoint(pygame.mouse.get_pos()):
                        Scenario1()
                    if b4.collidepoint(pygame.mouse.get_pos()):
                        Scenario2()
                    elif b5.collidepoint(pygame.mouse.get_pos()):
                        Scenario3()
        pygame.display.update()
    pygame.quit()


def Scenario1():
    """ b3 press """
    b3 = button(screen, (40, 250), "1A")
    b4 = button(screen, (40, 300), "1B")
    b5 = button(screen, (40, 350), "1C")
    screen = pygame.display.set_mode((1200, 800))
    screen.fill((80, 150, 255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b3.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                elif b3.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()

        pygame.display.update()
    pygame.quit()




def menu():
    """ This is the menu that waits you to click the s key to start """
    b1 = button(screen, (620, 700), " Quit ")
    b2 = button(screen, (530, 700), " Start ")
    while True:
        color = (255, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Welcome to (HOW TO MID)'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (400, 600))
        color = (255, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'The only game that tells you how much of a helmet you are'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (200, 635))
        crest = pygame.image.load('crest.png')
        screen.blit(crest, (400, 10))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                if key_to_start:
                    start()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    start()
        pygame.display.update()
    pygame.quit()

menu()
