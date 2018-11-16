"""
 ===============================================================================
 Auth: Sam Celani
 Prog: tlp.py
 Revn: 11-16-2018 Ver 1.X
 Func: Read in comma-separated data from file(s), load into dictionary(s)
       Parse user data, either [edit] or [lookup]
       [edit]: call h/hp.py, more info there
       [lookup]: use {}.get(), or search {}.values() & return key at that index
       Print associated key and value
 ===============================================================================
 CHANGE LOG
 -------------------------------------------------------------------------------
 ??-??-20??:  
 
"""
###########################################################

#
#   IMPORTS
#

import os           # Used for clearing the screen

from h import hp    # Used for help menu

###########################################################

#
#   FUNCTION DEFINITION 1
#       Special print function for verbs
#

def vPrint(strang):

#   /   VARIABLES   \
    
    global pairsV   # Get list of infinitives and translations
    spl = pairsV.get(strang).split(',')
    
    vp = ['Infinitive',
          'I\t/ Io',
          'You\t/ Tu',
          'He/She\t/ Lui/Lei',
          'We\t/ Noi',
          'You(pl)\t/ Voi',
          'They\t/ Loro'
         ]
    
#   \   VARIABLES   /


#   /   BODY    \

    print('\n  ENG\t\t  ->\tITAL')
    
    for c in range(len(spl)):
        print(vp[c],end='')
        if c == 3:
            print(' ->\t',end='')
        else:
            print('\t  ->\t',end='')
        print(spl[c])
    print()
    
#   \   BODY    /
    
###########################################################

#
#   FUNCTION DEFINITION 2
#       Main branch of Edit Hierarchy

def begin():

#   /   VARIABLES   \

    global Add
    global Brk
    global Dlt
    global Edt

#   \   VARIABLES   /


#   /   BODY   \

    print('What would you like to do?')
    string = ''

    while string != Brk:
        string = input('Add, Edit, or Delete?\n\n').lower()
        if string == Add:
            add()
        elif string == Edt:
            edit()
        elif string == Dlt:
            delete()
        elif string == 'fadd':
            fadd()
        elif string == 'fedit':
            fedit()
        elif string == 'fdel':
            fdelete()
        elif string == Brk:
            cls()
            continue
        else:
            print('That doesn''t match any acceptable answers. Please try again.\n')

#   \   BODY   /

###########################################################

#
#   FUNCTION DEFINITION 3
#       Add entry function

def add():

#   /   VARIABLES   \

    global pairs
    global pairsV
    global v

    y = 'yes'
    n = 'no'

#   \   VARIABLES   /


#   /   BODY   \ 

    eng = input('What word would you like to add?\t').lower()
    itl = input('What does that translate too?\t\t').lower()

    while(True):
        
        print('\nAre you sure you want to add { %s -> %s }?' % (eng, itl) )
        yn = input('Type "yes" to confirm.\n\n').lower()

        if yn == y:
            if eng[:3] == v:
                pairsV.update({eng : itl})

                with open('data/dataV.txt','a') as addV:
                    addV.write('%s,%s\n' % (eng, itl))
                
            else:
                pairs.update({eng : itl})

                with open('data/data.txt','a') as addN:
                    addN.write('%s,%s\n' % (eng, itl))
                    
            print('\nAdded { %s -> %s }' % (eng, itl) )
            break
        else:
            print('Add aborted.')
            break
    print()

#   \   BODY   /    

###########################################################

#
#   FUNCTION DEFINITION 4
#       Fast-Add entry function

def fadd():

#   /   VARIABLES   \ 

    global pairs
    global pairsV

#   \   VARIABLES   /


#   /   BODY   \

    eng = input().lower()
    itl = input().lower()

    if eng[:3] == v:
        pairsV.update({eng : itl})

        with open('data/dataV.txt','a') as addV:
            addV.write('%s,%s\n' % (eng, itl))
                
    else:
        pairs.update({eng : itl})

        with open('data/data.txt','a') as addN:
            addN.write('%s,%s\n' % (eng, itl))

#   \   BODY   / 

###########################################################

#
#   FUNCTION DEFINITION 5
#       Edit entry function

def edit():

#   /   VARIABLES   \

    global pairs
    global pairsV
    global v
    global no

    y = 'yes'
    
#   \   VARIABLES   /


#   /   BODY   \

    e = input('What word do you want to edit?\n').lower()

    if e in pairs or e in pairsV:
        if e[:3] == v:
            old = pairsV.get(e)
        else:
            old = pairs.get(e)
        print('{ %s -> %s }\nAre you sure you want to edit this?' % (e, old))
        yn = input('Type "yes" to confirm.\n\n').lower()
        if yn == y:
            new = input('What word do you want to replace %s with?\n' % old).lower()
            if e in pairs:
                pairs.update({ e : new })

                with open('data/data.txt','w') as editN:
                    for tup in pairs:
                        editN.write('%s,%s\n' % ( tup, pairs.get(tup) ) )
                    
            else:
                pairsV.update({ e : new })

                with open('data/dataV.txt','w') as editN:
                    for tup in pairsV:
                        editN.write('%s,%s\n' % ( tup, pairsV.get(tup) ) )
            
        else:
            print('Edit aborted.')
    else:
        print(no)

#   \   BODY   /

###########################################################

#
#   FUNCTION DEFINITION 6
#       Fast-Edit entry function

def fedit():

#   /   VARIABLES   \

    global pairs
    global pairsV
    global v
    global no
    
#   \   VARIABLES   /


#   /   BODY   \

    e = input().lower()

    if e in pairs or e in pairsV:
        if e[:3] == v:
            old = pairsV.get(e)
        else:
            old = pairs.get(e)
        new = input().lower()
        if e in pairs:
            pairs.update({ e : new })

            with open('data/data.txt','w') as editN:
                for tup in pairs:
                    editN.write('%s,%s\n' % ( tup, pairs.get(tup) ) )
                    
        else:
            pairsV.update({ e : new })

            with open('data/dataV.txt','w') as editN:
                for tup in pairsV:
                    editN.write('%s,%s\n' % ( tup, pairsV.get(tup) ) )


#   \   BODY   /

###########################################################

#
#   FUNCTION DEFINITION 7
#       Delete entry function

def delete():

#   /   VARIABLES   \

    y = 'yes'

#   \   VARIABLES   /


#   /   BODY   \

    d = input('What word needs to be deleted?\n').lower()
    
    if d in pairs:
        yn = input('Are you sure you want to delete { %s -> %s }?\n' % ( d, pairs.get(d)) )
        if yn == y:
            del pairs[d]

            with open('data/data.txt','w') as delN:
                for tup in pairs:
                    delN.write('%s,%s\n' % ( tup, pairs.get(tup) ) )
                
    elif d in pairsV:
        yn = input('Are you sure you want to delete { %s -> %s }?\n' % ( d, pairsV.get(d)) )
        if yn == y:
            del pairsV[d]

            with open('data/data.txt','w') as delV:
                for tup in pairsV:
                    delV.write('%s,%s\n' % ( tup, pairs.get(tup) ) )

    print()
    
#   \   BODY   /

###########################################################

#
#   FUNCTION DEFINITION 8
#       Fast-Delete entry function

def fdelete():

#   /   BODY   \

    d = input().lower()
    
    if d in pairs:
        del pairs[d]

        with open('data/data.txt','w') as delV:
            for tup in pairsV:
                delV.write('%s,%s\n' % ( tup, pairs.get(tup) ) )
                
    elif d in pairsV:
        del pairsV[d]

        with open('data/data.txt','w') as delV:
            for tup in pairsV:
                delV.write('%s,%s\n' % ( tup, pairs.get(tup) ) )

    print()
    
#   \   BODY   /


###########################################################

#
#   BODY
#


#   /   GLOBAL VARIABLES    \

pairs = {}      # Maybe I should have an array of these dictionaries
pairsV = {}     # so it's easier to access in these functions
pairsAv = {}
pairsAdj = {}
pairsC = {}
pairsPrn = {}
pairsPrp = {}

i = ''

ext = ['EXIT','E']
hlp = 'HELP'
edt = 'EDIT'
clr = ['CLEAR','cls']

Brk = 'stop'
Add = 'add'
Edt = 'edit'
Dlt = 'delete'

conj = []
prn = []
prep = []

hlp1 = 'Type any word to find its translation, if it exists.\n'
hlp2 = 'Type "EXIT" to exit, "HELP" for help, or "EDIT" to edit.\n'
hlp3 = 'Be sure to use the infinitive form of any verbs, e.g. "eat" -> "to eat".\n'
hlp4 = 'Do not search verb conjugations, e.g. "eaten" or "ate".\n\n'
hlpM = hlp1 + hlp2 + hlp3 + hlp4

no = 'That word does not exist in this look-up table.\n'

v = 'to '
av = 'ly'

#   \   GLOBAL VARIABLES    /


#   /   LAMBDA   \

cls = lambda: os.system('cls')

#   \   LAMBDA    /


#   /   FILE PARSING    1   \

with open('data/data.txt') as file:
    for line in file:
        spl = line.lower().split(',')
        if spl[0] not in pairs:
            iStr = ''
            for ital in spl[1:]:
                iStr = iStr + ',' + str(ital)
            iStr = iStr[1:len(iStr)-1]
            pairs.update({str(spl[0]) : iStr})

#   \   FILE PARSING    1   /


#   /   FILE PARSING    2   \

with open('data/dataV.txt') as fileV:
    for line in fileV:
        spl = line.lower().split(',')
        if spl[0] not in pairsV:
            iStr = ''
            for ital in spl[1:]:
                iStr = iStr + ',' + str(ital)
            iStr = iStr[1:len(iStr)-1]
            pairsV.update({str(spl[0]) : iStr})

#   \   FILE PARSING    2   /


#   /   LOOKUP  \

while not i in ext:

    try:
        i = input(hlpM)
        if i in ext:
            continue
        if i in clr:
            cls()
            continue
        if i == hlp:
            hp.menu()
            print()
            continue
        if i == edt:
            begin()
            continue
        i = i.lower()
        if i == '':
            continue
        if i in pairs or i in pairsV:
            if i in pairsV:
                if i[:3] == v:
                    vPrint(i)
            else:
                #print('\n  ENG\t->   ITAL')
                print(i,'->',pairs.get(i),'\n')
        elif i in pairs.values():
            for k in pairs.keys():
                if pairs[k] == i:
                    #print('\n  ENG\t->   ITAL')
                    print(k,'->',pairs.get(k),'\n')
                    break
        elif i not in pairs:
            print(no)
    except (EOFError,KeyboardInterrupt):
        break

#   \   LOOKUP  /


exit()

###########################################################
