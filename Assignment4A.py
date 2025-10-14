def format_word(word):
    word = word.title()
    return word

def convert_to_pascal_case(pascal):
    pascal = str(pascal)
    pascal = pascal.replace(" ","")
    return pascal


word = input("Enter a string: ")
pascal = str(format_word(word))
print(f"Pascal Case: {(convert_to_pascal_case(pascal))}")


