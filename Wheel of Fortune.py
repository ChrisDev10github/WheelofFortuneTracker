#Wheel of Fortune
import random

player1amount = 0
player2amount = 0
player3amount = 0

#word=''
wheel = [100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,-1,0]      #-1 is for bankrupt and 0 is for lose turn
#output=[]
#goal=list(word)

turnyes=True
countturn=0
game = True
roundnumber=1
personturn=1
wheelvalue=1
vguess=''
cguess=''
wguess=''



def spinwheel():
    wheelvalue=random(wheel)

def getword():
    f = open(r'C:\Users\Chris\Documents\PythonCode\words.txt')
    dictionary = f.read().split('\n')
    f.close()
    return random.choice(dictionary)

def vowel():
    if personturn==3:                         #Player3
        if player3amount >=250:                                 #checks if P3 have 250
            player3amount = player3amount - 250                 #subtracts $250
            vguess = str(input('Enter a vowel in lowercase form: '))
            for i in range(0,len(word)):
                if goal[i]==vguess:
                    output[i]==vguess                                 #word needs to addressed
                else:
                    turnyes=False
        else:
            print("You cannot buy a vowel and you lose your turn")
            turnyes=False

    if personturn==2:           #Player2
        if player2amount >=250:                                 #checks if P3 have 250
            player2amount = player2amount - 250                 #subtracts $250
            vguess = str(input('Enter a vowel in lowercase form: '))
            for i in range(0,len(word)):
                if goal[i]==vguess:
                    output[i]==vguess                                 #word needs to addressed
                else:
                    turnyes=False
        else:
            print("You cannot buy a vowel and you lose your turn")
            turnyes=False      

    if personturn==1:           #Player 1
        if player1amount >=250:                                 #checks if P3 have 250
            player1amount = player1amount - 250                 #subtracts $250
            vguess = str(input('Enter a vowel in lowercase form: '))
            for i in range(0,len(word)):
                if goal[i]==vguess:
                    output[i]==vguess                                 #word needs to addressed
                else:
                    turnyes=False
        else:
            print("You cannot buy a vowel and you lose your turn")
            turnyes=False      


def constinent():

    if personturn==3:       #player 3
        spinwheel()
        if wheelvalue >0:
           cguess = str(input('Enter a constient in lowercase form: ')) 
           for i in range(0,len(goal)):                                                      #goal not assigned which is the list of word
                if goal[i] ==cguess:
                   output[i]==cguess
                   player3amount += wheelvalue
                   print(output)
                else:
                    turnyes=False
        if wheelvalue == -1:
            player3amount =0
            turnyes=False
        else:                               #lose turn
            turnyes=False             


    if personturn==2:       #player 2
        spinwheel()
        if wheelvalue >0:
           cguess = str(input('Enter a constient in lowercase form: ')) 
           for i in range(0,len(goal)):                                                      #goal not assigned which is the list of word
                if goal[i] ==cguess:
                   output[i]==cguess
                   player2amount += wheelvalue
                   print(output)
                else:
                    turnyes=False
        if wheelvalue == -1:
            player2amount =0
            turnyes=False
        else:                               #lose turn
            turnyes=False    


    if personturn==1:       #player 1
        spinwheel()
        if wheelvalue >0:
           cguess = str(input('Enter a constient in lowercase form: ')) 
           for i in range(0,len(goal)):                                                      #goal not assigned which is the list of word
                if goal[i] ==cguess:
                   output[i]==cguess
                   player1amount += wheelvalue
                   print(output)
                else:
                    turnyes=False
        if wheelvalue == -1:
            player1amount =0
            turnyes=False
        else:                               #lose turn
            turnyes=False    



def wordguess():
    wguess =str(input('Enter Word all lowercase: '))
    if wguess ==word:
        print(goal)
        print("You guessed the word correctly!")
        roundnumber += 1
    else:
        turnyes=False



#Round1
word=getword()
word=word.lower()
goal=list(word)
output=[]
for i in range(0,len(goal),1):
    output.append('_ ')

while roundnumber == 1:
    turnyes=True
    
    #individual turn
    while turnyes == True:
        if countturn%3==0:
            personturn=3
        elif countturn%2==0:
            personturn=2
        else: 
            personturn=1

        choice =int(input('''
                            What do you want to do (1-3):
                                1. Buy vowel
                                2. Guess Constinent
                                3. Guess Word''')) 
        if choice == 1:
            vowel()
        if choice == 2:
            constinent()
        else:
            wordguess()
    countturn+=1

#Main game redefine word=getword(), output[], and make goal.list(word)