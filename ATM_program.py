#  Create a ATM program using functions.

def check_balance(balance):
    print("Your current balance is:", balance)
    return balance

def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Amount deposited successfully.")
    print("Updated balance is:", balance)
    return balance

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Please collect your cash.")
        print("Remaining balance is:", balance)
    else:
        print("Insufficient balance")
    return balance

def atm():
    balance = 25000  
    
    while True:
        print("\n----- ATM Menu Options-----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            balance = check_balance(balance)
        elif choice == '2':
            balance = deposit(balance)
        elif choice == '3':
            balance = withdraw(balance)
        elif choice == '4':
            print("Thank you for using ATM")
            break
        else:
            print("Invalid choice. Try again.")

atm()