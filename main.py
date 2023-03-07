print("Daily Mantra")

name = input("Name: ")
if name == "Yuchuan" or name == "yuchuan":
    print("Hi", name)
    faveWord = input("What's your favourite word? ")
    if faveWord == "i don't know.":
        print("please think one.")
    else:
        print("awesome!")
    currentMood = input("What's your mood now from 1 to 10?")
    if currentMood == "10" or currentMood == "9" or currentMood == "8":
        print("You are rocking today!")
    else:
        print("Oh no...")
        currentChallenge = input("which area of your life you have challenge?")
        if currentChallenge == "work" or currentChallenge == "family" or currentChallenge == "everything":
            print("i know how you feel.")
            print("And let me share with you a few words.")
            print("you are a strong person", name, "You like to feel", faveWord, ".", "But sometimes you are not feeling great. That is normal.", "The challenge you are facing at", currentChallenge, "suck,", "but i am sure you will find a way!" )
        else:
            print("let me note it down.")
            print("And let me share with you a few words.")
            print("you are a strong person", name, "You like to feel", faveWord, ".", "But sometimes you are not feeling great. That is normal.", "The challenge you are facing maybe daunting, but i am sure you will find a way!", name)
    

