account={351269:{"name":"mangesh","password": "1234", "balance": 1000}, 123456:{"name":"sachin","password": "abcd", "balance": 2000}, 789012:{"name":"priya","password": "xyz", "balance": 3000}, 456789:{"name":"rahul","password": "pass", "balance": 4000}}
print("Welcome to the Banking System")
print("Please login to continue")
userid = int(input("Enter userid: "))
password = input("Enter password: ")

if userid in account and account[userid]["password"] == password:
        print("Login successful!")
        print(f"Welcome {account[userid]["name"]}! Your balance is {account[userid]['balance']}.")
        # return True
        debit_or_credit = input("Do you want to debit : 0 or credit : 1 or transfer : 2? : ")
        if debit_or_credit == "0":
              amount= float(input("Enter amount to debit: "))
              if amount <= account[userid]["balance"]:
                  account[userid]["balance"] -= amount
                  print(f"Debited {amount}. current balance is {account[userid]['balance']}.")
        elif debit_or_credit == "1":
              amount = float(input("Enter amount to credit: "))
              account[userid]["balance"] += amount
              print(f"Credited {amount}. current balance is {account[userid]['balance']}.")
        elif debit_or_credit == "2":    
              transfrer_userid = int(input("Enter userid to transfer: "))
              if transfrer_userid in account:
                transfer_amount=float(input("Enter amount to transfer: "))
                if transfer_amount <= account[userid]["balance"]:
                    account[userid]["balance"] -= transfer_amount
                    account[transfrer_userid]["balance"] += transfer_amount
                    print(f"Transferred {transfer_amount} to {account[transfrer_userid]['name']}. Current balance is {account[userid]['balance']}.")
                else:
                    print("Insufficient balance for transfer.")
        else:
              print("Invalid option selected.")
              # return False
else:
    print("Invalid username or password.")
    # return False