# Initializing the dictionary with some values
country_capitals = {
    "India": "New Delhi",
    "United States": "Washington D.C.",
    "Russia": "Moscow",
    "England": "London"
}

# def display_menu():
#     print("\nMenu:")
#     print("1. Add a new element to the dictionary")
#     print("2. Update an element in the dictionary")
#     print("3. Remove an element from the dictionary")
#     print("4. Display dictionary elements")
#     print("5. Exit")

def add_country():
    country = input("Enter the name of the country: ")
    capital = input("Enter the capital city: ")
    country_capitals[country] = capital
    print(f"{country} with capital {capital} added successfully.")

def update_country():
    country = input("Enter the name of the country to update: ")
    if country in country_capitals:
        capital = input("Enter the new capital city: ")
        country_capitals[country] = capital
        print(f"{country}'s capital updated to {capital}.")
    else:
        print("Country not found.")

def remove_country():
    country = input("Enter the name of the country to remove: ")
    if country in country_capitals:
        del country_capitals[country]
        print(f"{country} removed successfully.")
    else:
        print("Country not found.")

def display_countries():
    print("\nCountry and Capital List:")
    for country, capital in country_capitals.items():
        print(f"{country}: {capital}")

# Main program loop
def menu():
    while True:
        print("\nMenu:")
        print("1. Add a new element to the dictionary")
        print("2. Update an element in the dictionary")
        print("3. Remove an element from the dictionary")
        print("4. Display dictionary elements")
        print("5. Exit")

        # display_menu()
        choice = input("Select an option (1-5): ")

        if choice == '1':
            add_country()
        elif choice == '2':
            update_country()
        elif choice == '3':
            remove_country()
        elif choice == '4':
            display_countries()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

menu()