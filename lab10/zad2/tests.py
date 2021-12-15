from lab10.zad2.noteStorage import noteStorage
from lab10.zad2.noteService import noteService
from lab10.zad1.main import Note
from unittest.mock import *
from unittest import TestCase
import random as rd



def make_dict(size):
    dict = {}
    for k in range(1, size):
        dict["spr" + str(k)] = rd.randint(2, 6)
    avg = round(sum(dict.values()) / len(dict.values()), 2)
    return dict, avg

class test_NotesService(TestCase):
    def setUp(self):
        self.noteService = noteService()


    @patch.object(noteStorage, 'add')
    def test_add(self, mock_method):
        note = Note('aaa', 5.5)
        mock_method.return_value = 5.5
        self.assertEqual(self.noteService.add(note), 5.5)


    @patch.object(noteStorage, 'add')
    def test_add_almost_too_low(self, mock_method):
        note = Note('aaa', 2.0000001)
        mock_method.return_value = 2.0000001
        self.assertEqual(self.noteService.add(note), 2.0000001)

    @patch.object(noteStorage, 'add')
    def test_add_almost_too_high(self, mock_method):
        note = Note('aaa', 5.9999999999)
        mock_method.return_value = 5.9999999999
        self.assertEqual(self.noteService.add(note), 5.9999999999)


    @patch.object(noteStorage, 'getAllNotesOf')
    def test_average_simple(self, mock_method):
        mock_method.return_value = {"spr1": 2.0, "spr2": 6.0}
        self.assertEqual(self.noteService.averageOf('AA'), 4.0)


    @patch.object(noteStorage, 'getAllNotesOf')
    def test_average_100_notes(self, mock_method):
        dict, avg = make_dict(101)
        mock_method.return_value = dict
        self.assertEqual(self.noteService.averageOf('AA'), avg)

    @patch.object(noteStorage, 'getAllNotesOf')
    def test_average_1000_notes(self, mock_method):
        dict, avg = make_dict(1001)
        mock_method.return_value = dict
        self.assertEqual(self.noteService.averageOf('AA'), avg)

    @patch.object(noteStorage, 'getAllNotesOf')
    def test_average_10000_notes(self, mock_method):
        dict, avg = make_dict(10001)
        mock_method.return_value = dict
        self.assertEqual(self.noteService.averageOf('AA'), avg)

    @patch.object(noteStorage, 'getAllNotesOf')
    def test_average_100000_notes(self, mock_method):
        dict, avg = make_dict(100001)
        mock_method.return_value = dict
        self.assertEqual(self.noteService.averageOf('AA'), avg)

    @patch.object(noteStorage, 'getAllNotesOf')
    def test_average_milion_notes(self, mock_method):
        dict, avg = make_dict(1000001)
        mock_method.return_value = dict
        self.assertEqual(self.noteService.averageOf('AA'), avg)
    

    @patch.object(noteStorage, 'clear')
    def test_clear(self, mock_method):
        mock_method.return_value = True
        self.assertEqual(self.noteService.clear(), True)

