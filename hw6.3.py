import sys
print("Welcome to Book Analyzer v0.1")
fileName = input("Enter File Name to Read:\n")
try:
    f = open(fileName, "r")
    text = f.read()
except:
    print("Error: Could Not Open File.")
    sys.exit()

letter = input("Letter to search for:\n")

if len(letter) == 1:
    letter = letter
else:
    print("Error: A single letter is required.")
    sys.exit()
    
position = input("Enter Position (0 for first letter):\n")

while True:
    try:
        position = int(position)
        break
    except:
        print("Error: A number is required.")
        sys.exit()
    
def word_search(letter, position):
    words = 0
    text.replace(",", " ")
    text.replace(".", " ")
    for word in text.split():
        if len(word) >= position:
            if word[position] == (letter.lower() or letter.upper()):
                words += 1
        else:
            continue
    return words

print("There are", word_search(letter, position), "words with", letter, "in position", position)

text.close()


    