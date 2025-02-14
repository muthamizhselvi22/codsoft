import json

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    for name, details in contacts.items():
        print(f"{name}: {details}")

# Search for a contact
def search_contact():
    query = input("Enter name or phone number to search: ")
    for name, details in contacts.items():
        if query in name or query in details["Phone"]:
            print(f"Found: {name} - {details}")
            return
    print("Contact not found.")

# Update a contact
def update_contact():
    name = input("Enter name of contact to update: ")
    if name in contacts:
        phone = input(f"Enter new phone number (current: {contacts[name]['Phone']}): ") or contacts[name]['Phone']
        email = input(f"Enter new email (current: {contacts[name]['Email']}): ") or contacts[name]['Email']
        address = input(f"Enter new address (current: {contacts[name]['Address']}): ") or contacts[name]['Address']

        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

# Delete a contact
def delete_contact():
    name = input("Enter name of contact to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

# Main menu
contacts = load_contacts()

while True:
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        break
    else:
        print("Invalid choice, try again.")
