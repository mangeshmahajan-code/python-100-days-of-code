import random
print("press :\n1 for password generator\n2 for pin generator")
choice = input("Enter your choice: ")
if choice==1:
 print ("password generator")
 input= input("Enter the length of the password: ")
 length = int(input)
 characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&"
 password = "".join(random.choice(characters) for i in range(length))
 print("Generated password:", password)
 print("Thank you for using the password generator!")
else:
 print ("pin generator")
 input= input("Enter the length of the pin: ")
 length = int(input)

 characters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

 pin = "".join(random.choice(characters) for i in range(length))
 print("Generated pin:", pin)
 print("Thank you for using the pin generator!")
 