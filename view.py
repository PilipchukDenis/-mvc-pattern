

class PhoneBookView:
    @staticmethod
    def display_contact(contact):
        if contact:
            print(f"Имя: {contact.name}, Телефон: {contact.phone_number}")
        else:
            print("Контакт не найден.")

    @staticmethod
    def display_all_contacts(contacts):
        for contact in contacts:
            print(f"Имя: {contact.name}, Телефон: {contact.phone_number}")

    @staticmethod
    def prompt_for_contact_info():
        name = input("Введите имя: ")
        phone_number = input("Введите номер телефона: ")
        return name, phone_number

    @staticmethod
    def prompt_for_contact_name():
        return input("Введите имя контакта: ")


