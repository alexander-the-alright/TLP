"""
 ===============================================================================
 Auth: Sam Celani
 Prog: tlp.py
 Revn: 12-27-2018 Ver 1.0
 Func: Read in comma-separated data from file(s), load into dictionary(s)
       Parse user data, either [edit] or [lookup]
       [edit]: call h/hp.py, more info there
       [lookup]: use {}.get(), or search {}.values() & return key at that index
       Print associated key and value

 TODO: Add feature to recognize adverbs
       Store specifics of different syntactic structs in parallel lists
       Add more data
       Create a mega-dictionary, list of dicts
 ===============================================================================
 CHANGE LOG
 -------------------------------------------------------------------------------
 ??-??-201?:    init
 ??-??-201?:    made working script
 ??-??-201?:    added data to data file
 12-27-2018:    started updating comments to adhere to new template
                removed global variables used in begin()
                replaced global variables used in body
 12-28-2018:    finished updating comments to adhere to new template
                removed redundant while loop from add()
 
"""

# ==============================================================================
#
#   IMPORTS
#
# ------------------------------------------------------------------------------


import os           # Used for clearing the screen
from h import hp    # Used for help menu


# ==============================================================================
#
#   FUNCTIONS
#
# -----------------------------------------------------------------------------

"""
 ===============================================================================
 Revn: 12-27-2018
 Func: Clears the screen
 Meth: Import os, lambda
 Vars: None
 Retn: None, clears screen

 TODO: make system independent
 ===============================================================================
"""
cls = lambda: os.system('cls')  # Call cls through the system
                                # Needs to be made more robust

"""
 ===============================================================================
 Revn: 12-27-2018
 Func: Verb-specific print function
 Meth: Iteratively print verb form and the translation
 Vars: str string: the English infinitive to be translated
 Retn: None

 TODO: update tabs for robustness
 ===============================================================================
"""
def vPrint(strang):

    global pairsV   # Get list of infinitives and translations
    spl = pairsV.get(strang).split(',')     # Split into array for ease

    # List of forms
    vp = ['Infinitive',
          'I\t/ Io',
          'You\t/ Tu',
          'He/She\t/ Lui/Lei',
          'We\t/ Noi',
          'You(pl)\t/ Voi',
          'They\t/ Loro'
         ]

    print('\n  ENG\t\t  ->\tITAL')
    
    for c in range(len(spl)):           # Iterate over amount of forms
        print(vp[c],end='')             # Print corresponding form
        if c == 3:                      # Position[3] is really long
            print(' ->\t',end='')       # so no tabbing
        else:                           # Otherwise
            print('\t  ->\t',end='')    # Tab it up
        print(spl[c])                   # Print the translation
    print()                             # Newline after
  
"""
 ===============================================================================
 Revn: 12-27-2018
 Func: init the edit menu
 Meth: iteratively get user input
       decide to add, edit, or delete an entry
 Vars: None
 Retn: None

 TODO:
 ===============================================================================
"""
def begin():

    print('What would you like to do?') # Print initial prompt
    string = ''                         # Initialize input variable

    while not string in extL:   # Loop until the input is an exit condition
        # Prompt user for input, force lower case
        string = input('Add, Edit, or Delete?\n\n').lower()
        if string == 'add':         # If user wants to add
            add()                   # call add function
        elif string == 'edit':      # If user wants to edit
            edit()                  # call edit function
        elif string == 'delete':    # If user wants to delete
            delete()                # call delete function
        elif string == 'fadd':      # Experienced user, add without prompts
            fadd()                  # call fast add
        elif string == 'fedit':     # Experienced user, edit without prompts
            fedit()                 # call fast edit
        elif string == 'fdel':      # Experienced user, delete without prompts
            fdelete()               # call fast delete
        elif string in extL:        # Do nothing if it hits the exit condition
            pass                    # This avoids it printing (below) on exit
        else:                       # Or if it's none of those...
            print('That doesn''t match any acceptable answers. Please try again.\n')

"""
 ===============================================================================
 Revn: 12-28-2018
 Func: Add translation pairs, with prompts
 Meth: Take user input twice, ask for confirm
       on confirmation, check if verb or not verb, add to appropriate file
 Vars: None
 Retn: None

 TODO:
 ===============================================================================
"""
def add():

    global pairs    # Get list of normal pairs
    global pairsV   # Get list of verb pairs
    global v        # Get string that denotes a verb

    # Prompt for 'english' half of pair
    eng = input('What word would you like to add?\t').lower()
    # Prompt for other half of pair
    itl = input('What does that translate too?\t\t').lower()

    # Prompt for confirmation
    print('\nAre you sure you want to add { %s -> %s }?' % (eng, itl) )
    yn = input('Type "yes" to confirm.\n\n').lower()    # Take user input

    if yn in ['yes', 'y', 'ye', 'yeet']:    # If confirmed
        if eng[:3] == v:                    # Check if verb
            pairsV.update({eng : itl})      # If True, add to verb dict

            with open('data/dataV.txt','a') as addV:    # Open verb file
                addV.write('%s,%s\n' % (eng, itl))      # Add to it
            
        else:                               # If not a verb
            pairs.update({eng : itl})       # Update regular dictionary

            with open('data/data.txt','a') as addN:     # Open normal file
                addN.write('%s,%s\n' % (eng, itl))      # Add to it
                
        print('\nAdded { %s -> %s }' % (eng, itl) )     # Confirmation
    else:
        print('Add aborted.')                           # No confirm, rip
    print()

"""
 ===============================================================================
 Revn: 12-28-2018
 Func: Add translation pairs, without prompts
 Meth: prompt twice, check if verb, add to appropriate file
 Vars: None
 Retn: None

 TODO:
 ===============================================================================
"""
def fadd():

    global pairs                                    # Get normal pairs
    global pairsV                                   # Get verb pairs

                                                    # No prompting
    eng = input().lower()                           # Get input 1, force lower
    itl = input().lower()                           # Get input 2, force lower

    if eng[:3] == v:                                # Check if verb
        pairsV.update({eng : itl})                  # If True, update verb dict

        with open('data/dataV.txt','a') as addV:    # Open verb file
            addV.write('%s,%s\n' % (eng, itl))      # Write new pair to it
                
    else:                                           # If it's not a verb
        pairs.update({eng : itl})                   # Update normal verb dict

        with open('data/data.txt','a') as addN:     # Open normal file
            addN.write('%s,%s\n' % (eng, itl))      # Write new pair to it

"""
 ===============================================================================
 Revn: 12-28-2018
 Func: Edit an existing pair with prompts
 Meth: Prompt user about pair, find, replace, rewrite file
 Vars: None
 Retn: None

 TODO:
 ===============================================================================
"""
def edit():

    global pairs    # Get normal pairs
    global pairsV   # Get verb pairs
    global v        # Get string that denotes a verb
    global no       # Get string for when a word isn't in any dictionary

    # Prompt user for word to edit
    e = input('What word do you want to edit?\n').lower()

    # Check to see if the entry exists in either dictionary
    if e in pairs or e in pairsV:
        # This could probably be done simpler with an assign or
        if e[:3] == v:              # Check to see if it's a verb
            old = pairsV.get(e)     # If True, store old value from verb dict
        else:                       # If it's not a verb
            old = pairs.get(e)      # Store old value from normal dict
        # Print old pair
        print('{ %s -> %s }\nAre you sure you want to edit this?' % (e, old))
        # Prompt user for confirmation
        yn = input('Type "yes" to confirm.\n\n').lower()
        if yn in ['yes', 'y', 'ye', 'yeet']:    # If confirmation is positive
            # Get new translation from user
            new = input('What word do you want to replace %s with?\n' % old).lower()
            if e in pairs:                  # If it's not a verb
                pairs.update({ e : new })   # Put it in the normal dictionary

                # Open normal file in write mode for desctructive write
                with open('data/data.txt','w') as editN:
                    for tup in pairs:   # Iterate over all pairs
                        # Rewrite all pairs, removing the old pair from the file
                        editN.write('%s,%s\n' % ( tup, pairs.get(tup) ) )
                        
            # Already know it's in one dictionary, so if it's not in normal,
            # it has to be a verb
            else:
                pairsV.update({ e : new })  # Put edited pair in verb dictionary

                # Open verb file in write mode for desctructive write
                with open('data/dataV.txt','w') as editV:
                    for tup in pairsV:  # Iterate over all pairs
                        # Rewrite all pairs, removing the old pair from the file
                        editV.write('%s,%s\n' % ( tup, pairsV.get(tup) ) )
            
        else:                       # User says no
            print('Edit aborted.')  # Abort
    else:           # If the user input isn't in the dictionaries
        print(no)   # Warn and leave, there's nothing to edit

"""
 ===============================================================================
 Revn: 12-28-2018
 Func: Edit an existing pair without prompts
 Meth: Prompt user about pair, find, replace, rewrite file
 Vars: None
 Retn: None

 TODO:
 ===============================================================================
"""
def fedit():

    global pairs                        # Get normal pairs
    global pairsV                       # Get verb pairs
    global v                            # Get string that denotes a verb

    # No prompting, force to lower case
    e = input().lower()                 # Get user input, old word to edit
    new = input().lower()               # Get user input, new translation
    if e in pairs:                      # If the old word is in the normal dict
        pairs.update({ e : new })       # Update that with new translation

        # Open normal file in write mode for desctructive write
        with open('data/data.txt','w') as editN:
            for tup in pairs:           # Iterate over all pairs
                # Rewrite all pairs, removing the old pair from the file
                editN.write('%s,%s\n' % ( tup, pairs.get(tup) ) )
                
    elif e in pairsV:
        pairsV.update({ e : new })

        # Open verb file in write mode for desctructive write
        with open('data/dataV.txt','w') as editV:
            for tup in pairsV:          # Iterate over all pairs
                # Rewrite all pairs, removing the old pair from the file
                editV.write('%s,%s\n' % ( tup, pairsV.get(tup) ) )
    else:                               # If it's not in a dictionary
        pass                            # There's nothing to edit

"""
 ===============================================================================
 Revn: 12-28-2018
 Func: Delete pair with prompts
 Meth: Take input, delete corresponding pair, rewrite entire file
 Vars: None
 Retn: None

 TODO:
 ===============================================================================
"""
def delete():

    # Prompt user input of what pair is to be deleted, force lower case
    d = input('What word needs to be deleted?\n').lower()
    
    if d in pairs:  # If it's in the normal dictionary
        # Prompt user if they want to delete that pair
        yn = input('Are you sure you want to delete { %s -> %s }?\n' % ( d, pairs.get(d)) )
        if yn in ['yes', 'y', 'ye', 'yeet']:    # On positive confirmation
            del pairs[d]                        # Delete that pair

            # Open verb file in write mode for desctructive write
            with open('data/data.txt','w') as delN:
                for tup in pairs:               # Iterate over all pairs
                    # Rewrite all pairs, removing the old pair from the file
                    delN.write('%s,%s\n' % ( tup, pairs.get(tup) ) )
                
    elif d in pairsV:   # If it's in the normal dictionary
        # Prompt user if they want to delete that pair
        yn = input('Are you sure you want to delete { %s -> %s }?\n' % ( d, pairsV.get(d)) )
        if yn in ['yes', 'y', 'ye', 'yeet']:    # On positive confirmation
            del pairsV[d]                       # Delete that pair

            # Open verb file in write mode for desctructive write
            with open('data/dataV.txt','w') as delV:
                for tup in pairsV:              # Iterate over all pairs
                    # Rewrite all pairs, removing the old pair from the file
                    delV.write('%s,%s\n' % ( tup, pairs.get(tup) ) )

    print()

"""
 ===============================================================================
 Revn: 12-27-2018
 Func: Delete pair without prompts
 Meth: Take input, delete corresponding pair, rewrite entire file
 Vars: None
 Retn: None

 TODO:
 ===============================================================================
"""
def fdelete():

    d = input().lower()             # Get user input, no prompts
    
    if d in pairs:                  # Validate user input for normal vocab
        del pairs[d]                # Delete if true

        # Open verb file in write mode for desctructive write
        with open('data/data.txt','w') as delN:
            for tup in pairsV:      # Iterate over all pairs
                # Rewrite entire file, minus deleted pair
                delN.write('%s,%s\n' % ( tup, pairs.get(tup) ) )
                
    elif d in pairsV:               # Validate user input for verbs
        del pairsV[d]               # Delete if true

        # Open verb file in write mode for desctructive write
        with open('data/data.txt','w') as delV:
            for tup in pairsV:      # Iterate over all pairs
                # Rewrite entire file, minus deleted pair
                delV.write('%s,%s\n' % ( tup, pairs.get(tup) ) )

    # No prompt on failure, maybe change this?

    print()

# ==============================================================================
#
#   GLOBAL VARIABLES
#
# ------------------------------------------------------------------------------

# Dictionaries where pairs are stored
# Multiple are used to make lookup/printing easier
pairs = {}      # Maybe I should have a list of these dictionaries
pairsV = {}     # so it's easier to access in these functions

# Unused for now
"""
pairsAv = {}
pairsAdj = {}
pairsC = {}
pairsPrn = {}
pairsPrp = {}
"""

i = ''  # Init input

extU = ['EXIT','E','STOP','QUIT','KILL']    # Exit conditions for main body
extL = ['exit','stop','quit','kill']        # Exit conditions for edit menu

# Not sure what these are, not ready to remove
"""
conj = []
prn = []
prep = []
"""

helpMenu = '''Type any word to find its translation, if it exists.
Type "EXIT" to exit, "HELP" for help, or "EDIT" to edit.
Be sure to use the infinitive form of any verbs, e.g. "eat" -> "to eat".
Do not search verb conjugations, e.g. "eaten" or "ate".

'''

# Replaced with normal multi-line string, not ready to remove
"""
hlp1 = 'Type any word to find its translation, if it exists.\n'
hlp2 = 'Type "EXIT" to exit, "HELP" for help, or "EDIT" to edit.\n'
hlp3 = 'Be sure to use the infinitive form of any verbs, e.g. "eat" -> "to eat".\n'
hlp4 = 'Do not search verb conjugations, e.g. "eaten" or "ate".\n\n'
hlpM = hlp1 + hlp2 + hlp3 + hlp4
"""

# Prompt when pair is not found
no = 'That word does not exist in this look-up table.\n'

v = 'to '   # Marks verb
av = 'ly'   # Marks adverb, not yet used


### ============================================================================
###
### BODY 
###
### ----------------------------------------------------------------------------


## File Parsing 1   ->  Normal words
with open('data/data.txt') as file:             # Open file, read only
    for line in file:                           # Iterate over all lines in file
        spl = line.lower().split(',')           # Split line around the commas
        if spl[0] not in pairs:                 # str[0] is the 'english' word
        # ^^^ This line probably isn't all that necessary, as there shouldn't be
        # ^^^ multiple lines in the data file for the same one word
            iStr = ''                           # Initialize translation string
            for ital in spl[1:]:                # Iterate over all translations
                iStr = iStr + ',' + str(ital)   # Add comma and next word
            iStr = iStr[1:]                     # Remove first char, ','
            pairs.update({str(spl[0]) : iStr})  # Add finished string to dict

## File Parsing 2   ->  Verbs
with open('data/dataV.txt') as fileV:           # Open file, read only
    for line in fileV:                          # Iterate over all lines in file
        spl = line.lower().split(',')           # Split line around the commas
        if spl[0] not in pairsV:                # str[0] is the 'english' word
        # ^^^ This line probably isn't all that necessary, as there shouldn't be
        # ^^^ multiple lines in the data file for the same one word
            iStr = ''                           # Initialize translation string
            for ital in spl[1:]:                # Iterate over all translations
                iStr = iStr + ',' + str(ital)   # Add comma and next word
            iStr = iStr[1:]                     # Remove first char, ','
            pairsV.update({str(spl[0]) : iStr}) # Add finished string to dict

## Actual loop, this is where the program spends the most time
while not i in extU:                                # Loop until user inputs
                                                    # a stop command

    try:                                    # Try to handle ^C, EOF
        i = input(helpMenu)                 # Prompt and get input
        if i in extU:                       # Immediately check for exit sequence
            continue
        if i in ['CLEAR','cls','CLS']:
            cls()                           # Check input for clear screen keys
            continue
        if i == 'HELP':
            hp.menu()                       # Check input for help menu keyword
            print()
            continue
        if i == 'EDIT':
            begin()                         # Check input for edit menu keyword
            continue
        i = i.lower()                       # Otherwise, force lower case
        if i == '':                         # This is probably dead code
            continue
        if i in pairs or i in pairsV:       # Check if input exists in any dict
        # vvv This segment could probably be rewritten a little nicer
            if i in pairsV:                 # If it's in the verbs dictionary
                # This line also seems unneccesary
                # WTF was I on when I wrote this?
                if i[:3] == v:
                    vPrint(i)               # Call special verb print function
            else:                           # If it's not a verb, it's normal
                print(i,'->',pairs.get(i),'\n')     # Print as is
        elif i in pairs.values():           # Search translations for user input
                                            # Don't even bother checking verbs
                                            # That's way too complicated
            for k in pairs.keys():
                if pairs[k] == i:           # Find corresponding word
                    print(k,'->',pairs.get(k),'\n') # Print as is
                    break
        # ^^^ This segment could probably be rewritten a little nicer
        elif i not in pairs:                # If it's not in anything else
            print(no)                       # Say so
    except (EOFError,KeyboardInterrupt):    # Try to handle ^C, EOF
        break

exit()                                      # EXEUNT


### ============================================================================
