# Final Project Program 

import os # importing this just in case I need this.
import def_functions # 3.17 I created a separate python file for functions I'm using within this program.  

phonebook = {} # phonebook is our dictionary that we will base our project on, we have two keys, the "name" and their "number".  

count = 0 # Creating a count in case too many errors.
while True:
    print("\nPhonebook Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if count >= 4: #When count is greater than or equal to 4, then the program quits with a message.
        print("Too many invalid choices inputted, closing program.  Bye.")
        exit()

    if choice == '1':
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        def_functions.add_contact(phonebook, name, number) 
        # 5.17 Accessing the keys in a dictonary, with "name" and "number"
        # 5.19 Able to update values / add values into the dictionary.  

    elif choice == '2':
        def_functions.view_contacts(phonebook)

    elif choice == '3':
        name = input("\nEnter contact name to search: ")
        def_functions.search_contacts(phonebook, name)
        # 5.18 We are accessing the keys, to view the value in the dictionary.  In this case, we are pairing a name to a number.  

    elif choice == '4': # Simple quit function.  
        print("\nThanks for using this phonebook program, bye.")
        exit()
    
    else: # 4.9 raising an error and providing a helpful error message.  
        count += 1
        print("\nInvalid choice.  Enter numbers 1 through 4.")
    