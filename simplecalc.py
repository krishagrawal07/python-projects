
def add(x,y):
       return x+y
def sub(x,y):
       return x-y
def mul(x,y):
       return x*y
def divide(x,y):
       if y==0:
              return "Error!"
       return x/y



while True:
          print("Select your choice of operators")
          print("\n1. Add")
          print("\n2. Subtract")
          print("\n3. MUltiply")
          print("\n4. Divide")
          print("\n5. Quit")

          choice = input("enter your choice 1/2/3/4/5/")
          
          if choice == '5':
                  print("Exiting calculator")
                  break
          if choice in (1,2,3,4):
             try:
                   n1 = float(input("Enter your first number: "))
                   n2 = float(input("Enter your second number: "))

             except ValueError:
                    print("Invalid input! Enter the number")
                    continue
          elif choice == '1':
                 print("Result: ",add(n1,n2))

          elif choice == '2':
                 print("Result: ",sub(n1,n2))         
          elif choice == '3':
                 print("Result: ",sub(n1,n2))         
          elif choice == '4':
                 print("Result: ",sub(n1,n2))
          else:
                 print("Invalid number")      