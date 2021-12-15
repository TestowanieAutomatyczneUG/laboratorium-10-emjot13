from lab10.zad2.noteStorage import noteStorage


class noteService:
    def __init__(self, storage: noteStorage):
        self.storage = storage

    def add(self, note):
        self.storage.add(note)

    def averageOf(self, name):
        notes = self.storage.getAllNotesOf(name)
        if len(notes) != 0:
            return round(notes / len(notes), 2)
        return 0

    def clear(self):
        return self.storage.clear()

