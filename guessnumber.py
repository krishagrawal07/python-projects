import random
target = random.ranint(1,100)

while True:
          choice = int(input("Enter your CHOICE or QUIT(q): "))
          if(choice=="q"):
                  break
          elif(choice==target):
                  print("Hurray you guess right")
                  break
          elif(choice<target):
                    print("Your number is small")
          else:
                  print("Your number is big")
print("Game over")