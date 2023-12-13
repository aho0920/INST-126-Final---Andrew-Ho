# Final Project Program 

import os
import def_functions

phonebook = {}

while True:
    print("\nPhonebook Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        def_functions.add_contact(phonebook, name, number)

    elif choice == '2':
        def_functions.view_contacts(phonebook)