# import sys
#
# n = int(sys.argv[1])
# m = int(sys.argv[2])
#
# print(n+m)  

import argparse

parser = argparse.ArgumentParser(description="Copy wc command", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("-c", "--bytes", action="store_true", help="Count the number of Bytes in a file")
parser.add_argument("-l", "--lines", action="store_true", help="Count the number of Lines in a file")
parser.add_argument("-w", "--words", action="store_true", help="Count the number of Words in a file")
parser.add_argument("-m", "--chars", action="store_true", help="Count the number of Characters in a file")
parser.add_argument("filepath", type=str, help="Path to the file to analyze")
args = parser.parse_args()

if args.c:
    print("É pra calcular a quantidade de bytes")
elif args.l: 
    print("É pra calcular a quantidade de linhas")
else:
    print("No arguments")
