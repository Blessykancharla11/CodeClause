import string
from collections import Counter
import math
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return words

def calculate_cosine_similarity(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])

    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def get_text_vector(text):
    word_counts = Counter(text)
    return word_counts

def check_plagiarism(text1, text2, threshold=0.8):
    processed_text1 = preprocess_text(text1)
    processed_text2 = preprocess_text(text2)

    vector1 = get_text_vector(processed_text1)
    vector2 = get_text_vector(processed_text2)

    similarity = calculate_cosine_similarity(vector1, vector2)

    if similarity >= threshold:
        return True
    else:
        return False

def check_plagiarism_gui():
    def check_similarity():
        text1 = text_entry1.get("1.0", "end-1c")
        text2 = text_entry2.get("1.0", "end-1c")

        if check_plagiarism(text1, text2):
            result_label.config(text="Potential plagiarism detected.", fg="red")
        else:
            result_label.config(text="No plagiarism detected.", fg="green")

    root = tk.Tk()
    root.title("Plagiarism Checker")

    text_label1 = tk.Label(root, text="Enter the first text:", font=("Helvetica", 14))
    text_label1.pack(pady=(20, 0))

    text_entry1 = scrolledtext.ScrolledText(root, height=8, width=50, font=("Helvetica", 12))
    text_entry1.pack()

    text_label2 = tk.Label(root, text="Enter the second text:", font=("Helvetica", 14))
    text_label2.pack(pady=(20, 0))

    text_entry2 = scrolledtext.ScrolledText(root, height=8, width=50, font=("Helvetica", 12))
    text_entry2.pack()

    check_button = tk.Button(root, text="Check Plagiarism", command=check_similarity, font=("Helvetica", 14))
    check_button.pack(pady=(20, 0))

    result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
    result_label.pack(pady=(20, 0))

    root.mainloop()

if __name__ == '__main__':
    check_plagiarism_gui()
