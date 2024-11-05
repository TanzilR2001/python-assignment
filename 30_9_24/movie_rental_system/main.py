import catalog_manage,rental_manage,earning

while True:
    print("\n--- Movie Rental System ---")
    print("1. Add New Movie to Catalog")
    print("2. Display Available Movies")
    print("3. Rent a Movie")
    print("4. Return a Movie")
    print("5. Display Rented Movies")
    print("6. Calculate Rental Earnings")
    print("7. Exit")

    choice = input("Select an option: ")

    if choice == '1':
        title = input("Enter movie title: ")
        genre = input("Enter genre: ")
        price = float(input("Enter rental price: "))
        quantity=int(input("Enter the quantity: "))
        catalog_manage.add_movie(title.upper(), genre, price,quantity)

    elif choice == '2':
        catalog_manage.display_available_movies()

    elif choice == '3':
        customer = input("Enter customer name: ")
        title = input("Enter movie title: ")
        rental_manage.rent_movie(customer, title.upper())

    elif choice == '4':
        customer = input("Enter customer name: ")
        title = input("Enter movie title: ")
        rental_manage.return_movie(customer, title.upper())

    elif choice == '5':
        rental_manage.display_rented_movies()

    elif choice == '6':
        earning.calculate_earnings()

    elif choice == '7':
        print("Exiting the system.")
        break

    else:
        print("Invalid choice. Please try again.")