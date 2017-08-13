import time

def start():
    print("\nWelcome to a mostly pointless yet still amazingly impressive game!")
    playerReady = raw_input("\nAre you ready to begin? (y/n) ").lower()
    readyYet(playerReady)

def readyYet(playerReady):
    print("playerReady equal to: \n")
    print(playerReady)
    if playerReady != "y" and playerReady != "n":
        print("\nWait, you do know which are the 'y' and 'n' keys, right? \nMaybe you're not ready for this game just yet.")
        playerReady = raw_input("\nMaybe try again. Are you ready? (y/n) ").lower()
        readyYet(playerReady)
    elif playerReady == "n":
        while playerReady == "n":
            print("\nTake your time, buddy. I can wait all day.")
            time.sleep(2)
            playerReady = raw_input("\nHow about now? Ready to start? (y/n) ").lower()
            readyYet(playerReady)
    else:
        print("\nNice job. You found the 'y' key. That's really fabulous.")
        time.sleep(2)
        print("\nOk, you're ready for this?")
        time.sleep(1)
        print("\nFine, here goes:\n")
        for x in range(0,3):
            time.sleep(1)
            print(3-x)
        time.sleep(1)
        print("\nLET'S DO THIS.")
        time.sleep(1)
        playGame()  

def playGame():
    word = raw_input("\nOk, enter your favorite word and I will do a bunch of contrived maths with it: \n")
    time.sleep(2)
    print("\n'{}' is a pretty great word, I concur.").format(word)
    time.sleep(1)
    print("\nLet's explore the nature of {} to see what it's like. ").format(word)
    length = len(word)
    isOdd = bool(length % 2)
    time.sleep(2)
    print("\nMy favorite thing about {} is that it's {} letters long! \nThat's totally a number!").format(word,length)
    if isOdd == True:
        print("\nTo be more precise: An odd number, wouldn't you know!")
    else:
        print("\nSpecifically, an even number, my favorite kind!")
    time.sleep(1)
    if length < 10:
        countUp(length)
    elif length > 10:
        countDown(length)
    else:
        wowTen()
    print("")


def countUp(length):
    print("\nLet's count up to ten from there, ok?!?!")
    for x in range (length, 10):
        x += 1
        print x
        time.sleep(1)
    steps = 10 - length
    countFinish(steps)

def countDown(length):
    print("\nLet's count down to ten from there, ok?!?!")
    for x in range (length, 10, -1):
        x -= 1
        print x
        time.sleep(1)
    steps = length - 10
    countFinish(steps)

def countFinish(steps):
    print("Wow, it sure took " + str(steps) + " steps to get to ten!")

def wowTen():
    print("Wow, ten!")


    
start()
