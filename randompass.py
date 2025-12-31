import random
import string
charval = string.ascii_letters + string.digits + string.punctuation
passslen = 8
password = ""
for i in range(passslen):
         password += random.choice(charval)
print(password)