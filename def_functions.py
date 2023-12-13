def add_contact(phonebook, name, number):
    """Add a contact to the phonebook."""
    if name not in phonebook:
        phonebook[name] = number
        print(f"\nContact '{name}' added successfully.")
    else:
        print(f"Contact '{name}' already exists!  Choose a different name!") 
        
    # 3.13 Using the f-string operator to make output easier to read.  
    # First function into my final program.  Phonebook is the dictionary I created in the main file, and name and number are the two keys
    # that are pairing with each other.  

def view_contacts(phonebook):
    """View all contacts in the phonebook."""
    if phonebook:
        print("\nContacts:")
        for name, number in phonebook.items():
            print(f"\n{name}: {number}")
    else: 
        print("Your phonebook is empty.")
    # Second function in my final program for viewing all contacts created.  This is so we can retrieve all names and numbers associated
    # with each other in our phonebook dictionary through the use of .items and the two keys we created.  

def search_contacts(phonebook, name):
    """Search for a contact by name."""
    if name in phonebook:
        print(f"\nContact found - {name}: {phonebook[name]}")
    else:
        print(f"\nContact '{name}' not found in the phonebook.")
    # A simple way I've made to search for a number in our dictionary using the name associated with the number.

def delete_contact(phonebook, name):
    """Delete a contact by their name."""
    if name in phonebook:
        del phonebook[name]
        print(f"Contact '{name}' has been deleted.")
    else:
        print(f"Contact '{name}' not found in the phonebook.") 
    # I wanted to add another option which is to delete a contact that has been created.  Utilizing "del" and specifying dictionary
    # and the key we want to delete.  So specifying the name and deleting the name and data associated with that key.  