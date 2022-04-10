#Wheel of Fortune
import random

player1amount = 0
player2amount = 0
player3amount = 0

wheel = [100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,'Bankrupt','Lose Turn']      #-1 is for bankrupt and 0 is for lose turn

turnyes=True
countturn=1                         #look at val later
game = True
roundnumber=1
personturn=1
wheelvalue=1
vguess=''
cguess=''
wguess=''
finalplayer=0


def spinwheel():
    return random.choice(wheel) 


def getword():
    f = open(r'C:\Users\Chris\Documents\PythonCode\words.txt')
    dictionary = f.read().split('\n')
    f.close()
    return random.choice(dictionary)

def vowel():
    global player1amount
    global player2amount
    global player3amount

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



def consonant():
    global player1amount
    global player2amount
    global player3amount
    global countturn
    global turnyes

    wheelvalue = spinwheel()                    #spin wheel


    if personturn==3:       #player 3                                                           If guess right still goes to next player. If wrong goes to P3 not P2
        if wheelvalue != 'Bankrupt' and wheelvalue != 'Lose Turn':
           cguess = str(input('Enter a constient in lowercase form: ')) 

           if cguess in ['a','e','i','o','u']:
               turnyes=False
               print('You cant guess vowels')

           print(f'Player3 spun a {wheelvalue}')


           if cguess not in goal:
                #print("Does this show")
                turnyes=False
                

           for i in range(0,len(goal)):                                                      #goal not assigned which is the list of word
                if goal[i] ==cguess:
                    output[i]=cguess
                    player3amount += wheelvalue
                    print(f'Player3 has {player3amount}')
                    print(output)   
                    turnyes=True

        if wheelvalue == 'Bankrupt':
            player3amount =0
            turnyes=False
            print('Bankrupt')


        if wheelvalue == 'Lose Turn':                               #lose turn
            turnyes=False   
            print('Lose Turn')

        
        if turnyes ==False:
                countturn+=1             



    if personturn==2:       #player 2                                                           If guess right still goes to next player. If wrong goes to P3 not P2
        if wheelvalue != 'Bankrupt' and wheelvalue != 'Lose Turn':
           cguess = str(input('Enter a constient in lowercase form: ')) 

           if cguess in ['a','e','i','o','u']:
               turnyes=False
               print('You cant guess vowels')

           print(f'Player2 spun a {wheelvalue}')


           if cguess not in goal:
                #print("Does this show")
                turnyes=False
                

           for i in range(0,len(goal)):                                                      #goal not assigned which is the list of word
                if goal[i] ==cguess:
                    output[i]=cguess
                    player2amount += wheelvalue
                    print(f'Player2 has {player2amount}')
                    print(output)   
                    turnyes=True

        if wheelvalue == 'Bankrupt':
            player2amount =0
            turnyes=False
            print('Bankrupt')


        if wheelvalue == 'Lose Turn':                               #lose turn
            turnyes=False   
            print('Lose Turn')

        
        if turnyes ==False:
                countturn+=1



    if personturn==1:       #player 1                                                           If guess right still goes to next player. If wrong goes to P3 not P2
        if wheelvalue != 'Bankrupt' and wheelvalue != 'Lose Turn':
           cguess = str(input('Enter a constient in lowercase form: ')) 

           if cguess in ['a','e','i','o','u']:
               turnyes=False
               print('You cant guess vowels')

           print(f'Player1 spun a {wheelvalue}')


           if cguess not in goal:
                #print("Does this show")
                turnyes=False
                

           for i in range(0,len(goal)):                                                      #goal not assigned which is the list of word
                if goal[i] ==cguess:
                    output[i]=cguess
                    player1amount += wheelvalue
                    print(f'Player1 has {player1amount}')
                    print(output)   
                    turnyes=True

        if wheelvalue == 'Bankrupt':
            player1amount =0
            turnyes=False
            print('Bankrupt')


        if wheelvalue == 'Lose Turn':                               #lose turn
            turnyes=False   
            print('Lose Turn')
        
        if turnyes ==False:
                countturn+=1




def wordguess():
    global roundnumber
    wguess =str(input('Enter Word all lowercase: '))
    if wguess ==word:
        print(goal)
        print("You guessed the word correctly!")
        turnyes=False
        roundnumber += 1                #cant get into next round
    else:
        turnyes=False



#Round1
word=getword()
word=word.lower()
goal=list(word)
output=[]
print(goal)    #testing purpose
for i in range(0,len(goal),1):
    output.append('_ ')

while roundnumber == 1:
    turnyes=True
    
    #individual turn
    while turnyes == True:
        if countturn%3==0:
            personturn=3
        elif countturn%3==2:
            personturn=2
        else: 
            personturn=1
        print(f'Player {personturn} turn')
        choice =int(input('''
                            What do you want to do (1-3):
                                1. Buy vowel
                                2. Spin the Wheel and Guess a consonant
                                3. Guess Word
                                ''')) 
        if choice == 1:
            vowel()
        if choice == 2:
            consonant()
        else:
            wordguess()
    #countturn+=1


#Round 2
print("Round 2")
word=getword()
word=word.lower()
goal=list(word)
output=[]
for i in range(0,len(goal),1):
    output.append('_ ')

while roundnumber == 2:
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
                                2. Guess consonant
                                3. Guess Word
                                ''')) 
        if choice == 1:
            vowel()
        if choice == 2:
            consonant()
        else:
            wordguess()
    countturn+=1
    

#Knowing Final Player
if player3amount > player1amount and player3amount > player2amount:
    finalplayer = 3
if player2amount > player1amount and player2amount > player3amount:
    finalplayer = 2
if player1amount > player2amount and player1amount > player3amount:
    finalplayer = 1


#Final Round

#while roundnumber ==3:



