import json
import datetime

def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file)

def load_notes():
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

def view_notes(notes):
    for note in notes:
        print("ID:", note["id"])
        print("Заголовок:", note["title"])
        print("Тело заметки:", note["body"])
        print("Дата создания:", note["date_created"])
        print("Дата последнего изменения:", note["date_modified"])
        print()

def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    date_created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_modified = date_created
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "date_created": date_created,
        "date_modified": date_modified
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка сохранена.")

def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note["id"] == note_id:
            title = input("Введите новый заголовок заметки: ")
            note["title"] = title
            body = input("Введите новое тело заметки: ")
            note["body"] = body
            note["date_modified"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка отредактирована.")
            return
    print("Заметка с указанным ID не найдена.")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка удалена.")
            return
    print("Заметка с указанным ID не найдена.")

def filter_notes_by_date():
    filter_date = input("Введите дату для фильтрации (гггг-мм-дд): ")
    filtered_notes = [note for note in notes if note["date_created"].startswith(filter_date) or note["date_modified"].startswith(filter_date)]
    view_notes(filtered_notes)

notes = load_notes()

while True:
    print()
    print("Меню:")
    print("1. Просмотреть заметки")
    print("2. Добавить заметку")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Фильтрация заметок по дате")
    print("6. Выйти из программы")
    choice = input("Выберите пункт меню (1-6): ")

    if choice == "1":
        view_notes(notes)
    elif choice == "2":
        add_note()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        filter_notes_by_date()
    elif choice == "6":
        break
    else:
        print("Некорректный выбор. Повторите попытку.")