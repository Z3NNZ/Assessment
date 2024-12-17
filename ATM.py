#ATM
(username: password, balance)

users = {
   "user 1": {"password": "1234", "balance": 100},
   "user 2": {"password": "2003", "balance": 200},
}

def main_menu(): 
    print ("Welcome to the ATM")
    print ("1. Balance")
    print ("Deposit")
    print ("Withdraw")
    print ("Exit")

def authenticate_user():
    username = input("Enter your username: ")
    if username in users:
        password = input("Enter your password: ")
        if password == users[username]["password"]:
            print(f"Login successful! Welcome, {username}.")
            return username
        else:
            print("Incorrect password. Try again.")
    else:
        print("Username not found.")
    return None

def check_balance(user):
    print(f"\nYour current balance is: ${users[user]['balance']}")

def deposit_money(user):
    try:
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            users[user]["balance"] += amount
            print(f"${amount} deposited successfully. New balance: ${users[user]['balance']}")
        else:
            print("Please enter a valid amount.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def withdraw_money(user):
    try:
        amount = float(input("Enter the amount to withdraw: "))
        if amount > 0 and amount <= users[user]["balance"]:
            users[user]["balance"] -= amount
            print(f"${amount} withdrawn successfully. Remaining balance: ${users[user]['balance']}")
        elif amount > users[user]["balance"]:
            print("Insufficient funds.")
        else:
            print("Please enter a valid amount.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def atm_simulation():
    while True:
        user = authenticate_user()
        if user:
            while True:
                main_menu()
                try:
                    choice = int(input("Select an option: "))
                    if choice == 1:
                        check_balance(user)
                    elif choice == 2:
                        deposit_money(user)
                    elif choice == 3:
                        withdraw_money(user)
                    elif choice == 4:
                        print("Thank you for using the ATM. Goodbye!")
                        return
                    else:
                        print("Invalid option. Please try again.")
                except ValueError:
                    print("Invalid input. Please select a number between 1 and 4.")
        else:
            retry = input("Do you want to try logging in again? (yes/no): ").lower()
            if retry != "yes":
                print("Exiting ATM. Goodbye!")
                break
