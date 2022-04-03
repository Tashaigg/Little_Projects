import os, random
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s -  %(levelname)s -  %(message)s"
)


os.chdir(Path.home())
try:
    os.makedirs('MadLips')
except:
    print('Welcome back\n')
os.chdir(f'{Path.home()}/MadLips')

ps1 = open('Story1.txt','w')
ps1.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')
ps1.close()
ps2 = open('Story2.txt','w')
ps2.write("NOUN declared that it's ilegal to VERB, NOUN did it anyway because they were ADJECTIVE.")
ps2.close()

while True:
    p = open('Your Tales.txt','a')
    p.close()
    tales = Path('Your Tales.txt').read_text()
    #achar index tale
    index = str(0)
    single = ''
    for i in tales:
        if i != '/':
            single = single+i
        else:
            n=1
            ultindex = ''
            while single[n] != '-':
                ultindex = ultindex+single[n]
                n += 1
            try:
                index < ultindex
            except:
                single = ''
            else:
                if int(index) < int(ultindex):
                    index = ultindex
                    single = ''
    inp = input('\nType:\nP to play\nR to register a new Story\nV to view your past Tales\nQ to quit:\n')
    if inp in ('p', 'P', 'play', 'Play', 'PLAY'):
        p = Path(Path.cwd())
        list_mad = os.listdir(p)
        random.shuffle(list_mad)
        while list_mad[0] == 'Your Tales.txt':
            random.shuffle(list_mad)
        mad = Path(f'{list_mad[0]}')
        texto = mad.read_text()

        for i in range(texto.count('NOUN')):
            no = (input('Type a Noun:\n'))
            texto = texto.replace('NOUN', no, 1)
        for i in range(texto.count('VERB')):
            ve = (input('Type an Verb:\n'))
            texto = texto.replace('VERB', ve, 1)
        for i in range(texto.count('ADJECTIVE')):
            ad = (input('Type an Adjective:\n'))
            texto = texto.replace('ADJECTIVE', ad, 1)

        print(texto)
        p = open('Your Tales.txt','a')
        p.write(f'\n{int(index)+1}- {texto}\n/')
        p.close()
    elif inp in ('r', 'R', 'register', 'REGISTER', 'Register'):
        newmad = input('Type the title of your story:\n')
        newmad = Path(f'{newmad}.txt')
        story = input('Using NOUN, VERB and ADJECTIVE (all uppercase) for the words that will be added later\nType your Story:\n')
        newmad.write_text(story)
        print('Your Story was successfully registered')
    elif inp in ('v', 'V', 'view', 'VIEW', 'View'):
        view = str(input('Type the number of your Tale or type ALL to see all past Tales.\n'))
        single = ''
        if view in ('a', 'A', 'all', 'ALL', 'All') or view == '':
            print(tales)
        elif view.isdigit():
            if int(view) in range(1,int(index)+1):
                for i in tales:
                    if i != '/':
                        single = single+i
                    else:
                        if single[1:(len(view))+1] == str(view):
                            print(single)
                            single = ''
                        else:
                            single = ''
            else:
                print('There is no Tale with this number')
                continue
        else:
            continue


    elif inp in ('q', 'Q', 'quit', 'QUIT', 'Quit'):
        break
    else:
        continue
























#
