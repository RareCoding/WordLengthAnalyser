import os
import time
import sys

def show_animation():
    animation = ["Calculating   ", "Calculating.  ", "Calculating.. ", "Calculating..."]
    for _ in range(2):
        for frame in animation:
            sys.stdout.write("\r" + frame)
            sys.stdout.flush()
            time.sleep(0.4)
    print("\rCalculation complete.      ")

def read_words(file_path):
    if not os.path.isfile(file_path):
        print("Error: The specified path does not point to a valid file.")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = [line.strip() for line in file if line.strip()]
            return sorted(words, key=len, reverse=True)
    except Exception as e:
        print(f"Error while reading the file: {e}")
        return []

def display_words(words):
    print("\nWords from longest to shortest:\n")
    for idx, word in enumerate(words, start=1):
        print(f"{idx}. {word} ({len(word)} characters)")

def query_word(words):
    try:
        pos = int(input("Enter the position number to query (e.g., 7): "))
        if pos < 1 or pos > len(words):
            print("Error: Position is out of range.")
        else:
            print(f"Word at position {pos}: {words[pos - 1]} ({len(words[pos - 1])} characters)")
    except ValueError:
        print("Error: Please enter a valid number.")

def main():
    file_path = input("Enter the full path to the text file: ").strip('"')
    show_animation()
    words = read_words(file_path)

    if not words:
        print("No valid words found in the file.")
        return

    while True:
        print("\nOptions:")
        print("1. Display all words from longest to shortest")
        print("2. Query a word by position")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            display_words(words)
        elif choice == '2':
            query_word(words)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
