from Model.model import Contact


class PhoneBookController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_contact(self):
        name, phone_number = self.view.prompt_for_contact_info()
        contact = Contact(name, phone_number)
        self.model.add_contact(contact)

    def show_all_contacts(self):
        contacts = self.model.get_all_contacts()
        self.view.display_all_contacts(contacts)

    def find_contact(self):
        name = self.view.prompt_for_contact_name()
        contact = self.model.find_contact(name)
        self.view.display_contact(contact)

