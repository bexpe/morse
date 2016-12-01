alphabet = {
       "A" : "-+",
       "B" : "+---",
       "C" : "+-+-",
       "D" : "+--",
       "E" : "-",
       "F" : "--+-",
       "G" : "++-",
       "H" : "----",
       "I" : "--",
       "J" : "-+++",
       "K" : "+-+",
       "L" : "-+--",
       "M" : "++",
       "N" : "+-",
       "O" : "+++",
       "P" : "-++-",
       "Q" : "++-+",
       "R" : "-+-",
       "S" : "---",
       "T" : "+",
       "U" : "--+",
       "V" : "---+",
       "W" : "-++",
       "X" : "+--+",
       "Y" : "+-++",
       "Z" : "++--",
       " " : "/"
       }
file = "house_of_code.txt"
inverseMorseAlphabet = []
inverseMorseAlphabet = dict((v, k) for (k, v) in alphabet.items())
# print(inverseMorseAlphabet)
f = open(file, "r")
cos_tam = open(file).read().split()
char = ''
# char = set(v['chr'] for v in alphabet.values())
#print(char)
decrypted = []
for line in cos_tam:
    if line in inverseMorseAlphabet:
        decrypted.append(inverseMorseAlphabet[line])
decrypted_words = "".join(decrypted)
replaced = decrypted_words.replace("QUESTION MARK", "?")
replaced = replaced.replace("DOT", ".")
replaced = replaced.replace("COMMA", ",")
print(replaced)
