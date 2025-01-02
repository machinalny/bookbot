
def count_characters_occuerrences(text):
    characters_occurrences = {}
    for character in text.lower():
        if character == ' ' or character == '\n':
            continue
        if not character.isalpha():
            continue
        if character in characters_occurrences:
            characters_occurrences[character] += 1
        else:
            characters_occurrences[character] = 1
    characters_occurrences = dict(sorted(characters_occurrences.items(), key=lambda item: item[1], reverse=True))
    return characters_occurrences

def count_words(text):
    return len(text.split())

def main():
    path = 'books/frankenstein.txt'
    with open(path) as f:
        whole_text = f.read()
        print(f"--- Begin report of {path} ---")
        print(f"{count_words(whole_text)} words found in the document\n")
        for character, occurrences in count_characters_occuerrences(whole_text).items():
            print(f"The '{character}' character was found {occurrences} times")
        print("--- End report ---")

if __name__ == '__main__':
    main()