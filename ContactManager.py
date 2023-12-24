class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = {"name": name, "phone": phone, "email": email}
        self.contacts.append(contact)
        print(f"Contact added: {name}")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return

        print("Contacts:")
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

    def edit_contact(self, index, name, phone, email):
        if 1 <= index <= len(self.contacts):
            self.contacts[index - 1] = {"name": name, "phone": phone, "email": email}
            print("Contact updated successfully.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 1 <= index <= len(self.contacts):
            deleted_contact = self.contacts.pop(index - 1)
            print(f"Contact deleted: {deleted_contact['name']}")
        else:
            print("Invalid contact index.")

contact_manager = ContactManager()

while True:
    print("\nContact Management Program")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        contact_manager.add_contact(name, phone, email)

    elif choice == "2":
        contact_manager.view_contacts()

    elif choice == "3":
        index = int(input("Enter the index of the contact to edit: "))
        name = input("Enter updated name: ")
        phone = input("Enter updated phone number: ")
        email = input("Enter updated email address: ")
        contact_manager.edit_contact(index, name, phone, email)

    elif choice == "4":
        index = int(input("Enter the index of the contact to delete: "))
        contact_manager.delete_contact(index)

    elif choice == "5":
        print("Exiting Contact Management Program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
