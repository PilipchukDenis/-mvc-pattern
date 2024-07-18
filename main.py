from Model.model import PhoneBookModel
from View.view import PhoneBookView
from Controller.controller import PhoneBookController
def main():
    model = PhoneBookModel()
    view = PhoneBookView()
    controller = PhoneBookController(model, view)

    while True:
        print("1. Добавить контакт")
        print("2. Показать все контакты")
        print("3. Найти контакт")
        print("4. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            controller.add_contact()
        elif choice == '2':
            controller.show_all_contacts()
        elif choice == '3':
            controller.find_contact()
        elif choice == '4':
            break

if __name__ == "__main__":
    main()
