# 📘 Mini Project: Contact Book Manager

# 👉 Features:

# 1. Add a new contact (name, phone, email).
# 2. View a contact.
# 3. Update contact.
# 4. Delete contact.
# 5. Show all contacts.
# 6. Exit.

contacts = {}

while True:
    print("\n----- Contact Book Manager -----\n")
    print("1. Add a new contact (name, phone, email)")
    print("2. View a contact")
    print("3. Update a contact")
    print("4. Delete contact")
    print("5. Show all contacts")
    print("6. Exit")

    choice = input("\nSelect your choice(1-6): ")

    if choice == "1":
        # add a new contact
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")

        contacts[name] = {
            "phone": phone,
            "email": email
        }

        print("✅ Contact added successfully.")

    elif choice == "2":
        # view a contact
        name_temp = input("Enter name of the contact: ")
        contact_keys = list(contacts.keys())

        if name in contact_keys:
            for name, details in contacts.items():
                print(f"Name: {name}")
                for key, value in details.items():
                    print(f"{key.capitalize()}: {value}")
        else:
            print("❌ No such name found in the contact list. Try again!")

    elif choice == "3":
        # update a contact
        name = input("Enter name to update: ")
        contact_keys = list(contacts.keys())
        if name in contact_keys:
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            contacts[name] = {"phone": new_phone, "email": new_email}
            print("✅ Contact updated!")
        else:
            print("❌ Contact not found!")
    elif choice == "4":
        # delete contact
        name = input("Enter Name to Delete: ")
        contact_keys = list(contacts.keys())

        if name in contact_keys:
            del contacts[name]
            print("🗑️ Contact deleted!")
        else:
            print("❌ Contact not found!")
    elif choice == "5":
        # show all contacts
        
        if len(contacts) == 0:
            print("Contact book is empty")
        else:
            for name, details in contacts.items():
                print(f"Name: {name}")
                for key, value in details.items():
                    print(f"{key.capitalize()}: {value}")
                print("---------------------")
    elif choice == "6":
        # Exit the program
        print("Thank you for using our software.")
        break
    else:
        print("Invalid choice. Please try again!")

    
