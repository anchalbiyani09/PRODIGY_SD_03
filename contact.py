import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog

class ContactManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Manager")

        # Create a custom style
        style = ttk.Style()
        style.configure("Custom.Treeview", background="#f0f0f0", foreground="black", fieldbackground="#f0f0f0")

        # Create a Treeview for displaying contacts
        columns = ("Name", "Phone", "Email")
        self.tree = ttk.Treeview(master, columns=columns, show="headings", style="Custom.Treeview")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        self.tree.pack(pady=10)

        # Buttons for actions
        button_style = {"background": "#4CAF50", "foreground": "white"}

        add_button = tk.Button(master, text="Add Contact", command=self.add_contact, **button_style)
        add_button.pack(side=tk.LEFT, padx=10)

        edit_button = tk.Button(master, text="Edit Contact", command=self.edit_contact, **button_style)
        edit_button.pack(side=tk.LEFT, padx=10)

        delete_button = tk.Button(master, text="Delete Contact", command=self.delete_contact, **button_style)
        delete_button.pack(side=tk.LEFT, padx=10)

        # List to store user-defined contacts
        self.contacts = []

    def load_contacts(self):
        # Add contacts to the Treeview
        for contact in self.contacts:
            self.tree.insert("", "end", values=contact)

    def add_contact(self):
        name = simpledialog.askstring("Add Contact", "Enter name:")
        if name:
            phone = simpledialog.askstring("Add Contact", "Enter phone number:")
            email = simpledialog.askstring("Add Contact", "Enter email address:")
            contact = (name, phone, email)
            self.contacts.append(contact)
            self.tree.insert("", "end", values=contact)

    def edit_contact(self):
        selected_item = self.tree.selection()
        if selected_item:
            selected_contact = self.tree.item(selected_item, 'values')
            name = simpledialog.askstring("Edit Contact", "Enter new name:", initialvalue=selected_contact[0])
            if name:
                phone = simpledialog.askstring("Edit Contact", "Enter new phone number:", initialvalue=selected_contact[1])
                email = simpledialog.askstring("Edit Contact", "Enter new email address:", initialvalue=selected_contact[2])
                updated_contact = (name, phone, email)
                self.contacts[self.contacts.index(selected_contact)] = updated_contact
                self.tree.item(selected_item, values=updated_contact)

    def delete_contact(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)
            selected_contact = self.tree.item(selected_item, 'values')
            self.contacts.remove(selected_contact)


def main():
    root = tk.Tk()

    # Set a custom font for the application
    custom_font = ("Helvetica", 12)
    root.option_add('*Font', custom_font)

    # Set a custom background color for the application
    root.configure(bg="#f0f0f0")

    # Create the ContactManagerApp
    app = ContactManagerApp(root)

    root.mainloop()

if __name__ == "__main__":
    main()