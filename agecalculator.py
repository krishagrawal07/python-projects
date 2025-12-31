from datetime import datetime

birthdateinput = input("Enter your birthdate in YYYY-MM-DD format: ")
birthdate = datetime.strptime(birthdateinput, "%Y-%m-%d")

  # strptime is used to convert a date string into a datetime object 
currentdate = datetime.now()
age = currentdate.year - birthdate.year

print(f"Your age is {age} years. ")