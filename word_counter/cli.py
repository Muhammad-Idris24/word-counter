import argparse
from .core import read_file, preprocess_text, count_words, count_unique_words, get_word_frequencies
from .visualization import plot_word_frequencies

def main():
    parser = argparse.ArgumentParser(description='Word Counter - Count words in a text file.')
    parser.add_argument('file_path', help='Path to the text file')
    parser.add_argument('--unique', action='store_true', help='Count unique words')
    parser.add_argument('--frequencies', action='store_true', help='Show word frequencies')
    parser.add_argument('--visualize', action='store_true', help='Visualize top word frequencies')
    parser.add_argument('--top', type=int, default=10, help='Number of top words to visualize (default: 10)')
    
    args = parser.parse_args()
    
    try:
        # Read and preprocess file
        text = read_file(args.file_path)
        processed_text = preprocess_text(text)
        
        # Basic word count
        total_words = count_words(processed_text)
        print(f"Total words: {total_words}")
        
        # Optional features
        if args.unique:
            unique_words = count_unique_words(processed_text)
            print(f"Unique words: {unique_words}")
            
        if args.frequencies:
            frequencies = get_word_frequencies(processed_text)
            print("\nWord frequencies:")
            for word, count in frequencies.most_common():
                print(f"{word}: {count}")
                
        if args.visualize:
            frequencies = get_word_frequencies(processed_text)
            plot_word_frequencies(frequencies, top_n=args.top)
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()