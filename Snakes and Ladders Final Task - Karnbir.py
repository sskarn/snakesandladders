'''
Karnbir Saini
ICS2O0-B
Dec 06, 2017 (Made in 2-3 Hours in 1 Day)
Python 2.7 Final Task (Snakes and Ladders)
Description: This is a 2 player game of Snakes and Ladders which includes:
* The ability to input player names
* 3 Ladders & 3 Snakes
* Rolling 2 dice to move forward
* The ability to display square number and dice results
* A forfeit and continue option
* & The ability to return to the previous square if the piece goes over the square 100
The game ends once 1 of the players lands on 100. 
'''

from random import choice #Allows the ability for the dice to randomize
p1piece = 1 #Starting Square #
p2piece = 1 #Starting Square #
die1array = [1,2,3,4,5,6] #Dice 1 List to randomize and choose from
die2array = [1,2,3,4,5,6] #Dice 2 List to randomize and choose from
print "Welcome to Snakes & Ladders!"
p1name = raw_input ("Enter Name of Player 1: ") #Stores Player 1's name to display in the square number and dice results
p2name = raw_input ("Enter Name of Player 2: ") #Stores Player 2's name to display in the square number and dice results
player = 1 #Starts game with player 1

while (player == 1): #While loop for Player 1
        dicerollp1 = raw_input ("Player 1: type 'R' to roll dice: ") #Asks Player 1 to roll dice
        dicerollp1 = dicerollp1.lower() #converts uppercase to lowercase
        
        if dicerollp1 == 'r': #if statement to check for roll confirmation
                die1 = choice(die1array) #Rolls Die 1
                die2 = choice(die2array) #Rolls Die 2
                p1piece = p1piece + die1 + die2 #Adds result of Die 1 and Die 2
                print "Dice 1 rolled {} & Dice 2 rolled {}".format(die1, die2) #Displays Dice roll
                if p1piece <= 100: #Displays Square #
                        print "{}'s piece is on Square #{}".format(p1name, p1piece)
                if p1piece == 9: #9 to 34 ladder
                        print p1name,"climbs up a ladder! You went from 9 to 34!"
                        p1piece = p1piece + 25
                        print "{}'s piece is on Square #{}".format(p1name, p1piece)
                if p1piece == 40: #40 to 64 ladder
                        print p1name,"climbs up a ladder! You went from 40 to 64!"
                        p1piece = p1piece + 24
                        print "{}'s piece is on Square #{}".format(p1name, p1piece)
                if p1piece == 54: #54 to 19 snake
                        print p1name,"slides down a snake. You went from 54 to 19."
                        p1piece = p1piece - 35
                        print "{}'s piece is on Square #{}".format(p1name, p1piece)
                if p1piece == 67: #67 to 86 ladder
                        print p1name,"climbs up a ladder! You went from 67 to 86!"
                        p1piece = p1piece + 19
                        print "{}'s piece is on Square #{}".format(p1name, p1piece)
                if p1piece == 90: #90 to 48 snake
                        print p1name,"slides down a snake. You went from 90 to 48."
                        p1piece = p1piece - 42
                        print "{}'s piece is on Square #{}".format(p1name, p1piece)
                if p1piece == 99: #99 to 77 snake
                        print p1name,"slides down a snake. You went from 99 to 77."
                        p1piece = p1piece - 22
                        print "{}'s piece is on Square #{}".format(p1name, p1piece)
                if p1piece == 100: #Win Check
                        print p1name,"wins by getting to 100!"
                        break#Ends game
                if p1piece > 100: #Checks for piece exceeding 100 and sends piece back to previous square
                        p1piece = p1piece - die1 - die2
                        print "{}'s piece goes higher than 100 so {} stays on Square #{}".format(p1name, p1name, p1piece)
                die1 = 0 #Resets Die 1
                die2 = 0 #Resets Die 2
                continuep1 = raw_input ("type 'C' to continue or 'F' to forfeit: ") #Continue or Forfeit
                continuep1 = continuep1.lower()#converts uppercase to lowercase
                if continuep1 == 'c':#if c, then continues
                        player = 2
                elif continuep1 ==  'f':#if f, then forfeits
                        print p1name,"has forfeited. Therefore",p2name,"has won by Forfeit."
                        break#Ends game
                else:#if wrong character typed, continues game
                        player = 2
                
        while (player == 2): #While loop for Player 2 (Same as above but for player 2)
                dicerollp2 = raw_input ("Player 2: type 'R' to roll dice: ")
                dicerollp2 = dicerollp2.lower()

                if dicerollp2 == 'r':
                        die1 = choice(die1array)
                        die2 = choice(die2array)
                        p2piece = p2piece + die1 + die2
                        print "Die 1 rolled {} & Die 2 rolled {}".format(die1, die2)
                        if p2piece <= 100:
                                print "{}'s piece is on Square #{}".format(p2name, p2piece)
                        if p2piece == 9:
                                print "You climb up a ladder! You went from 9 to 34!"
                                p2piece = p2piece + 25
                                print "{}'s piece is on Square #{}".format(p2name, p2piece)
                        if p2piece == 40:
                                print "You climb up a ladder! You went from 40 to 64!"
                                p2piece = p2piece + 24
                                print "{}'s piece is on Square #{}".format(p2name, p2piece)
                        if p2piece == 54:
                                print "You slide down a snake. You went from 54 to 19."
                                p2piece = p2piece - 35
                                print "{}'s piece is on Square #{}".format(p2name, p2piece)
                        if p2piece == 67:
                                print "You climb up a ladder! You went from 67 to 86!"
                                p2piece = p2piece + 19
                                print "{}'s piece is on Square #{}".format(p2name, p2piece)
                        if p2piece == 90:
                                print "You slide down a snake. You went from 90 to 48."
                                p2piece = p2piece - 42
                                print "{}'s piece is on Square #{}".format(p2name, p2piece)
                        if p2piece == 99:
                                print "You slide down a snake. You went from 99 to 77."
                                p2piece = p2piece - 22
                                print "{}'s piece is on Square #{}".format(p2name, p2piece)
                        if p2piece == 100:
                                print p2name,"wins by getting to 100!"
                                break
                        if p2piece > 100:
                                p2piece = p2piece - die1 - die2
                                print "{}'s piece goes higher than 100 so {} stays on Square #{}".format(p2name, p2name, p2piece)
                        die1 = 0
                        die2 = 0
                        continuep2 = raw_input ("type 'C' to continue or 'F' to forfeit: ")
                        continuep2 = continuep1.lower()
                        if continuep2 == 'c':
                                player = 1
                        elif continuep2 ==  'f':
                                print p2name,"has forfeited. Therefore",p1name,"has won by Forfeit."
                                break
                        else:
                                player = 1
                

                
                
                

                

        
                
                
        



