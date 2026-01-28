---

# Contact Management System

A simple **Python-based Contact Management System** that allows you to **add, view, update, and delete contacts** via a command-line interface.

---

## Features

* **Add Contact**: Store a new contact with a name and phone number.
* **View Contacts**: Display all saved contacts.
* **Update Contact**: Modify the phone number of an existing contact.
* **Delete Contact**: Remove a contact from the system.
* **Exit Program**: Safely close the application.

---

## Installation

1. Make sure you have **Python 3.x** installed on your system.
2. Clone this repository or copy the `contact_management.py` file to your local machine.
3. Navigate to the directory containing the file using the terminal/command prompt.

---

## Usage

Run the program using Python:

```bash
python contact_management.py
```

You will see a menu like this:

```
--- Contact Management System ---
1. Add Contact
2. View Contacts
3. Update Contact
4. Delete Contact
5. Exit
```

Enter the number corresponding to the action you want to perform.

Example workflow:

1. Add a contact:

```
enter choice (1-5): 1
enter name: John
enter contact number: 123456789
contact added successfully
```

2. View all contacts:

```
enter choice (1-5): 2
John : 123456789
```

3. Update a contact:

```
enter choice (1-5): 3
enter name you want to updated: John
enter new number: 987654321
contact update successfully
```

4. Delete a contact:

```
enter choice (1-5): 4
enter name you want to delete: John
contact delete successfully
```

5. Exit:

```
enter choice (1-5): 5
program stop
```

---

## Notes

* Contact names are **case-sensitive**.
* Only **one contact per name** is allowed.
* Ensure you enter **valid integers** for contact numbers.

---

This project is open-source and free to use.

---

