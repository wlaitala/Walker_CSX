import re

text = "There are 10 kinds of people in the world:  those who know binary and those who don't!  Thus learn binary."
message = "1.12.4 2.1.2 2.2.3 1.18.1 3.1.4 1.2.1 1.9.3 1.10.5 1.20.1 1.13.6 1.16.3 2.1.3"



def decodeMessage(text, message):

    text = text.replace("-", ' ')
    text = text.replace("(", ' ')
    text = text.replace(")", ' ')
    text = text.replace(",", ' ')
    text = text.replace("/", ' ')
    text = text.replace("'", ' ')
    text = text.replace('"', ' ')
    text = text.replace("#", ' ')
    text = text.replace("$", ' ')
    text = text.replace("%", ' ')
    text = text.replace("&", ' ')
    text = text.replace("*", ' ')
    text = text.replace("+", ' ')
    text = text.replace(":", ' ')
    text = text.replace(";", ' ')
    text = text.replace("<", ' ')
    text = text.replace("=", ' ')
    text = text.replace(">", ' ')
    text = text.replace("@", ' ')
    text = text.replace("[", ' ')
    text = text.replace('\\', ' ')
    text = text.replace("]", ' ')
    text = text.replace("^", ' ')
    text = text.replace("_", ' ')
    text = text.replace("`", ' ')
    text = text.replace("{", ' ')
    text = text.replace("}", ' ')
    text = text.replace("|", ' ')
    text = text.replace("~", ' ')

    text = text.replace("  ", " ")
    text = text.replace("  ", " ")
    text = text.replace("  ", " ")
    text = text.replace("  ", " ")

    example = []
    message = message.split(" ")
    text = re.split('! |\? |\. ', text)

    for i in range(len(min(message,text))):

        sentence = int((message[i].split(".")[0])) - 1
        word = int((message[i].split("."))[1]) - 1
        char = int((message[i].split("."))[2]) - 1

        if sentence + 1 > len(text):
            example.append(" ")
        elif word + 1 > len(text[sentence].split(" ")):
            example.append(" ")
        elif char + 1 > len(text[sentence].split(" ")[word]):
            example.append(" ")
        else:
            #blah = text[sentence].split(" ")[word]
            example.append(text[sentence].split(" ")[word][char])
    return(''.join(example))

print(decodeMessage(text, message))