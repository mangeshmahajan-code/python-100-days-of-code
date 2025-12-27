import random

print("Press:")
print("1 for password generator")
print("2 for pin generator")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Password Generator")
    length = int(input("Enter the length of the password: "))

    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&"
    password = "".join(random.choice(characters) for _ in range(length))

    print("Generated password:", password)
    print("Thank you for using the password generator!")

elif choice == 2:
    print("PIN Generator")
    length = int(input("Enter the length of the pin: "))

    characters = "0123456789"
    pin = "".join(random.choice(characters) for _ in range(length))

    print("Generated pin:", pin)
    print("Thank you for using the pin generator!")

else:
    print("Invalid choice!")
