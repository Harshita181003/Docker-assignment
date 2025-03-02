import os
import re
import socket
from collections import Counter

# Define file paths
input_dir = "/home/data"
output_file = "/home/data/output/result.txt"
file1_path = os.path.join(input_dir, "IF-1.txt")
file2_path = os.path.join(input_dir, "AlwaysRememberUsThisWay-1.txt")

# Function to read and count words
def count_words(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        words = re.findall(r"\b\w+\b", file.read().lower())  # Extract words
    return words, Counter(words)

# Handle contractions in AlwaysRememberUsThisWay-1.txt
def handle_contractions(words):
    expanded_words = []
    for word in words:
        expanded_words.extend(re.split(r"['’]", word))  # Split contractions
    return Counter(expanded_words)

# Process IF-1.txt
words1, counter1 = count_words(file1_path)
top_3_if1 = counter1.most_common(3)

# Process AlwaysRememberUsThisWay-1.txt with contractions
words2, counter2 = count_words(file2_path)
top_3_if2 = handle_contractions(words2).most_common(3)

# Get container's IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Write results to output file
os.makedirs(os.path.dirname(output_file), exist_ok=True)
with open(output_file, "w") as f:
    f.write(f"Total words in {file1_path}: {len(words1)}\n")
    f.write(f"Total words in {file2_path}: {len(words2)}\n")
    f.write(f"Grand total words: {len(words1) + len(words2)}\n")
    f.write(f"Top 3 words in IF-1.txt: {top_3_if1}\n")
    f.write(f"Top 3 words in AlwaysRememberUsThisWay-1.txt: {top_3_if2}\n")
    f.write(f"Container IP Address: {ip_address}\n")

# Print results to console
with open(output_file, "r") as f:
    print(f.read())
 
