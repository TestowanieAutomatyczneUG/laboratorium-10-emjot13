from lab10.zad2.noteStorage import noteStorage


class noteService:
    def __init__(self):
        self.storage = noteStorage()

    def add(self, note):
        return self.storage.add(note)

    def averageOf(self, name):
        notes = self.storage.getAllNotesOf(name)
        if len(notes.values()) != 0:
            return round(sum(notes.values()) / len(notes), 2)
        return 0

    def clear(self):
        return self.storage.clear()

