contact = {}

while  True:
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    choice = input("enter choice (1-5)")
    if choice == "1":
        name = input("enter name ")
        number = int(input("enter contact number "))

        if name in contact:
            print("Contact already exists.")
        else:
            contact[name] = number
            print("contact added successfully")

    elif choice == "2":
            if not contact:
                print("not contact found")
            else:
                 for name, number in contact.items():
                      print(name," : ",number)
    elif choice == "3":
            name = input("enter name you want to updated : ")

            if name in contact:
                 new_number = input("enter new number ")
                 contact[name] = new_number
                 print("contact update successfully")
            else:
                 print("contact not found")
    elif choice == "4":
            name = input("enter name you want to delete : ")
            if name in contact:
                 del contact[name]
                 print("contact delete successfully")
            else:
                 print("contact not found")
    elif choice == "5":
            print("program stop")
            break
    else:
         print("invalid choice, try again",choice)