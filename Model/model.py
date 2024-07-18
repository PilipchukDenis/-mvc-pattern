# Реализовать mvc pattern для записи контактов в телефонную книгу




class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class PhoneBookModel:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def get_all_contacts(self):
        return self.contacts

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None












