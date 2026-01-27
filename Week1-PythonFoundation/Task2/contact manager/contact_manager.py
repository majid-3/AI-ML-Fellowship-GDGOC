# This program can add and view contacts using a text file

CONTACT_FILE = "contacts.txt"

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    try:
        file = open(CONTACT_FILE, "a")
        file.write(name + "," + phone + "\n")
        file.close()
        print("Contact added successfully!")
    except:
        print("Error while adding contact.")

def view_contacts():
    try:
        file = open(CONTACT_FILE, "r")
        lines = file.readlines()
        file.close()

        if len(lines) == 0:
            print("No contacts found.")
            return

        print("\nContact List:")
        for line in lines:
            name, phone = line.strip().split(",")
            print("Name:", name, "\nPhone no:", phone)

    except FileNotFoundError:
        print("No contact file found.")
    except:
        print("Error while reading contacts.")


while True:
        print("Contact Manager Menu")
        print("1. Add Contact")
        print("2. View Contacts")       
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

