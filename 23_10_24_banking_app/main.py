from functions import *
accounts = load_accounts()  # Load accounts from file at the start
while True:
    print("\n=== Welcome to the Bank ===")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Check Balance")
    print("6. Exit")
    
    choice = input("Select an option: ")
    
    if choice == '1':
        create_account(accounts)
    elif choice == '2':
        deposit(accounts)
    elif choice == '3':
        withdraw(accounts)
    elif choice == '4':
        transfer(accounts)
    elif choice == '5':
        check_balance(accounts)
    elif choice == '6':
        print("Thank you for using our banking services!")
        break
    else:
        print("Invalid option. Please try again.")

