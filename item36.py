# -*- coding: cp1252 -*-
import time

def printStuff(intVar,strVar,floatVar):

    #4. Use the print function and .format() notation to print out the variable you assigned
    print("\nHi there, I've got some lovely variables here. Let's take a look:")
    time.sleep(2)
    print("\nFirst off, there's {}, which is quite a lovely integer, I feel.").format(intVar)
    time.sleep(2)
    print("\nSecondly, there's {}, which is a marvelous little string.").format(strVar)
    time.sleep(2)
    print("\nFinally, there's {}, which, frankly, I have to tell you, is the best float ever.").format(floatVar)
    time.sleep(2)
    print("\nJust really fantastic.")
    time.sleep(2)


#12. Define a function that returns a string variable
def returnString():
    thanks = "\nWell, thanks for playing!"
    return thanks

def integerFun(intVar):
    print("\nCool, let's investigate {} and see what it's all about").format(intVar)

    #5. Use each of these operators +, - , * , / , +=, ­= , %
    add1 = intVar + 1
    sub1 = intVar - 1
    mult2 = intVar * 2
    div2 = intVar / 2
    mod3 = intVar % 3
    
    time.sleep(1)
    print("\nYou can add 1 to {} and get {}").format(intVar,add1)
    time.sleep(1)
    print("\nYou can subtract 1 from {} and get {}").format(intVar,sub1)
    time.sleep(1)
    print("\nYou can multiply {} by 2 and get {}").format(intVar,mult2)
    time.sleep(1)
    print("\nYou can divide {} by 2 and get {}").format(intVar,div2)
    time.sleep(1)
    print("\nYou can divide {} by 3 and get a remainder of {}. But I bet you knew that!").format(intVar,mod3)
    time.sleep(2)    
    print("\nThat's all I know about {}.").format(intVar)

    #13. Call the function you defined above and print the result to the shell
    print returnString()

def stringFun(strVar):
    print("\n" + strVar + " is a string containing " + str(len(strVar)) + " letters.")
    time.sleep(.5)
    print("\nCool!")
    time.sleep(1)

    #10. Create a list and iterate through that list using a for loop to print each item out on a new line
    threeList = (strVar[0], strVar[1], strVar[2], strVar[3], strVar[4])
    for x in range(0,5):
        print("Letter no. " + str(x + 1) + " is: " + str(threeList[x]))
        time.sleep(1)
    #13. Call the function you defined above and print the result to the shell
    print returnString()

def floatFun(intVar,strVar,floatVar):
    time.sleep(1)
    print("\nFloats are boring; let's make a tuple instead!")
    myTuple = (intVar, strVar, floatVar,[intVar,strVar,floatVar])
    time.sleep(1)
    print("\nOk, here's my tuple:")
    for x in range(0,4):
        print("\nTuple element #" + str(x + 1) + ": " + str(myTuple[x]))
        time.sleep(1)
    print("\nWell, there you have it.")
    time.sleep(1)

    #13. Call the function you defined above and print the result to the shell
    print returnString()    

def playAgain():
    repeat = raw_input("\nWould you like to play again? (y/n) ")

    #6. Use of logical operators: and, or, not
    if (not(repeat == "y" or repeat == "Y") and not(repeat == "n" or repeat == "N")):
        print("\nYour human ways confound me.")
        playAgain()
    elif (repeat == "y" or repeat =="Y"):
        startProgram()
    else:
        print("\nFine, let's not.")

def startProgram():

    #1. Assign an integer to a variable
    intVar = 3

    #2. Assign a string to a variable
    strVar = "three"

    #3. Assign a float to a variable
    floatVar = 3.14

    printStuff(intVar,strVar,floatVar)
    print("\nWhich variable would you like to know more about?")
    choice = raw_input("\nInteger(i), String(s), Float(f)? ")

    #7. Use of conditional statements: if, elif, else
    if choice == "i":
        integerFun(intVar)
        playAgain()
    elif choice == "s":
        stringFun(strVar)
        playAgain()
    elif choice == "f":
        floatFun(intVar,strVar,floatVar)
        playAgain()
    else:
        print("\nINVALID INPUT; SELF-DESTRUCTING IN TEN SECONDS")
        time.sleep(2)
        x = 10

        #8. Use of a while loop
        while x > 5:
            print x
            x -= 1
            time.sleep(.75)
        while x > 1:
            print x

            #5. Use each of these operators +, - , * , / , +=, ­= , %
            x -= 1
            time.sleep(.4)        

        #9. Use of a for loop
        for y in range(1,5):
            print x
            time.sleep(1)

            #5. Use each of these operators +, - , * , / , +=, ­= , %
            y += 1

        time.sleep(2)
        print("\nTIMER MALFUNCTION; MELTDOWN AVERTED.")
        time.sleep(2)
        print("\nGuess we'll start over now...")
        time.sleep(2)
        startProgram()
        
startProgram()
