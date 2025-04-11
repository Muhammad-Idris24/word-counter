# tests/test_cli.py
import unittest
from unittest.mock import patch
from io import StringIO
import word_counter.cli

class TestCLI(unittest.TestCase):
    @patch('sys.argv', ['cli.py', 'nonexistent.txt'])
    def test_file_not_found(self):
        with self.assertRaises(SystemExit):
            word_counter.cli.main()
    
    @patch('sys.argv', ['cli.py', 'test_file.txt'])
    @patch('word_counter.core.read_file')
    def test_main_execution(self, mock_read):
        mock_read.return_value = "test text"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            word_counter.cli.main()
            self.assertIn("Total words", fake_out.getvalue())