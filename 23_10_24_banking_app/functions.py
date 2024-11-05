ACCOUNTS_FILE = "accounts.txt"

# Function to validate account number
def is_valid_account_number(account_number):
    return len(str(account_number)) == 10 and str(account_number).isdigit()

# Function to load all accounts from file into a dictionary
def load_accounts():
    accounts = {}
    try:
        with open(ACCOUNTS_FILE, 'r') as file:
            for line in file:
                account_number, balance = line.strip().split(',')
                accounts[account_number] = float(balance)
    except FileNotFoundError:
        # If file doesn't exist,return an empty dictionary
        pass
    return accounts

# Function to save all accounts to file
def save_accounts(accounts):
    with open(ACCOUNTS_FILE, 'w') as file:
        for account_number, balance in accounts.items():
            file.write(f"{account_number},{balance}\n")

# Function to create an account
def create_account(accounts):
    account_number = input("Enter a 10-digit account number: ")
    
    if is_valid_account_number(account_number):
        if account_number in accounts:
            print("Account already exists.")
        else:
            try:
                initial_balance = float(input("Enter initial deposit amount: "))
                accounts[account_number] = initial_balance
                save_accounts(accounts)
                print(f"Account created successfully! Balance: {initial_balance}")
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
    else:
        print("Invalid account number format. Try again.")

# Function to deposit money
def deposit(accounts):
    account_number = input("Enter your account number: ")
    
    if account_number in accounts:
        try:
            amount = float(input("Enter amount to deposit: "))
            accounts[account_number] += amount
            save_accounts(accounts)
            print(f"Deposited {amount}. New balance: {accounts[account_number]}")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
    else:
        print("Account not found. Please create an account first.")

# Function to withdraw money
def withdraw(accounts):
    account_number = input("Enter your account number: ")
    
    if account_number in accounts:
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= accounts[account_number]:
                accounts[account_number] -= amount
                save_accounts(accounts)
                print(f"Withdrew {amount}. Remaining balance: {accounts[account_number]}")
            else:
                print("Insufficient funds for the withdrawal.")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
    else:
        print("Account not found. Please create an account first.")

# Function to check balance
def check_balance(accounts):
    account_number = input("Enter your account number: ")
    
    if account_number in accounts:
        print(f"Your current balance is: {accounts[account_number]}")
    else:
        print("Account not found. Please create an account first.")

# Function to transfer money between accounts
def transfer(accounts):
    sender = input("Enter your account number: ")
    recipient = input("Enter recipient's account number: ")
    
    if sender in accounts and recipient in accounts:
        try:
            amount = float(input("Enter amount to transfer: "))
            if amount <= accounts[sender]:
                accounts[sender] -= amount
                accounts[recipient] += amount
                save_accounts(accounts)
                print(f"Transfer successful! New balance: {accounts[sender]}")
            else:
                print("Insufficient funds for the transfer.")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
    else:
        if sender not in accounts:
            print("Sender account not found. Please create an account first.")
        if recipient not in accounts:
            print("Recipient account not found. Please check the account number.")