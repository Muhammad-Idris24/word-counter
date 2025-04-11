import matplotlib.pyplot as plt

def plot_word_frequencies(word_counter, top_n=10):
    """
    Create a bar plot of the most common words.
    
    Args:
        word_counter (collections.Counter): Word frequency counter
        top_n (int): Number of top words to display
    """
    top_words = word_counter.most_common(top_n)
    words, counts = zip(*top_words)
    
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title(f'Top {top_n} Most Frequent Words')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()