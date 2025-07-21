:

📞 Phone Book Program (Python Dictionary Project)
This is a simple Phone Book application built using the concept of dictionaries in Python. It allows users to store, add, delete, and search for contact numbers efficiently.

🚀 Features
View all contacts in the phone book.

Add a new contact.

Delete an existing contact.

Search for a contact by name.

🧠 Concepts Used
Python Dictionaries (dict)

for loops

input() function

Conditional statements (if)

del keyword

📄 Code Overview
python
Copy
Edit
Phoe_book = {
    'Rahul': 9365476198,
    'Mohan': 7002605460,
    'Neha': 8011224629,
    'old_man': 9101124288
}

# Display all contacts
for key, value in Phoe_book.items():
    print(f'The phonebook is {key}:{value}')

# Add a new contact
print('\nHere is the feature using which a user can add new contact on phone-book.')
new_name = input('Enter your name: ')
new_contact = int(input('Enter your number = '))
Phoe_book[new_name] = new_contact

# Display updated phonebook
for key, value in Phoe_book.items():
    print(f'The phonebook is {key}:{value}')

# Delete a contact
print('\nHere is the feature using which a user can delete any existing contact on phone-book.')
Delete = input('Enter your name: ')
del Phoe_book[Delete]

# Display updated phonebook
for key, value in Phoe_book.items():
    print(f'The phonebook is {key}:{value}')

# Search for a contact
Search = input('Enter your name: ')
if Search in Phoe_book:
    print(f'In the search, person\'s contact number is: {Phoe_book[Search]}')
✅ How to Run
Make sure Python is installed on your system.

Save the code in a file, e.g., phonebook.py.

Open a terminal or command prompt and run:



Allow multiple operations in a loop.

Save and load data from a file for persistence.

Use functions to modularize code.

