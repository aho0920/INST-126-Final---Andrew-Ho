import json #importing json here to use def function with json.

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

def get_valid_number():
    """Get a valid phone number from the user."""
    while True:
        number = input("Enter contact number (format: ***-***-****): ")
        if validate_number(number):
            return number
        else:
            print("That is an invalid phone number format!  Try again.")
    # This function replaces the number input for adding a contact.  And it is paired with another function to ensure the length,
    # Basically, each function needs to be 10 digits resembling a real phone number. 

def validate_number(number):
    """Validates the format of a phone number."""
    return len(number) == 10
    # This function checks for 10 digit phone number.  

def load_phonebook(filename="phonebook.json"):
    """Load a phonebook file previously saved"""
    try:
        with open(filename, "r") as file: #Seen in class, filename and "r"
            return json.load(file) # found out how to use json import, just mainly using load to load json into program, and dump to extract
                                    # data from program into json file.  
    except FileNotFoundError:
        return {}
    # This functions tries to load a phonebook saved into our project file.
    # The phonebook file should be named "phonebook.json" as created by save function.  
    # We are using a try / except function so that if there is no phonebook.json, then phonebook will be loaded as default dictionary. 
    # If phonebook.json is found, then the dictionary will be loaded including saved contacts.  
    
def save_phonebook(phonebook, filename="phonebook.json"):
    """Saves phonebook as a file"""
    with open(filename, "w") as file:
        json.dump(phonebook, file)
    print(f"Phonebook saved to '{filename}'.")
    # This function is used to save contacts we created in program as a json file.  
    # I don't care about things being rewritten, so we are using "w" to overwrite the same file as phonebook.json.  
    # This phonebook will load whatever is previously saved from last time using program.  