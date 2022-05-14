from unicodedata import name

import sys
from lib.fileio import read_file, write_file
from lib.text2words import Text2Words
from lib.words2tokens import Words2Tokens

def main():
  if len(sys.argv) != 2:
    print("ERROR invalid command")
    print("correct command is")
    print("python "+__file__.split("/")[-1]+" <filename>")
    exit()
  filename = sys.argv[1]
  print("start compiling file "+filename)

  ## Reading text from source file
  text = read_file(filename)
  print("\n/// Source File Code")
  print(text+"\n")

  ## converting text to words
  text2Words = Text2Words(text)
  text2Words.parse()
  print(text2Words.words)

  ## converting words to tokens
  words2Tokens = Words2Tokens(text2Words.words)
  words2Tokens.parse()
  print(words2Tokens.tokens)
  lexical_text = " ".join(words2Tokens.tokens)
  write_file(filename+".lexical"," "+lexical_text)


if __name__ == "__main__":
  main()