# Project: Contact Book with File Handling
# This project will allow users to add, view, update, delete, and save contacts using file handling.

# Features:
# Add Contact – Store name, phone, and email.

# View Contacts – Display all stored contacts.

# Update Contact – Modify existing details.

# Delete Contact – Remove a contact.

# Save Contacts – Store data in a file.

# Load Contacts – Retrieve saved data when the program starts.

import json

contact_book = {}

def load_contact():
    global contact_book
    try:
        with open("contact.json","r") as file:
            contact_book = json.load(file)
    except FileNotFoundError:
        contact_book = {}

def save_contact():
    with open("contact.json", "w") as file:
        json.dump(contact_book, file, indent=4)

def add_details():
    n = int(input("how many details you want to add: "))

    for i in range(n):
        label = input("\nenter lkabel: ")
        name = input("enter name; ")
        pn = input("enter phne number: ")
        email = input("enter email: ")

        contact_book[label]= {
            "name": name,
            "phone_number": pn,
            "email": email
        }
    save_contact()

def remove_details():
    label = input("Enter label to delete: ")
    if label in contact_book:
        del contact_book[label]
        save_contact()
        print(f"Contact {label} removed successfully.")
    else:
        print(f"Contact {label} not found.")

def view_details():
    try:
        with open("contact.json","r") as file:
            print(json.dumps(json.load(file),indent=4))
    except Exception as e:
        print("file doesn't exist",e)



load_contact()

while True:
    print("\n1. Add detals\n" \
    "2. remove detils\n" \
    "3. view drtials\n" \
    "4. exit\n")

    userinput = int(input("which option do you select: "))

    match userinput:
        case 1:
            add_details()
        case 2:
            remove_details()
        case 3:
            view_details()
        case 4:
            break    