import pygame
from pygame import mixer
pygame.init()
screen = pygame.display.set_mode((1200, 800))
screen.fill((0,0,0))
HP = []
BP = []


pygame.mixer.music.load("a-hero-of-the-80s-126684.mp3")
pygame.mixer.music.play()


def button(screen, position, text):
    font = pygame.font.SysFont("Segoe UI", 25)
    text_render = font.render(text, 1, (255, 215, 0))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w, h))
    return screen.blit(text_render, (x, y))


def start(HP, BP):
    while True:
        screen = pygame.display.set_mode((1200, 800))
        screen.fill((0,0,0))
        b3 = button(screen, (40, 230), " A ")
        b4 = button(screen, (40, 340), " B ")
        b5 = button(screen, (40, 470), " C ")
        bQ1 = button(screen, (90, 230), " Confirm his suspicions and ask for  ")
        bQ1a = button(screen, (90, 270), " 2 weeks to get a love chit finalized")
        bQ3 = button(screen, (90, 340), " Tell him that he must be thinking of  ")
        bQ3a = button(screen, (90, 380), "someone else and ask why he is having so much")
        bQ3b = button(screen, (90, 420), "trouble with names and faces in the company")
        bQ4 = button(screen, (90, 470), " Point at the window and scream pterodactyl  ")
        bQ4a = button(screen, (90, 510), "and run out of his officer while he is distracted")
        color = (255, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Your CO asks you to meet them in their office. '}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (250, 60))
        color = (255, 215, 0)
        crest = pygame.image.load('Forbidden.png')
        screen.blit(crest, (620, 200))
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'During the meeting he mentions that he suspects'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (250, 100))
        color = (255, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'you are fratting with a firstie, (you are). Choose your response'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (250, 140))
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b3.collidepoint(pygame.mouse.get_pos()):
                        HP.append(100)
                        print(HP)
                        print(BP)
                        Scenario1()

                    if b4.collidepoint(pygame.mouse.get_pos()):
                        BP.append(80)
                        print(HP)
                        print(BP)
                        Scenario2()

                    elif b5.collidepoint(pygame.mouse.get_pos()):
                        BP.append(100)
                        print(HP)
                        print(BP)
                        Scenario3()




        pygame.display.update()
    pygame.quit()

def Scenario3():
    """ after clicking C1 """

    while True:
        screen.fill((0, 0, 0))
        b6 = button(screen, (460, 700), " CLICK TO CONTINUE ")

        color = (25, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Selected Answer = C...  What made you think that was a good idea?'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (80, 250))
        color = (255, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Admitted to Insane Asylum: After running away your company officer hired a private'}",
            False, color)  # "text", color
        screen.blit(textsurface, (20, 300))
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'investigator to watch you and your suspected lover. There was AMPLE evidence.'}",
            False, color)  # "text", color
        screen.blit(textsurface, (20, 340))
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'After recieivng an honor and conduct offense you earned yourself an impressive'}",
            False, color)  # "text", color
        screen.blit(textsurface, (20, 380))
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'amount of restriction. While on tours one night your mind could no longer bear the'}",
            False, color)  # "text", color
        screen.blit(textsurface, (20, 420))
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'you mentally snapped and attacked the gunnery sergeant calling the candence'}",
            False, color)  # "text", color
        screen.blit(textsurface, (20, 460))
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'(he kicked your ass) and now you are in a hospital for the mentally unstable'}",
            False, color)  # "text", color
        screen.blit(textsurface, (20, 500))
        crest = pygame.image.load('Petarodactyl.png')
        screen.blit(crest, (450, 40))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b6.collidepoint(pygame.mouse.get_pos()):
                    Question2(HP, BP)

        pygame.display.update()
    pygame.quit()


def Scenario2():
    """ after clicking B1 """

    while True:
        screen.fill((0, 0, 0))
        b6 = button(screen, (460, 700), " CLICK TO CONTINUE ")

        color = (25, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Selected Answer = B'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (400, 500))
        color = (255, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'You played on his ego.  He apologizes for the mixup and '}",
            False, color)  # "text", color
        screen.blit(textsurface, (180, 580))
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'assures you he will put the rumors to rest.'}",
            False, color)  # "text", color
        screen.blit(textsurface, (280, 620))

        crest = pygame.image.load('PartyOnWane.png')
        screen.blit(crest, (270, 40))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b6.collidepoint(pygame.mouse.get_pos()):
                    Question2(HP, BP)

        pygame.display.update()
    pygame.quit()

def Scenario1():
    """ after clicking A1 """

    while True:

        screen.fill((0, 0, 0))
        b6 = button(screen, (460, 700), " CLICK TO CONTINUE ")







        color = (25, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Selected Answer = A'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (420, 450))
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Yeah, sure you would'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (400, 560))


        crest = pygame.image.load('SureBudy.png')
        screen.blit(crest, (400, 40))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b6.collidepoint(pygame.mouse.get_pos()):
                    Question2(HP, BP)

        pygame.display.update()
    pygame.quit()


def Question2(HP, BP):
    """ after clicking A """
    while True:
        screen = pygame.display.set_mode((1200, 800))
        screen.fill((0, 0, 0))
        b71 = button(screen, (40, 230), " A ")
        b8 = button(screen, (40, 340), " B ")
        b9 = button(screen, (40, 430), " C ")
        bQ1 = button(screen, (90, 230), " Gas light the CDO into believing that there is an extra  ")
        bQ1a = button(screen, (90, 270), " hour tonight because of daylight savings time")
        bQ3 = button(screen, (90, 340), " Try to bribe him with half a bag of sour skittles you have ")
        bQ3a = button(screen, (90, 380), " left in your pocket")
        bQ3b = button(screen, (90, 430), "Apologize and accept whatever unfortold immense consequences")
        bQ4 = button(screen, (90, 470), " will beseach you")

        color = (255, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'You arrive on deck three minutes past TAPS, your CDO is very upset. '}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (150, 100))
        color = (255, 215, 0)
        crest = pygame.image.load('Paperwork.png')
        screen.blit(crest, (360, 470))
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Chooose your response'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (350, 140))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b71.collidepoint(pygame.mouse.get_pos()):
                    BP.append(100)
                    print(HP)
                    print(BP)
                    Scenario4()
                if b8.collidepoint(pygame.mouse.get_pos()):
                    BP.append(90)
                    print(HP)
                    print(BP)
                    Scenario5()
                elif b9.collidepoint(pygame.mouse.get_pos()):
                    HP.append(70)
                    print(HP)
                    print(BP)
                    Scenario6()
        pygame.display.update()




def Scenario4():
    """ after clicking A1 """

    while True:
        screen.fill((0, 0, 0))
        b7 = button(screen, (460, 700), " CLICK TO CONTINUE ")






        color = (25, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Selected Answer = A'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (420, 460))
        color = (255, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'That Should not have worked, but it did'}",
            False, color)  # "text", color
        screen.blit(textsurface, (320, 590))
        crest = pygame.image.load('HowDidYou.png')
        screen.blit(crest, (320, 70))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b7.collidepoint(pygame.mouse.get_pos()):
                    Question3(HP, BP)

        pygame.display.update()
    pygame.quit()


def Scenario5():
    """ after clicking B """

    while True:
        screen.fill((0, 0, 0))
        b7 = button(screen, (460, 700), " CLICK TO CONTINUE ")

        color = (25, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Selected Answer = B'}",
            False, color)  # "text", antialias, color





        screen.blit(textsurface, (400, 500))
        color = (255, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'He loves sour skittles.  No UA this time'}",
            False, color)  # "text", color
        screen.blit(textsurface, (350, 540))
        crest = pygame.image.load('Skittles.png')
        screen.blit(crest, (350, 60))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):



                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b7.collidepoint(pygame.mouse.get_pos()):
                    Question3(HP, BP)

        pygame.display.update()
    pygame.quit()

def Scenario6():
    """ after clicking A1 """

    while True:
        screen.fill((0, 0, 0))
        b7 = button(screen, (460, 700), " CLICK TO CONTINUE ")

        color = (25, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Selected Answer = C'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (420, 400))
        color = (255, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Your CDO takes pitty on you.  No UA this time'}",
            False, color)  # "text", color
        screen.blit(textsurface, (220, 535))
        crest = pygame.image.load('Lucky.png')
        screen.blit(crest, (420, 70))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b7.collidepoint(pygame.mouse.get_pos()):
                    Question3(HP, BP)

        pygame.display.update()
    pygame.quit()


def Question3(HP, BP):
    """ after clicking A """
    while True:
        screen = pygame.display.set_mode((1200, 800))
        screen.fill((0, 0, 0))
        b10 = button(screen, (40, 270), " A ")
        b11 = button(screen, (40, 320), " B ")
        b12 = button(screen, (40, 370), " C ")
        bQ1 = button(screen, (90, 270), " Turn around and hide in the bathroom until he leaves  ")
        bQ1a = button(screen, (90, 320), "Own up to it and BEG for your life")
        bQ3 = button(screen, (90, 370), " Tell your Batt-O that you only went into the bathroom because you ")
        bQ3a = button(screen, (90, 410), " had to stop and armed assalant who was posted up in stall 2")

        crest = pygame.image.load('watch.png')
        screen.blit(crest, (400, 470))
        color = (255, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{' You come out of the bathroom to find your battalion officer waiting'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (50, 100))
        color = (255, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{' at the mates desk looking over the log book and the watchbelt that you left'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (50, 140))
        color = (255, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'on the desk while you took a bathroom break.   '}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (50, 180))
        color = (255, 215, 0)

        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Chooose your response'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (350, 220))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b10.collidepoint(pygame.mouse.get_pos()):
                    BP.append(5)
                    print(HP)
                    print(BP)
                    Scenario7()
                if b11.collidepoint(pygame.mouse.get_pos()):
                    HP.append(60)
                    print(HP)
                    print(BP)
                    Scenario8()
                elif b12.collidepoint(pygame.mouse.get_pos()):
                    BP.append(200)
                    print(HP)
                    print(BP)
                    Scenario9()
        pygame.display.update()


def Scenario7():
    """ after clicking A1 """

    while True:
        screen.fill((0, 0, 0))
        b12 = button(screen, (460, 700), " CLICK TO CONTINUE ")




        color = (25, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Selected Answer = A'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (420, 460))
        color = (255, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'You died.  The assalant in stall 2 killed you on as soon as'}",
            False, color)  # "text", color





        screen.blit(textsurface, (260, 590))
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'you re-entered the bathroom'}",
            False, color)  # "text", color
        screen.blit(textsurface, (350, 630))
        crest = pygame.image.load('Forgot.png')
        screen.blit(crest, (320, 70))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):





                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b12.collidepoint(pygame.mouse.get_pos()):
                    Question4(HP, BP)

        pygame.display.update()
    pygame.quit()


def Scenario8():
    """ after clicking B """

    while True:
        screen.fill((0, 0, 0))
        b12 = button(screen, (460, 700), " CLICK TO CONTINUE ")

        color = (25, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Selected Answer = B'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (420, 500))
        color = (255, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Conduct offense.  Your begging did not help'}",
            False, color)  # "text", color
        screen.blit(textsurface, (250, 540))
        crest = pygame.image.load('Begging.png')
        screen.blit(crest, (350, 60))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b12.collidepoint(pygame.mouse.get_pos()):
                    Question4(HP, BP)

        pygame.display.update()
    pygame.quit()

def Scenario9():
    """ after clicking A1 """

    while True:
        screen.fill((0, 0, 0))
        b12 = button(screen, (460, 700), " CLICK TO CONTINUE ")





        color = (25, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Selected Answer = C'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (420, 300))
        color = (255, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'You are awarded the Navy cross'}",
            False, color)  # "text", color
        screen.blit(textsurface, (20, 350))
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'After telling your Batt-O about the intruder he demands you show him'}",
            False, color)  # "text", color
        screen.blit(textsurface, (20, 390))





        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{' Upon re-entering the bathroom you are attacked by two members of '}",
            False, color)  # "text", color
        screen.blit(textsurface, (20, 430))
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Russian special forces.  You take two rounds to the calf and your '}",
            False, color)  # "text", color
        screen.blit(textsurface, (20, 470))
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Battalion officer is shot in the shoulder. The two of you use the'}",
            False, color)  # "text", color
        screen.blit(textsurface, (20, 510))
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{' ruler and pen from the logbook to disarm and detain the assalants'}",
            False, color)  # "text", color
        screen.blit(textsurface, (20, 550))




        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'You are a hero'}",
            False, color)  # "text", color
        screen.blit(textsurface, (280, 590))
        crest = pygame.image.load('Fight.png')
        screen.blit(crest, (350, 30))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b12.collidepoint(pygame.mouse.get_pos()):
                    Question4(HP, BP)

        pygame.display.update()
    pygame.quit()


def Question4(HP, BP):
    """ after clicking A """
    while True:
        screen = pygame.display.set_mode((1200, 800))
        screen.fill((0, 0, 0))
        b13 = button(screen, (40, 270), " A ")
        b14 = button(screen, (40, 320), " B ")
        b15 = button(screen, (40, 370), " C ")
        bQ1 = button(screen, (90, 270), " Tell him that you're the reincarnation of John Paul Jones and walk away  ")
        bQ1a = button(screen, (90, 320), "Run Away!")
        bQ3 = button(screen, (90, 370), " Appologize, plea incompotence  ")
        crest = pygame.image.load('Caught.png')
        screen.blit(crest, (320, 430))



        color = (255, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Captain Foreman catches you walking down Stribling in Blue and Golds.'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (50, 100))
        color = (255, 215, 0)




        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Before 1800 Chooose your response'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (280, 140))


        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b13.collidepoint(pygame.mouse.get_pos()):
                    BP.append(90)
                    print(HP)
                    print(BP)
                    Scenario10()
                if b14.collidepoint(pygame.mouse.get_pos()):
                    BP.append(30)
                    print(HP)
                    print(BP)
                    Scenario11()
                elif b15.collidepoint(pygame.mouse.get_pos()):
                    HP.append(80)
                    print(HP)
                    print(BP)
                    Scenario12()
        pygame.display.update()



def Scenario10():
    """ after clicking A1 """

    while True:
        screen.fill((0, 0, 0))
        b16 = button(screen, (460, 700), " CLICK TO CONTINUE ")


        color = (25, 215, 0)


        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Selected Answer = A'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (420, 460))
        color = (255, 215, 0)




        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Captain Foreman is highly superstitious of the supernatural.  '}",
            False, color)  # "text", color
        screen.blit(textsurface, (200, 590))
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(




            f"{'He lets you walk'}",
            False, color)  # "text", color
        screen.blit(textsurface, (390, 630))
        crest = pygame.image.load('Spooky.png')
        screen.blit(crest, (420, 70))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()


            if event.type == pygame.MOUSEBUTTONDOWN:
                if b16.collidepoint(pygame.mouse.get_pos()):
                    Question5(HP, BP)

        pygame.display.update()
    pygame.quit()


def Scenario11():
    """ after clicking B """

    while True:
        screen.fill((0, 0, 0))
        b16 = button(screen, (460, 700), " CLICK TO CONTINUE ")





        color = (25, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Selected Answer = B'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (420, 390))
        color = (255, 215, 0)




        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'The DepDant pulls out a handheld tranqualizer pistol and shoots you '}",
            False, color)  # "text", color
        screen.blit(textsurface, (25, 430))
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'in the back of the neck.  The last thing you remeber is pulling'}",
            False, color)  # "text", color
        screen.blit(textsurface, (25, 470))
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'a dart out of your neck before falling asleep. you wake up in your room'}",
            False, color)  # "text", color
        screen.blit(textsurface, (25, 510))

        textsurface = font.render(
            f"{'to find no more blue and golds in your closet and a note that says'}",
            False, color)  # "text", color
        screen.blit(textsurface, (25, 550))
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Justice always wins - CAPT Foreman'}",
            False, color)  # "text", color
        screen.blit(textsurface, (25, 590))
        crest = pygame.image.load('Law.png')
        screen.blit(crest, (430, 30))



        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b16.collidepoint(pygame.mouse.get_pos()):
                    Question5(HP, BP)

        pygame.display.update()
    pygame.quit()

def Scenario12():
    """ after clicking A1 """

    while True:
        screen.fill((0, 0, 0))
        b16 = button(screen, (460, 700), " CLICK TO CONTINUE ")

        color = (25, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Selected Answer = C'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (420, 400))
        color = (255, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Conduct Offense'}",
            False, color)  # "text", color
        screen.blit(textsurface, (400, 500))
        crest = pygame.image.load('NoOffice.png.')
        screen.blit(crest, (400, 30))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b16.collidepoint(pygame.mouse.get_pos()):
                    Question5(HP, BP)

        pygame.display.update()
    pygame.quit()

def Question5(HP, BP):
    """ after clicking A """
    while True:

        screen = pygame.display.set_mode((1200, 800))
        screen.fill((0, 0, 0))
        b17 = button(screen, (40, 270), " A ")
        b18 = button(screen, (40, 320), " B ")
        b19 = button(screen, (40, 370), " C ")
        bQ1 = button(screen, (90, 270), " Politely decline and grab a Capri sun instead  ")
        bQ1a = button(screen, (90, 320), "You take it and enjoy three more cans of it before the end of the night")
        bQ3 = button(screen, (90, 370), " Ask for a glass of milk instead ")
        crest = pygame.image.load('Rockstar.png')
        screen.blit(crest, (330, 450))



        color = (255, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'While back home during Christmas leave your friend offers  '}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (50, 100))
        color = (255, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'you a drink of rockstar unplugged '}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (50, 140))


        color = (255, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Chooose your response'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (350, 180))



        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b17.collidepoint(pygame.mouse.get_pos()):
                    BP.append(70)
                    print(HP)
                    print(BP)
                    Scenario13()
                if b18.collidepoint(pygame.mouse.get_pos()):
                    BP.append(-200)
                    print(HP)
                    print(BP)
                    Scenario14()
                elif b19.collidepoint(pygame.mouse.get_pos()):
                    HP.append(300)
                    print(HP)
                    print(BP)
                    Scenario15()
        pygame.display.update()

def Scenario13():
    """ after clicking A1 """

    while True:
        screen.fill((0, 0, 0))
        b16 = button(screen, (460, 700), " CLICK TO CONTINUE ")

        color = (25, 215, 0)



        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Selected Answer = A'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (420, 460))
        color = (255, 215, 0)


        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{' You enjoy a delicious capri sun.  '}",
            False, color)  # "text", color
        screen.blit(textsurface, (380, 590))

        crest = pygame.image.load('CapriSun.png')
        screen.blit(crest, (220, 10))


        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b16.collidepoint(pygame.mouse.get_pos()):
                    Question6(HP, BP)

        pygame.display.update()
    pygame.quit()


def Scenario14():
    """ after clicking B """

    while True:
        screen.fill((0, 0, 0))
        b16 = button(screen, (460, 700), " CLICK TO CONTINUE ")

        color = (25, 215, 0)


        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Selected Answer = B'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (420, 430))
        color = (255, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Upon returning to USNA you are subject to a drug test. '}",
            False, color)  # "text", color
        screen.blit(textsurface, (250, 470))


        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Of all the tests you have taken at the academy, this one' }",
            False, color)  # "text", color
        screen.blit(textsurface, (250, 510))
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'is the only test that could actually get you kicked out'}",
            False, color)  # "text", color


        screen.blit(textsurface, (250, 550))
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Kiss your commission goodbye'}",
            False, color)  # "text", color


        screen.blit(textsurface, (250, 590))


        crest = pygame.image.load('Drugs.png')
        screen.blit(crest, (300, 30))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b16.collidepoint(pygame.mouse.get_pos()):
                    Question6(HP, BP)

        pygame.display.update()
    pygame.quit()

def Scenario15():
    """ after clicking A1 """

    while True:
        screen.fill((0, 0, 0))
        b16 = button(screen, (460, 700), " CLICK TO CONTINUE ")

        color = (25, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Selected Answer = C'}",


            False, color)  # "text", antialias, color
        screen.blit(textsurface, (420, 400))
        color = (255, 215, 0)
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'You are a psychopath.'}",
            False, color)  # "text", color
        screen.blit(textsurface, (400, 500))
        crest = pygame.image.load('Milk.png.')
        screen.blit(crest, (450, 90))



        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b16.collidepoint(pygame.mouse.get_pos()):
                    Question6(HP, BP)

        pygame.display.update()
    pygame.quit()

def Question6(HP, BP):
    """ after clicking A """
    while True:

        screen = pygame.display.set_mode((1200, 800))
        screen.fill((0, 0, 0))

        crest = pygame.image.load('crest.png.')
        screen.blit(crest, (400,5))
        color = (255, 215, 0)

        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Thanks for playing! '}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (450, 590))
        color = (255, 215, 0)
        color = (255, 215, 0)

        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{sum(HP)} Helmet Points {sum(BP)} Hero Points",
            False, color)  # "text", antialias, color

        screen.blit(textsurface, (400, 640))
        pygame.display.update()


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
        font = pygame.font.SysFont("Segoe UI", 33)
        textsurface = font.render(
            f"{'Disclaimer: (Helmet) will not be used as a derogatory term in this game'}",
            False, color)  # "text", antialias, color
        screen.blit(textsurface, (110, 735))
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
                    start(HP, BP)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    start(HP, BP)
        pygame.display.update()
    pygame.quit()


menu()