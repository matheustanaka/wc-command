#!/usr/bin/python

import argparse

def readfile(file):
    # print("Reading file:", file)
    file_content = open(file, "r")
    return file_content

def countBytes(file_content):
    #return print("Quantidade de bytes: ", len(file_content.read().encode('utf-8')))
    return len(file_content.read().encode('utf-8'))

def countLines(file_content):
    lines = file_content.read().split('\n')

    count = 0
    for line in lines:
        count = count + 1
        # print("Número de linhas: {} - {}".format(count, line))

    #print("Número de linhas: {}".format(count))
    return count

def countWords(file_content):
    #return print("Quantidade de palavras", len(file_content.read().split())) 
    return len(file_content.read().split())

def countCharacters(file_content):
    text = file_content.read() 
    count = 0
    for character in text:
        count = count + 1
        # print(character)
        
    #return print("Número de caracteres: ", count)
    return count

def commandLine():

    parser = argparse.ArgumentParser(description="Copy wc command", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-c", "--bytes", action="store_true", help="Count the number of Bytes in a file")
    parser.add_argument("-l", "--lines", action="store_true", help="Count the number of Lines in a file")
    parser.add_argument("-w", "--words", action="store_true", help="Count the number of Words in a file")
    parser.add_argument("-m", "--chars", action="store_true", help="Count the number of Characters in a file")
    parser.add_argument("filepath", type=str, help="Path to the file to analyze")

    args = parser.parse_args()

    logs = []

    if args.bytes:
        logs.append(f"{countBytes(readfile(args.filepath))}")
    if args.lines:
        logs.append(f"{countLines(readfile(args.filepath))}")
    if args.words:
        logs.append(f"{countWords(readfile(args.filepath))}")
    if args.chars:
        logs.append(f"{countCharacters(readfile(args.filepath))}")
    if args.filepath and args.bytes == False and args.lines == False and args.words == False and args.chars == False:
        logs.append(f"{countBytes(readfile(args.filepath))}")
        logs.append(f"{countLines(readfile(args.filepath))}")
        logs.append(f"{countWords(readfile(args.filepath))}")
        logs.append(f"{countCharacters(readfile(args.filepath))}")
    
    if logs:
        print(' '.join(logs), args.filepath)
    else:
        print('fudeu')

commandLine()
