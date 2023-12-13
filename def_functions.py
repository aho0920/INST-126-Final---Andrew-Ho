def add_contact(phonebook, name, number):
    """Add a contact to the phonebook."""
    phonebook[name] = number
    print(f"\nContact '{name}' added successfully.")

def view_contacts(phonebook):
    """View all contacts in the phonebook."""
    print("\nContacts:")
    for name, number in phonebook.items():
        print(f"\n{name}: {number}")

def search_contacts(phonebook, name):
    """Search for a contact by name."""
    if name in phonebook:
        print(f"\nContact found - {name}: {phonebook[name]}")
    else:
        print(f"\nContact '{name}' not found in the phonebook.")

