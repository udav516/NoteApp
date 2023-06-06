import json
import os

notes = []


def save_notes():
    with open("notes.json", "w") as f:
        json.dump(notes, f)


def load_notes():
    global notes
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as f:
            notes = json.load(f)


def list_notes():
    for note in notes:
        print(note["id"], note["title"], note["date"])


def add_note(title, body, date):
    id = len(notes) + 1
    notes.append({"id": id, "title": title, "body": body, "date": date})
    save_notes()
    return print("Заметка добавлена")


def edit_note(id, title, body, date):
    for note in notes:
        if note["id"] == id:
            note["title"] = title
            note["body"] = body
            note["date"] = date
            save_notes()
            return print("Заметка отредактирована")


def delete_note(id):
    for note in notes:
        if note["id"] == id:
            notes.remove(note)
            save_notes()
            return print("Заметка удалена")
