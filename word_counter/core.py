import string
from collections import Counter

def read_file(file_path):
    """
    Read content from a text file.
    
    Args:
        file_path (str): Path to the text file
        
    Returns:
        str: Content of the file
        
    Raises:
        FileNotFoundError: If file doesn't exist
        UnicodeDecodeError: If file encoding isn't supported
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except UnicodeDecodeError:
        raise UnicodeDecodeError("Could not decode the file with 'utf-8' encoding.")

def preprocess_text(text):
    """
    Normalize text by removing punctuation and converting to lowercase.
    
    Args:
        text (str): Raw text input
        
    Returns:
        str: Processed text
    """
    # Remove punctuation using string.punctuation
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    
    # Convert to lowercase
    return text.lower()

def count_words(text):
    """
    Count total words in the text.
    
    Args:
        text (str): Input text
        
    Returns:
        int: Total word count
    """
    words = text.split()
    return len(words)

def count_unique_words(text):
    """
    Count unique words in the text.
    
    Args:
        text (str): Input text
        
    Returns:
        int: Count of unique words
    """
    words = text.split()
    return len(set(words))

def get_word_frequencies(text):
    """
    Calculate frequency of each word in the text.
    
    Args:
        text (str): Input text
        
    Returns:
        collections.Counter: Word frequency counter
    """
    words = text.split()
    return Counter(words)