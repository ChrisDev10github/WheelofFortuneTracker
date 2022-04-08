#Wheel of Fortune
import random

player1amount = 0
player2amount = 0
player3amount = 0

word=[]
wheel = [100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,'Bankrupt','Lose Turn']
display=[]

turnyes=True
countturn=0
game = True
roundnumber=1
personturn=1


def spinwheel():
    value=random(wheel)

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
                if word[i]==vguess:
                    display[i]==vguess                                 #word needs to addressed
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
                if word[i]==vguess:
                    display[i]==vguess                                 #word needs to addressed
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
                if word[i]==vguess:
                    display[i]==vguess                                 #word needs to addressed
                else:
                    turnyes=False
        else:
            print("You cannot buy a vowel and you lose your turn")
            turnyes=False      