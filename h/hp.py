#   Author:     Donnie Brasco
#   Date:       Sure

###########################################################

#
#   FUNCTION DEFINITION 1
#       Prints the help menu for the help menu

def helpM():
    print('In this help menu, you can find out about the following subjects:\n')

    for num in nums:
        print(num,'\t|\t',subj[nums.index(num)])

###########################################################

#
#   FUNCTION DEFINITION 2
#       Looks up user input and prints the associated
#       help file

def menu():

#   /   GLOBAL VARIABLES    \

    global stop
    global file
    global hlp
    global helpText

#   \   GLOBAL VARIABLES    /


    inp = ''


##  //      INPUT SEARCHING    \\
    while inp != stop:
        inp = input(inputText)
        
#   /   STOP CONDITION  \

        if inp == stop:
            continue
        
#   \   STOP CONDITION  /

#   /   MATCH FILE TO INPUT     \
        inp = inp.lower()

        if inp == condition[0]:
            file = chap[0]
        elif inp == condition[1]:
            file = chap[1]
        elif inp == condition[2]:
            file = chap[2]
        elif inp == condition[3]:
            file = chap[3]
        elif inp == condition[4]:
            file = chap[4]
        elif inp == condition[5] or inp == condition[6]:
            file = chap[5]
        elif inp == condition[7] or inp == condition[8]:
            file = chap[6]
        elif inp == condition[9]:
            file = chap[7]
        elif inp == condition[10] or inp == condition[11]:
            file = chap[8]
        elif inp == condition[12]:
            file = chap[9]
        elif inp == stop:
            break
        elif inp == hlp:
            helpM()
        else:
            print(helpText,end='')

#   \   MATCH FILE TO INPUT     /

#   /   LOOKUP  \

        if file in chap:
            file = direc + file
            with open(file) as f:
                print()
                for line in f:
                    print(line,end='')
        file = ''
        
        print('\n')

#   \   LOOKUP  /
##  \\      INPUT SEARCHING    //

###########################################################

#
#   GLOBAL VARIABLES
#

direc = 'h/'

chap = ['pv1.txt',
        'prep.txt',
        'pro.txt',
        'conj.txt',
        'poss.txt',
        'det.txt',
        'plr.txt',
        'adj.txt',
        'comm.txt',
        'abt.txt'
       ]

subj = ['About',
        'Useful Commands',
        'Present-Tense Verbs',
        'Prepositions',
        'Pronouns',
        'Conjunctions',
        'Possessives',
        'Determiners / Articles',
        'Plurality',
        'Adjectives'
       ]

nums = ['I',
        'II',
        'III',
        'IV',
        'V',
        'VI',
        'VII',
        'IIX',
        'X',
        'XI'
       ]

condition = ['verbs',
             'prepositions',
             'pronouns',
             'conjunctions',
             'possessives',
             'determiners', 'articles',
             'plurals', 'plurality',
             'adjectives',
             'commands', 'useful commands',
             'about'
            ]

hlp = 'help'
stop = 'stop'
inputText = 'What do you need help with?\n\n'
helpText = 'That does not exist in the help dialogue. Please try again, or type "STOP" to stop.'

file = ''
    
###########################################################
