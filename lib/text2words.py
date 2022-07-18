from cgitb import text
from distutils.command.config import config
from tokenize import String
from typing import List
from config.wordbreakers import wordbreakers
import re


class Text2Words:
  def __init__(self, text) -> None:
      self.text = text
      self.text_len = len(text)
      self.words = []
      self.word = ""
      self.isStr = False
      self.isChar = False
  
  def parse(self) -> List:
    for i in range(self.text_len):
      cur = self.text[i]
      prev = self.text[i-1] if i > 0 else None

      ## For string literal
      if not self.isStr and cur == "\"" :
        self.isStr = True
        self.word += cur
        continue
      elif self.isStr and prev != "\\" and cur == "\"":
        self.isStr = False
        self.word += cur
        self.save_word()
        continue
      elif self.isStr:
        self.word += cur
        continue


      ## For char literal
      if not self.isChar and cur == "\'" :
        self.isChar = True
        self.word += cur
        continue
      elif self.isChar and prev != "\\" and cur == "\'":
        self.isChar = False
        self.word += cur
        self.save_word()
        continue
      elif self.isChar:
        self.word += cur
        continue


      if cur in wordbreakers:
        self.save_word()
        self.word += cur
        self.save_word()
        continue

      if cur == "." and re.match(r"[A-Za-z]", str(prev)):
        self.save_word()
        self.word += cur
        self.save_word()
        continue

      self.word += cur
    self.save_word()

  def save_word(self) -> None:
    if len(self.word) > 0:
      self.words.append(self.word)
      self.word = ""
      



