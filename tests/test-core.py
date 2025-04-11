import unittest
import os
from word_counter.core import read_file, preprocess_text, count_words, count_unique_words

class TestWordCounter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a temporary test file
        cls.test_file = "test_file.txt"
        with open(cls.test_file, 'w', encoding='utf-8') as f:
            f.write("Hello world! This is a test. Hello again.")
    
    @classmethod
    def tearDownClass(cls):
        # Clean up test file
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)
    
    def test_read_file(self):
        content = read_file(self.test_file)
        self.assertIsInstance(content, str)
        self.assertGreater(len(content), 0)
        
        with self.assertRaises(FileNotFoundError):
            read_file("nonexistent_file.txt")
    
    def test_preprocess_text(self):
        text = "Hello, World! 123"
        processed = preprocess_text(text)
        self.assertEqual(processed, "hello world 123")
    
    def test_count_words(self):
        text = "one two three four"
        self.assertEqual(count_words(text), 4)
        
        text = "word"
        self.assertEqual(count_words(text), 1)
        
        text = ""
        self.assertEqual(count_words(text), 0)
    
    def test_count_unique_words(self):
        text = "hello world hello"
        self.assertEqual(count_unique_words(text), 2)

if __name__ == "__main__":
    unittest.main()