import random
#Inputting the user's name
print('Hello! Welcome to Miracle\'s information gathering bot')

userName=input(str('What is your name?:'))
#Asking user for age
userAge=input(str('Do you know your exact age?'))
def guessAgefunc():
    #Age guessing funtion
    print('Let me try to guess')
    print('Give me a range')
    #Minimum age value
    firstRange=input('What is the first range value?:')
    #Maximum age value
    secondRange=input('What is the second range value?:')
    #Getting random age using range
    global trialGuess,userAgeGuess
    userAgeGuess=random.randrange(int(firstRange),int(secondRange))
    #Asking if the guess is correct
    ansGuess='Do you think you are {} years old?:'
    trialGuess=input((ansGuess.format(userAgeGuess)))
    
def realagefunc():
        #inputing real age function
        realage=input('How old are you?:')
        def infofunc():
            print('Here is the information gathered.')
            global information
            #printing information received
            information=('Your name is {} and you are {} years old')
            print(information.format(userName,realage))
        infofunc()
if 'y' in userAge.lower():
    realagefunc()

elif 'n' in userAge.lower():
    guessAgefunc()
    while trialGuess.lower()!='yes':
        print('No worries! Let\'s go over it again')
        guessAgefunc()
        if 'y' in trialGuess.lower():
            break
    rightGuess='You are {} years old!'
    print(rightGuess.format(userAgeGuess))
    print('Here is the information gathered.')
            #global information
            #printing information received
    information=('Your name is {} and you are {} years old')
    print(information.format(userName,userAgeGuess))
#print(rands)


