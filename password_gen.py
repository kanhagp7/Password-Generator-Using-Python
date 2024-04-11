import random
import string

pwd_len = int(input("Enter Desired Password Lenght: "))

print("""Choose the type of character you want in your password: 
          1. Letters
          2. Digits
          3. Special Characters
          4. Exit """)

allchar = ""

while True:
    choice = int(input("pick a number"))

    if(choice == 1):
        allchar += string.ascii_letters
    
    elif(choice== 2):
        allchar += string.digits

    elif(choice==3):
        allchar += string.punctuation
    
    elif(choice == 4):
        break
    else:
        print("Please pick a valid option")

password = []

for i in range(pwd_len):

    randomchar = random.choice(allchar)
    password.append(randomchar)

print("The random password is: ", "".join(password) )



