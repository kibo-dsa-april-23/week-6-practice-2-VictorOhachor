import unittest
import io
import sys
from llstring import LLString

class TestLLString(unittest.TestCase):
    def setUp(self):
        self.llstring = LLString('hello')

    def test_print_every_other(self):
        captured = io.StringIO()
        sys.stdout = captured
        self.llstring.print_every_other()
        sys.stdout = sys.__stdout__
        assert captured.getvalue() == 'hlo\n'

    def test_print_every_other_two(self):
        llstring = LLString('ab')
        captured = io.StringIO()
        sys.stdout = captured
        llstring.print_every_other()
        sys.stdout = sys.__stdout__
        assert captured.getvalue() == 'a\n'

    def test_print_every_other_empty(self):
        llstring = LLString('')
        captured = io.StringIO()
        sys.stdout = captured
        llstring.print_every_other()
        sys.stdout = sys.__stdout__
        assert captured.getvalue() == '\n'

    def test_char_at(self):
        char = self.llstring.char_at(3)
        assert char == 'l'

    def test_char_at_invalid(self):
        char = self.llstring.char_at(20)
        assert char == None

    def test_char_at_empty(self):
        empty = LLString('')
        char = empty.char_at(21)
        assert char == None

    def test_concat(self):
        other_llstring = LLString('orange')
        self.llstring.concat(other_llstring)
        assert self.llstring.to_string() == 'helloorange'

    def test_reverse(self):
        self.llstring.reverse()
        assert self.llstring().to_string() == 'olleh'

    def test_reverse(self):
        llstring = LLString('')
        assert llstring.to_string() == ''

    def test_index_of(self):
        assert self.llstring.index_of('l') == 2

    def test_index_of_invalid(self):
        assert self.llstring.index_of('a') == -1
