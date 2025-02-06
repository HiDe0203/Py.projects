def wfc():
    paragraph = input("Enter a paragraph:").lower()

    import string
    for char in string.punctuation:
        paragraph = paragraph.replace(char, "")
    words = paragraph.split()

    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    print("\nWord Frequency:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

wfc()