# Our epic programmer dict from before
epic_programmer_dict = {'tim berners-lee' : ['tbl@gmail.com', 111],
                        'guido van rossum' : ['gvr@gmail.com', 222],
                        'linus torvalds' : ['lt@gmail.com', 333],
                        'larry page' : ['lp@gmail.com', 444],
                        'sergey brin' : ['sb@gmail.com', 555]
    }

def searchPeople(personsName):
    # Looks up the name in the epic ditionary
    try:
        # Tries the following lines of texts and if there are no errors then it runs
        personsInfo = epic_programmer_dict[personsName]
        print 'Name: ' + personsName.title()
        print 'Email: ' + personsInfo[0]
        print 'Number: ' + str(personsInfo[1])
    except:
        # If there are errors, then this code gets run.
        print 'No information found for that name'

userWantsMore = True
while userWantsMore == True:

    # Asks user to input persons name
    personsName = raw_input('Please enter a name: ').lower()
    # Run our new function searchPeople with what was typed in
    searchPeople(personsName)
    # See if user wants to search again
    searchAgain = raw_input('Search again? (y,n) ').lower()
    # Look at what they replay and act accordingly
    if searchAgain == 'y':
        # userWantsMore stays as true so loop repeats
        userWantsMore = True
    elif searchAgain == 'n':
        # userWantsMore turns to False to stop loop
        userWantsMore = False
    else:
        # user inputs an invalid response, so we quit anyway
        print 'I dont understand your human ways; quitting'
        userWantsMore = False


