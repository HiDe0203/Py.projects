def wfc():
    paragraph = input("Enter a paragraph:").lower()

    import string
    for char in string.punctuation:
        paragraph = paragraph.replace(char, "")
        print(paragraph)

wfc()