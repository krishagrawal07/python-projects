import random
import time
snakes = {99:4,70:54,52:40,24:10} #like snake is from 99 to  4 and 70 to 54 , basically it is high to low
ladders = {6:25,11:45,60:84,46:90} #same concept appliedd for ladder,it is low to high

def roll_dice():
        return random.randint(1,6)
def move_player(currpos,roll):
        print("You rolled a",roll,"!")
        time.sleep(1)
        
        currpos+=roll

        if currpos in snakes:
                print("Oh no! it's a snake bite! Go back from",currpos ,"to",snakes[currpos])
                currpos = snakes[currpos]
        elif currpos in ladders:
                print("Yay! climbed  a ladder from",currpos ,"to",ladders[currpos])
                currpos = ladders[currpos]
        else:
                print("Your current position is: ",currpos)
        return currpos

print("Lets start the game ! you have to reach to 100 to win the game")
currpos=0

while currpos<100:
          user_choice=input("\nPress Enter to roll the dice or type q to Quit: ").lower()


          if(user_choice=='q'):
                  print("Game Over! Your final position was: ",currpos)
                  break

          roll = roll_dice()
          currpos = move_player(currpos,roll)

          if (currpos>=100):
                  print("Congrats !You won")



