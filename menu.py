def menu():
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Option 4")
    print("0. Exit the program.")


def option4():
    print("This is option 4.")

menu()

while True:
    try:
        option = int(input("Enter your option: "))
        if option == 0:
            break

        if option == 1:
            print("You selected option 1")
        elif option == 2:
            print("You selected option 2")
        elif option == 3:
            print("You selected option 3")
        elif option == 4:
            option4()
        else:
            print("Invalid Option.")

        print()
        menu()
    except ValueError:
        print("Please enter a valid number for your option.")
    

print("Thanks for using this program. Goodbye!")