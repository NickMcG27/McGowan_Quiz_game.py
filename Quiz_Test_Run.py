print('Welcome to (HOW TO MID.)  The only game that tells you how much of helmet you are')
answer = input('Ready to play ? (not really / no / definitely not) :')
Helmet_score = 0
Lucky_score = 0
Steel_Nerves_score = 0
total_questions = 10
if answer.lower() == 'no' or 'yes':
    #Kyle helped me figure out how to use the or Statement to force the player to start the game
        answer = input('Too bad! Sinario 1: \n\n '
                   'Your CO asks you to meet them in their office.  \n '
                   'During the meeting he mentions that he suspects you \n'
                   'are fratting with a firstie in-company (you are.).\n'
                   '  Do you \n'
                   'A.  Confirm his suspicions and ask for 2 weeks to get a love chit finalized\n'
                   'B.  Tell him that he must be thinking of someone else and ask why he is having\n'
                   ' so much trouble with names and faces in the company\n'
                   'C.  Point at the window and scream pterodactyl and run out of his \n'
                   'officer while he is distracted\n'
                   'Selected Answer =')
        if answer.lower() == 'a':

            Lucky_score +=0
            Steel_Nerves_score += 0
            print('Yeah. Sure you would')
        if answer.lower() == 'b':
            Helmet_score += 0

            Steel_Nerves_score += 30
            print('You played on his ego.  He apologizes for the mixup and assures you he will put the rumors to rest')
        if answer.lower() == 'c':
            print('Admitted to Insane Asylum.  \n'
              'After running away your company officer hired a private investigator to watch you and your suspected lover.\n  '
              'There was AMPLE evidence.  After recieivng an honor and conduct offense you earned yourself an impressive amount of restriction.  \n '
              'While on tours one night your mind could no longer bear the manotony, you mentally snapped \n '
              'and attacked the gunnery sergeant calling the candence (he kicked your ass) \n '
              'and now you are in a hospital for the mentally unsafe \n\n')
            Helmet_score += 0
            Lucky_score +=100
            Steel_Nerves_score += 70
        else:
            print("Next Sinario\n\n")

        answer = input('Sinario 2: You arrive on deck three minutes past TAPS,\n your CDO is very upset.  Chooose your response\n'
                   ' A. Gas light the CDO into believing that there is an extra hour tonight because of daylight savings time\n'
                   ' B. Try to bribe him with half a bag of sour skittles you have left in your pocket\n'
                   ' C. Apologize and accept whatever unfortold immense consequences will beseach you \n'
                   'Selected Answer = ')
        if answer.lower() == 'a':
            Helmet_score += 0
            Lucky_score += 20
            Steel_Nerves_score += 70
            print('That should not have worked.  Congradulations')
        if answer.lower() == 'b':
            Helmet_score += 0
            Lucky_score += 50
            Steel_Nerves_score += 30
            print('He loves sour skittles.  No UA this time')
        if answer.lower() == 'c':
            Helmet_score += 30
            Lucky_score += 20
            Steel_Nerves_score += 0
            print('Your CDO takes pitty on you.  No UA this time')
        else:
            print('Next Sinario\n\n')

        answer = input('Sinario 3: You come out of the bathroom to find your battalion officer waiting at the mates desk\n'
                   ' looking over the log book and the watchbelt that you left on the desk while you took a bathroom break. \n'
                   ' What do you do?\n'
                   ' A. Turn around and hide in the bathroom until he leaves\n'
                   ' B. Own up to it and BEG for your life\n'
                   ' C. Tell your Batt-O that you only went into the bathroom because you had\n'
                   ' to stop and armed assalant who was posted up in stall 2 \n'
                   'Selected Answer =')
        if answer.lower() == 'a':
            Helmet_score += 0
            Lucky_score += 20
            Steel_Nerves_score += 0
            print('You died.  The assalant in stall 2 killed you on as soon as you re-entered the bathroom')
        if answer.lower() == 'b':
            Helmet_score += 100
            Lucky_score += 0
            Steel_Nerves_score += 0
            print('He did not appreciate your begging.  Conduct offense')
        if answer.lower() == 'c':
            Helmet_score += 0
            Lucky_score += 20
            Steel_Nerves_score += 100
            print('You are awarded the Navy cross.  After telling your Batt-O about the intruder he demands you show him.\n'
              '  Upon re-entering the bathroom you are attacked by two members of Russian special forces.  \n '
              'You take two rounds to the calf and your Battalion officer is shot in the shoulder.  The two of you use the\n'
              ' ruler and pen from the logbook to disarm and detain the assalants.  You are a hero\n\n')
        else:
            print('Next Sinario\n\n')

        answer = input(
            'Sinario 4: There is only one Krave cereal left in King Hall, you spot it from a couple tables away and make a B-line for such a rare treat.\n '
            'As you reach into the cereal bin opening at the bottom, someone else comes and grabs the Krave from the top.\n'
            ' A. Throat punch the cereal thief and run off with your well deserved meal\n'
            ' B. take some frosted flakes instead\n'
            ' C. Tell him that all the Krave cereal in King Hall was recalled and supposed to be thrown out because \n'
            'they are carrying a dangerous pathogen that the Academy has classified as a biological weapon. \n'
            ' Take it as soon as he puts it back\n'
            'Selected Answer =')
        if answer.lower() == 'a':
            Helmet_score += 0
            Lucky_score += 0
            Steel_Nerves_score += 60
            print('That did not work. He had strong throat. He lifts you by your collar and throws you into the cereal \n'
                  'bin while king hall watches and laughs')
        if answer.lower() == 'b':
            Helmet_score += 100
            Lucky_score += 0
            Steel_Nerves_score += 0
            print('Enjoy your frosted flakes! they taste better with chocolate milk.\n')
        if answer.lower() == 'c':
            Helmet_score += 0
            Lucky_score += 20
            Steel_Nerves_score += 100
            print('Someone overhears your bio-hazard threat and the rumor spreads like wildfire.  \n'
                  'Two days later you are put in ROM and being questioned for information regarding \n'
                  'the imaginary disease.  All over some cereal. \n\n')
        else:
            print('Next Sinario\n\n')


Helmet_mark = (Helmet_score / total_questions) * 10
Lucky_mark = (Lucky_score / total_questions) * 10
Steel_Nerves_mark = (Steel_Nerves_score / total_questions) * 10

print('Thanks for Playing. Your scored a total of', Lucky_mark + Steel_Nerves_mark - Helmet_mark, "points!")
print('Points obtained:', Helmet_mark, 'Helmet points' , Lucky_mark , 'Luck points' ,Steel_Nerves_mark , "Steel Nerves points\n\n")

if int(Helmet_mark) > 100:
    print ("Whoa budy, your helmet has been on too tight for too long")

if int(Lucky_mark) > 100:
    print("You lucky SOB")

if int(Steel_Nerves_mark) > 100:
    print("You have no stimulus to fear")