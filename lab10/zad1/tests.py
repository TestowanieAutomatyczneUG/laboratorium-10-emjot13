from lab10.zad1.main import Note
import unittest

class Tests(unittest.TestCase):
    def setUp(self):
        self.temp = Note("aaa", 2.88)

    def tearDown(self):
        self.temp = None


    def test_get_name(self):
        self.assertEqual("aaa", self.temp.getName())
    
    def test_get_note(self):
        self.assertEqual(2.88, self.temp.getNote())
        
    def test_0_length(self):
        self.assertRaises(Exception, Note, "", 5.99)

    def test_note_too_low(self):
        self.assertRaises(Exception, Note, "AA", 1.9)

    def test_note_negative(self):
        self.assertRaises(Exception, Note, "AA", -3.1)

    def test_note_too_high(self):
        self.assertRaises(Exception, Note, "AA", 6.9)

    def test_name_is_none(self):
        self.assertRaises(Exception, Note, None, 4.1)

    def test_name_is_list(self):
        self.assertRaises(Exception, Note, ["aa"], 4.55)

    def test_name_is_dict(self):
        self.assertRaises(Exception, Note, {"aa": "xy"}, 5.0)

    def test_note_is_string(self):
        self.assertRaises(Exception, Note, "aa", "5.5")

    def test_arguments_in_bad_order(self):
        self.assertRaises(Exception, Note, 5.5, "AA")

    def test_note_is_none(self):
        self.assertRaises(Exception, Note, "AA", None)

    def test_note_is_int(self):
        self.assertRaises(Exception, Note, "XY", 5)

    def test_note_is_list(self):
        self.assertRaises(Exception, Note, "AA", [1])

    def test_name_is_true(self):
        self.assertRaises(Exception, Note, True, 4.1)

    def test_name_is_false(self):
        self.assertRaises(Exception, Note, False, 4.1)

    def test_note_is_true(self):
        self.assertRaises(Exception, Note, "XX", True)

    def test_name_is_false(self):
        self.assertRaises(Exception, Note, "AA", False)

