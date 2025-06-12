#  Create a contact book using dictionaries to store and manage names, phone numbers,
# and emails.

contact_book = {}

def add_details():
    n = int(input("how many detials you wnat t to addd: "))

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

def remove_details():
    label = input("enter label to delete: ")
    contact_book[label].pop()

def view_details():
    for i,j in contact_book.items():
        print(f"{i}: \nname: {j["name"]} phone_number = {j["phone_number"]} email = {j["email"]}")

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