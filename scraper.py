import requests
import re
from bs4 import BeautifulSoup

# URL of the five-letter word list on WordFind
url = "https://wordfind.com/length/5-letter-words/"

# Fetch the page content
d = requests.get(url)
d.raise_for_status()

# Parse HTML
soup = BeautifulSoup(d.text, "html.parser")

# Extract all text and normalize to lowercase
text = soup.get_text(separator=" ").lower()

# Use regex to find all five-letter alphabetical words
raw_words = re.findall(r"\b[a-z]{5}\b", text)

# Deduplicate and sort
words = sorted(set(raw_words))

# Output file
output_file = "five_letter_words.txt"
with open(output_file, "w") as f:
    for w in words:
        f.write(w + "\n")
