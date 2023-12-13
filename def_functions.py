def add_contact(phonebook, name, number):
    """Add a contact to the phonebook."""
    phonebook[name] = number
    print(f"Contact '{name}' added successfully.")

def view_contacts(phonebook):
    """View all contacts in the phonebook."""
    print("Contacts:")
    for name, number in phonebook.items():
        print(f"{name}: {number}")

def search_contacts(phonebook, name):
    """Search for a contact by name."""
    if name in phonebook:
        print(f"Contact found - {name}: {phonebook[name]}")
    else:
        print(f"Contact '{name}' not found in the phonebook.")

