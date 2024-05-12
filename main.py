import argparse

def readfile(file):
    # print("Reading file:", file)
    file_content = open(file, "r")
    return file_content

def countBytes(file_content):
    #return print("Quantidade de bytes: ", len(file_content.read().encode('utf-8')))
    return print(len(file_content.read().encode('utf-8')))

def countLines(file_content):
    lines = file_content.read().split('\n')

    count = 0
    for line in lines:
        count = count + 1
        # print("Número de linhas: {} - {}".format(count, line))

    #print("Número de linhas: {}".format(count))
    return print(count)

def countWords(file_content):
    #return print("Quantidade de palavras", len(file_content.read().split())) 
    return print(len(file_content.read().split()))

def countCharacters(file_content):
    text = file_content.read() 
    count = 0
    for character in text:
        count = count + 1
        # print(character)
        
    #return print("Número de caracteres: ", count)
    return print(count)

def logger():
    charFunc = countCharacters
    print(charFunc)


def commandLine():
    parser = argparse.ArgumentParser(description="Copy wc command", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-c", "--bytes", action="store_true", help="Count the number of Bytes in a file")
    parser.add_argument("-l", "--lines", action="store_true", help="Count the number of Lines in a file")
    parser.add_argument("-w", "--words", action="store_true", help="Count the number of Words in a file")
    parser.add_argument("-m", "--chars", action="store_true", help="Count the number of Characters in a file")
    parser.add_argument("filepath", type=str, help="Path to the file to analyze")

    args = parser.parse_args()

    if args.filepath:
        countBytes(readfile(args.filepath))
        countLines(readfile(args.filepath))
        countWords(readfile(args.filepath))
        countCharacters(readfile(args.filepath))
    else:
        if args.bytes:
            countBytes(readfile(args.filepath))
        if args.lines:
            countLines(readfile(args.filepath))
        if args.words:
            countWords(readfile(args.filepath))
        if args.chars:
            countCharacters(readfile(args.filepath))


commandLine()

# # Step 1 - number of bytes
# countBytes(readfile("test.txt")) # TO-DO - O que é um byte, para que server
#
# # Step 2 - Number of lines
# countLines(readfile("test.txt"))
#
# # Step 3 - Number of words
# countWords(readfile("test.txt"))
#
# # Step 4 - Number of characters
# countCharacters(readfile("test.txt"))


# text ="a b c d e f g h i j"
#
# text = "Matheus Nogueira Tanaka é foda"
#
# print(len(text.split()))
#
# count = 0 
#
# for word in text:
#     if word == " ":
#         count = count + 1
#         print("numero de espaco: ",count)
#
# splited = text.split("\n")
#
# print(splited)
# for word in splited:
#     print("Letra: ",word)

# print(text)
