# Final Project Program 
# I want to focus on dictionaries for this final project, as I feel like from the last two consolidation assignments I worked more
# lists and tuples.

import os # importing this just in case I need this.
import def_functions # 3.17 I created a separate python file for functions I'm using within this program.  
import json # Might be able to use this for advanced topic JSON... using file for saving contact history?  

phonebook_filename = "phonebook.json" #Will be the name of a previous phonebook saved file.  
phonebook = def_functions.load_phonebook(phonebook_filename) 
# phonebook is our dictionary that we will base our project on, we have two keys, the "name" and their "number".  
# RECENTLY CHANGED:  See def_functions, load_phonebook now defines phonebook as dictionary if cannot load phonebook file.  

count = 0 # Creating a count in case too many errors.
while True:
    print("\nPhonebook Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Delete Contact")
    print("5. Save Phonebook")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if count >= 4: #When count is greater than or equal to 4, then the program quits with a message.
        print("Too many invalid choices inputted, closing program.  Bye.")
        exit()

    if choice == '1':
        name = input("Enter contact name: ")
        number = def_functions.get_valid_number() # NEW function, where the phone number needs to be 10 digits.  
        def_functions.add_contact(phonebook, name, number) 
        # 5.17 Accessing the keys in a dictonary, with "name" and "number"
        # 5.19 Able to update values / add values into the dictionary.  

    elif choice == '2':
        def_functions.view_contacts(phonebook) # can just view def_functions for information on this.  

    elif choice == '3':
        name = input("\nEnter contact name to search: ")
        def_functions.search_contacts(phonebook, name)
        # 5.18 We are accessing the keys, to view the value in the dictionary.  In this case, we are pairing a name to a number.  

    elif choice == '4':
        name = input("Enter contact name to delete: ")
        def_functions.delete_contact(phonebook, name)
        # 5.11 Removing an item from a list iteratively.  

    elif choice =='5':
        def_functions.save_phonebook(phonebook, phonebook_filename) 
        # 10.5 Extracting and manipulating values from JSON formatted data!!!  see def_functions.

    elif choice == '6': # Simple quit function.  
        print("\nThanks for using this phonebook program, bye.")
        exit()
    
    else: # 4.9 raising an error and providing a helpful error message.  
        count += 1
        print("\nInvalid choice.  Enter numbers 1 through 6.")
    