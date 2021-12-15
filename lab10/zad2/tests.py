from lab10.zad2.noteStorage import noteStorage
from lab10.zad2.noteService import noteService
from lab10.zad1.main import Note
from unittest.mock import *
from unittest import TestCase

class test_NotesService(TestCase):
    def setUp(self):
        self.storage = noteStorage()
        self.storage.add = Mock()
        self.storage.clear = Mock()
        self.storage.getAllNotesOf = Mock()

    
