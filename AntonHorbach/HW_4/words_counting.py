import re

path_to_text = input("Enter path to text: ")

with open(path_to_text) as f:
    text = f.read()

sentences = re.split(r'([\w][^?!.]*[.?!])', text, flags=re.IGNORECASE)
for sentence in sentences:
    print(sentence)
    print("BREAK!!!")
