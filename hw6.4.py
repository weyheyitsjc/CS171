import sys
print("Welcome to fun a word replacement game.")
filename = input("Enter the name of the file to use:\n")
try:
    f = open(filename, "r")
    text = f.read()
except:
    print("Error Bad File Name")
    sys.exit()

def story():
    story = []
    for word in text.split():
        if word == "[name]":
            story.append(input("Please give a name\n"))
        elif word == "[place]":
            story.append(input("Please give a place\n"))
        elif word == "[place],":
            story.append(input("Please give a place\n") + ",")
        elif word == "[day-of-the-week].":
            story.append(input("Please give a day of the week\n") + ".")
        elif word == "[time],":
            story.append(input("Please give a time\n") + ",")
        elif word == "[verb]":
            story.append(input("Please give a verb\n"))
        elif word == "[animal]":
            story.append(input("Please give an animal\n"))
        elif word == "[body-part].":
            story.append(input("Please give a body part\n") + ".")
        elif word == "[noun]":
            story.append(input("Please give a noun\n"))
        elif word == "[noun],":
            story.append(input("Please give a noun\n") + ",")
        elif word == "[noun].":
            story.append(input("Please give a noun\n") + ".")
        elif word == "[adjective]":
            story.append(input("Please give an adjective\n"))
        elif word == "[adjective],":
            story.append(input("Please give an adjective\n") + ",")
        elif word == "[adjective].":
            story.append(input("Please give an adjective\n") + ".")
        elif word == "[plural-noun]":
            story.append(input("Please give a plural noun\n"))
        elif word == "[plural-noun].":
            story.append(input("Please give a plural noun\n") + ".")
        elif word == "[game]":
            story.append(input("Please give a game\n"))
        elif word == "[verb-ending-in-ing]":
            story.append(input("Please give a verb ending in ing\n"))
        elif word == "[verb-ending-in-ing].":
            story.append(input("Please give a verb ending in ing\n") + ".")
        elif word == "[plant]":
            story.append(input("Please give a plant\n"))
        elif word == "[part-of-the-body].":
            story.append(input("Please give a part of the body\n") + ".")
        elif word == "[number]":
            story.append(input("Please give a number\n"))
        else:
            story.append(word)
    print("Here is your story:")
    print("--------------------")
    return " ".join(story)

print(story())
  
f.close()