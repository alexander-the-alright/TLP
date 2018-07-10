# -*- coding: utf-8 -*-

#   Author:     Donnie Brasco
#   Date:       Sure

###########################################################

#
#   IMPORTS
#

import os
import codecs

from h import hp

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
    rus = input('What does that translate too?\t\t').lower()

    while(True):
        
        print('\nAre you sure you want to add { %s -> %s }?' % (eng, rus) )
        yn = input('Type "yes" to confirm.\n\n').lower()

        if yn == y:
            if eng[:3] == v:
                pairsV.update({eng : rus})

                with open('data/dataV.txt','a') as addV:
                    addV.write('%s,%s\n' % (eng, rus))
                
            else:
                pairs.update({eng : rus})

                with open('data/data.txt','a') as addN:
                    addN.write('%s,%s\n' % (eng, rus))
                    
            print('\nAdded { %s -> %s }' % (eng, rus) )
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
        pairsV.update({eng : rus})

        with open('data/dataV.txt','a') as addV:
            addV.write('%s,%s\n' % (eng, rus))
                
    else:
        pairs.update({eng : itl})

        with open('data/data.txt','a') as addN:
            addN.write('%s,%s\n' % (eng, rus))

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

r = ''

ext = 'EXIT'
hlp = 'HELP'
edt = 'EDIT'
clr = 'CLEAR'

Brk = 'stop'
Add = 'add'
Edt = 'edit'
Dlt = 'delete'

conj = []
prn = []
prep = []

hlp1 = 'Type any word to find its translation, if it exists.\n'
hlp2 = 'Type "EXIT" to exit, "HELP" for help, or "EDIT" to edit.\n'
hlp2 = 'Type "EXIT" to exit or "EDIT" to edit.\n'
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

with codecs.open('data/data.txt','r','utf-8') as file:
    for line in file:
        spl = line.lower().split(',')
        if spl[0] not in pairs:
            rStr = ''
            for rtal in spl[1:]:
                rStr = rStr + ',' + str(rtal)
            rStr = rStr[1:len(rStr)-1]
            pairs.update({str(spl[0]) : rStr})

#   \   FILE PARSING    1   /


#   /   FILE PARSING    2   \

with codecs.open('data/dataV.txt','r','utf-8') as fileV:
    for line in fileV:
        spl = line.lower().split(',')
        if spl[0] not in pairsV:
            rStr = ''
            for rtal in spl[1:]:
                rStr = rStr + ',' + str(rtal)
            rStr = rStr[1:len(rStr)-1]
            pairsV.update({str(spl[0]) : rStr})

#   \   FILE PARSING    2   /


#   /   LOOKUP  \

while r != ext:

    try:
        r = input(hlpM)
        if r == ext:
            break
        if r == clr:
            cls()
            continue
        if r == hlp:
            #hp.menu()
            print()
            continue
        if r == edt:
            begin()
            continue
        r = r.lower()
        if r == '':
            continue
        if r in pairs:
            print(pairs.get(r),'\n')
        elif r in pairs.values():
            for k in pairs.keys():
                if pairs[k] == r:
                    print(k,'\n')
                    break
        elif r not in pairs:
            print(no)
    except (EOFError,KeyboardInterrupt):
        break

#   \   LOOKUP  /


#exit()

###########################################################
