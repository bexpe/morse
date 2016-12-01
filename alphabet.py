import csv
ascii_letters = 'abcdefghijklmnopqrstuvwxyz'
index = 0
long_len = 1
myfile = "FirstRiddleOK.txt"

def replace_letter():
    while ascii_letters[index]:
        print(ascii_letters[index])
        print(ascii_letters[len(ascii_letters) - long_len])
        index += 1
        long_len += 1
        if long_len == 14:
            break


def reading_file(myfile):
    # index = 0
    # long_len = 1
    text = []
    with open(myfile, 'r') as f:
        text = f.read()
    print(text)
    for character in text:
        character_index = ascii_letters.index(character)
        character = ascii_letters[len(ascii_letters) - long_len]
        ''.join(character))
        # index += 1
        # long_len += 1
        # #print(ascii_letters[index])
        # #print(ascii_letters[len(ascii_letters) - long_len])
        # if long_len == 14:
        #     break
        if character == " ":
            print(" ")
        if character == "\n":
            print("\n")

# def main():
#
# reading_file("FirstRiddleOK.txt")
reading_file(myfile)
    # for item in line:
    #     if item == "a":
    #         print('% s', b)
    #     if item == "l":
    #         print('% s', d)
