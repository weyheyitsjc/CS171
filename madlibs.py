def is_question(word):
    if word[0] == "[":
        return True
    else:
        return False
def get_punc(word):
    pos = word.find("]")
    punc = word[pos + 1: ]
    return punc
def get_question_text(word):
    pos1 = word.find("[")
    pos2 = word.find("]")
    text = word[pos1 + 1: pos2]
    text = text.replace("-", " ")
    if text[0] in "aeiou":
        text = "an " + text
    else:
        text = "a " + text
    text = "Please give " + text + "\n"
    return text
def ask_questions(words):
    counter = 0
    while counter < len(words):
        if is_question(words[counter]):
            q = get_question_text(words[counter])
            answer = input(q) + get_punc(words[counter])
            words[counter] = answer
        counter += 1
    return
def make_text(words):
    story = ""
    counter = 0
    while counter < len(words):
        story += words[counter]
        if counter + 1 < len(words):
            story += " "
        counter += 1
    return story

filename = "example1.txt"
file = open(filename, "r")
for line in file:
    words = line.split()
    words = ask_questions(words)
print(make_text(words))