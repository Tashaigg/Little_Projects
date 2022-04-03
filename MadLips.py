#MadLips.py
#Game MadLips created by Natasha Tiburcio
#This game let the player choose nouns, verbs and adjectives on pre recorded sentences, creating a (hopefully) fun new sentence.
#all files will be saved somewhere like C:\Users\YOURNAME\MadLips


import os, random
from pathlib import Path
import logging, string

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s -  %(levelname)s -  %(message)s"

)
logging.disable(logging.CRITICAL)# logging deactive

logging.debug('Start of program')
os.chdir(Path.home())
try:
    os.makedirs('MadLips')# trying to create a folder on home, if it already exist, print welcome
except:
    print('\nWelcome back\n')
os.chdir(f'{Path.home()}/MadLips')# changing dir to home/MadLips where everthing will be stored
logging.debug('Folder ok')

ps1 = open('Story1.txt','w')# opening, saving and closing the 2 default models
ps1.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')
ps1.close()
ps2 = open('Story2.txt','w')
ps2.write("NOUN declared that it's ilegal to VERB, NOUN did it anyway because they were ADJECTIVE.")
ps2.close()
logging.debug('Inicial models ok')

while True:
    p = open('Your Tales.txt','a')# creating 'Your Tales.txt' if isn't there already
    p.close()
    tales = Path('Your Tales.txt').read_text()# getting the index of the last Tale
    index = str(0)
    single = ''
    for i in tales:# if there is no talesaved, skip this altogether
        if i != '/':# the character '/' is used to separate the tales
            single = single+i
        else:# when the whole tale is on 'single'
            n=1
            atualindex = ''
            while single[n] != '-':# the '-' comes right after the number (ex: \n3241- Taletext...)
                atualindex = atualindex+single[n]
                n += 1
            try:
                index < atualindex
            except:
                single = ''
            else:
                if int(index) < int(atualindex):
                    index = atualindex
                    single = ''
    logging.debug('Index sentences found.')
    
    inp = input('\nType:\nP to play\nR to register a new Story\nV to view your past Tales\nQ to quit:\n')#inicial input
    if inp in ('p', 'P', 'play', 'Play', 'PLAY'):#Playing
        logging.debug('starting play')
        p = Path(Path.cwd())
        list_mad = os.listdir(p)#get a list of all filenames
        random.shuffle(list_mad)#shuffle that list
        while list_mad[0] == 'Your Tales.txt':#we use the first file, so if it is the tales, shuffle again
            random.shuffle(list_mad)
        mad = Path(f'{list_mad[0]}')
        texto = mad.read_text()#save the story in texto

        for i in range(texto.count('NOUN')):#for each NOUN in texto ask input and replace it in texto
            no = (input('Type a Noun:\n'))
            texto = texto.replace('NOUN', no, 1)
        for i in range(texto.count('VERB')):# Same for VERB
            ve = (input('Type an Verb:\n'))
            texto = texto.replace('VERB', ve, 1)
        for i in range(texto.count('ADJECTIVE')):# Same for Adjective
            ad = (input('Type an Adjective:\n'))
            texto = texto.replace('ADJECTIVE', ad, 1)

        print(texto)#Show the final texto on screen
        p = open('Your Tales.txt','a')
        p.write(f'\n{int(index)+1}- {texto}\n/')#save on 'Your Tales.txt'
        p.close()
    elif inp in ('r', 'R', 'register', 'REGISTER', 'Register'):#Registering new tales model
        logging.debug('starting reg')
        # Create a random 20char long name to be used on the new file name. This is simplier for the player for only the tale is needed, only one input
        random20 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
        newmad = Path(f'model {random20}.txt')#saving the tales model in a new file
        story = input('Using NOUN, VERB and ADJECTIVE (all uppercase) for the words that will be added later\nType your Story:\n')
        newmad.write_text(story)
        print('Your Story was successfully registered')
    elif inp in ('v', 'V', 'view', 'VIEW', 'View'):#to view the already told tales
        logging.debug('starting view')
        view = str(input('Type the number of your Tale or type ALL to see all past Tales.\n'))
        single = ''
        if view in ('a', 'A', 'all', 'ALL', 'All') or view == '':
            print(tales)#show all tales
        elif view.isdigit():
            if int(view) in range(1,int(index)+1):
                for i in tales:#separate every tale
                    if i != '/':
                        single = single+i
                    else:
                        if single[1:(len(view))+1] == str(view):#check the index
                            print(single)#print selected tale
                            single = ''
                        else:
                            single = ''
            else:#if input not in index range
                print('There is no Tale with this number')
                continue#go to main menu
        else:#if input is not number
            continue#go to main menu


    elif inp in ('q', 'Q', 'quit', 'QUIT', 'Quit'):
        logging.debug('quiting')
        break#quit the loop closing the game
    else:#if input on main menu is not expected
        continue#go to main menu again






#
