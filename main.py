import datetime
import note_manager


def main():
    note_manager.load_notes()

    while True:
        print("""Введите команду:
        1 - Список заметок
        2 - Добавить заметку
        3 - Редактировать заметку
        4 - Поиск заметки
        5 - Удалить заметку
        0 - Выход""")
        choice = input()

        if choice == "1":
            note_manager.list_notes()
        elif choice == "2":
            title = input("Введите название заметки: ")
            body = input("Введите текст заметки: ")
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            note_manager.add_note(title, body, date)
        elif choice == "3":
            id = int(input("Введите номер заметки: "))
            title = input("Введите новое название заметки: ")
            body = input("Введите новый текст заметки: ")
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            note_manager.edit_note(id, title, body, date)
        elif choice == '4':
            id = int(input("Введите номер заметки: "))
            title = input("Введите новое название заметки: ")
            body = input("Введите новый текст заметки: ")
            note_manager.search_note(id, title, body)
        elif choice == "5":
            id = int(input("Введите номер заметки: "))
            note_manager.delete_note(id)
        elif choice == "0":
            return print("Рад был помочь, заходите ещё")
        else:
            print("Неверная команда")


if __name__ == "__main__":
    main()


