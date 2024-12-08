import string 
from collections import Counter
import re

import enchant

english_dict = enchant.Dict("en_US")

def read_file(file_path):
    try:
        with open(file_path,'r',encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: The File '{file_path}' does not exist. ")
        return []
    
def clean_text(text):
    # Remove punctuation
    text = text.translate(str.maketrans('','',string.punctuation))
    # Remove non-English words 
    words = re.findall(r'\b[a-zA-z]+\b',text)
    # Convert to lowercase & checks vaildation
    valid_words = [word.lower() for word in words if check_in_dictionary(word)]
    return ' '.join(valid_words)

def check_in_dictionary(word):
    #print(f"Checking: {word}")
    return english_dict.check(word)
    

def count_words(words):
    all_words = []
    for word in words:
        all_words.extend(word.split())
    return Counter(all_words)

def top_words(words_counts, top_n=20):
    return words_counts.most_common(top_n)

def save_cleaned_text(words,output_file):
    try:
        with open(output_file,'w',encoding='utf-8') as file:
            file.writelines(line + '\n' for line in words)
        print(f"Cleaned words saved to '{output_file}' ")
    except IOError as e:
        print(f"Error saving file: {e}")

def save_frequent_words(frequent_words, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for word, count in frequent_words:
                file.write(f"{word}: {count}\n")
        print(f"Frequent words saved to '{output_file}'")
    except IOError as e:
        print(f"Error saving file: {e}")


def main():
    # File path
    file_path = "Shakespeare.txt"
    cleaned_file = "Shakespeare_output.txt"  
    frequent_words_file = "frequent_words.txt"

    # Read File
    file = read_file(file_path)
    if not file:
        return
    # Clean text
    cleanText = [clean_text(line) for line in file]
    # Save Edited Shakespeare File
    save_cleaned_text(cleanText,cleaned_file)
    #Count Words
    countWords = count_words(cleanText)
    # Frequent words
    topWords = top_words(countWords)
    # Save Frequent Words File
    save_frequent_words(topWords, frequent_words_file)

    print("Top 20 Frequent Words:")
    for cleanText, count in topWords:
        print(f"{cleanText}: {count}")

if __name__ == "__main__":
    main()