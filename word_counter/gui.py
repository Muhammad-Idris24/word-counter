import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from .core import read_file, preprocess_text, count_words, count_unique_words, get_word_frequencies
from .visualization import plot_word_frequencies
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class WordCounterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Counter GUI")
        self.root.geometry("800x600")
        
        self.create_widgets()
        self.setup_layout()
        
    def create_widgets(self):
        # File Selection
        self.file_frame = ttk.LabelFrame(self.root, text="File Selection")
        self.file_path = tk.StringVar()
        ttk.Entry(self.file_frame, textvariable=self.file_path, width=50).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.file_frame, text="Browse", command=self.browse_file).pack(side=tk.LEFT)
        
        # Analysis Options
        self.options_frame = ttk.LabelFrame(self.root, text="Analysis Options")
        self.show_unique = tk.BooleanVar(value=True)
        self.show_frequencies = tk.BooleanVar(value=True)
        self.show_visualization = tk.BooleanVar(value=True)
        ttk.Checkbutton(self.options_frame, text="Show Unique Words", variable=self.show_unique).pack(anchor=tk.W)
        ttk.Checkbutton(self.options_frame, text="Show Word Frequencies", variable=self.show_frequencies).pack(anchor=tk.W)
        ttk.Checkbutton(self.options_frame, text="Show Visualization", variable=self.show_visualization).pack(anchor=tk.W)
        
        # Visualization Options
        self.viz_frame = ttk.LabelFrame(self.root, text="Visualization Options")
        self.top_n = tk.IntVar(value=10)
        ttk.Label(self.viz_frame, text="Top N Words:").pack(side=tk.LEFT)
        ttk.Spinbox(self.viz_frame, from_=1, to=50, textvariable=self.top_n, width=5).pack(side=tk.LEFT)
        
        # Results Display
        self.results_frame = ttk.LabelFrame(self.root, text="Results")
        self.results_text = tk.Text(self.results_frame, height=10, wrap=tk.WORD)
        self.results_scroll = ttk.Scrollbar(self.results_frame, command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=self.results_scroll.set)
        
        # Visualization Canvas
        self.viz_canvas_frame = ttk.LabelFrame(self.root, text="Visualization")
        self.figure = plt.Figure(figsize=(6, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.viz_canvas_frame)
        
        # Action Button
        self.analyze_button = ttk.Button(self.root, text="Analyze Text", command=self.analyze_text)
        
    def setup_layout(self):
        self.file_frame.pack(fill=tk.X, padx=5, pady=5)
        self.options_frame.pack(fill=tk.X, padx=5, pady=5)
        self.viz_frame.pack(fill=tk.X, padx=5, pady=5)
        self.analyze_button.pack(pady=10)
        
        # Results area
        self.results_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.results_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.results_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Visualization area
        self.viz_canvas_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def create_menu(self):
        menubar = tk.Menu(self.root)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.browse_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)
        
        self.root.config(menu=menubar)
        
    def add_text_preview(self, filepath=None):
        self.preview_frame = ttk.LabelFrame(self.root, text="Text Preview")
        self.preview_text = tk.Text(self.preview_frame, height=5, wrap=tk.WORD)
        self.preview_scroll = ttk.Scrollbar(self.preview_frame, command=self.preview_text.yview)
        self.preview_text.configure(yscrollcommand=self.preview_scroll.set)
        
        self.preview_frame.pack(fill=tk.X, padx=5, pady=5)
        self.preview_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.preview_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Update in browse_file method
        if filepath:
            self.file_path.set(filepath)
            with open(filepath, 'r') as f:
                self.preview_text.delete(1.0, tk.END)
                self.preview_text.insert(tk.END, f.read(1000))  # Show first 1000 chars
    
    def add_export_button(self):
        self.export_button = ttk.Button(
            self.root, 
            text="Export Results", 
            command=self.export_results
        )
        self.export_button.pack(pady=5)
    
    def export_results(self):
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("CSV files", "*.csv")]
        )
        if filepath:
            if filepath.endswith('.csv'):
                self.export_to_csv(filepath)
            else:
                self.export_to_txt(filepath)
            
    def browse_file(self):
        filepath = filedialog.askopenfilename(
            title="Select a text file",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filepath:
            self.file_path.set(filepath)
            
    def analyze_text(self):
        if not self.file_path.get():
            messagebox.showerror("Error", "Please select a file first")
            return
            
        try:
            # Clear previous results
            self.results_text.delete(1.0, tk.END)
            self.figure.clf()
            
            # Process file
            text = read_file(self.file_path.get())
            processed_text = preprocess_text(text)
            
            # Basic count
            total_words = count_words(processed_text)
            self.results_text.insert(tk.END, f"Total words: {total_words}\n\n")
            
            # Unique words
            if self.show_unique.get():
                unique_words = count_unique_words(processed_text)
                self.results_text.insert(tk.END, f"Unique words: {unique_words}\n\n")
            
            # Word frequencies
            if self.show_frequencies.get():
                frequencies = get_word_frequencies(processed_text)
                self.results_text.insert(tk.END, "Word frequencies:\n")
                for word, count in frequencies.most_common(10):
                    self.results_text.insert(tk.END, f"{word}: {count}\n")
            
            # Visualization
            if self.show_visualization.get():
                frequencies = get_word_frequencies(processed_text)
                ax = self.figure.add_subplot(111)
                top_words = frequencies.most_common(self.top_n.get())
                words, counts = zip(*top_words)
                
                ax.bar(words, counts)
                ax.set_xlabel('Words')
                ax.set_ylabel('Frequency')
                ax.set_title(f'Top {self.top_n.get()} Most Frequent Words')
                ax.tick_params(axis='x', rotation=45)
                self.figure.tight_layout()
                self.canvas.draw()
                
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            
            

def run_gui():
    root = tk.Tk()
    app = WordCounterGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()