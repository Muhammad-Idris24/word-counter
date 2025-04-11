from .core import (
    read_file,
    preprocess_text,
    count_words,
    count_unique_words,
    get_word_frequencies
)
from .visualization import plot_word_frequencies

__version__ = "0.1.0"
__all__ = [
    'read_file',
    'preprocess_text',
    'count_words',
    'count_unique_words',
    'get_word_frequencies',
    'plot_word_frequencies',
    'WordCounterGUI',
    'run_gui'
]