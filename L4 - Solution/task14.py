import json
from collections import Counter

def count_words(input_file_path, output_file_path):
    with open(input_file_path) as f:
        sentences = json.load(f)

    word_counts = Counter()
    for sentence in sentences:
        words = sentence.lower().split()
        word_counts.update(words)

    with open(output_file_path, 'w') as f:
        json.dump(dict(word_counts), f)