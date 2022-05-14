from cgitb import text
from distutils.command.config import config
from tokenize import String
from typing import List
from config.wordbreakers import wordbreakers


class Text2Words:
  def __init__(self, text) -> None:
      self.text = text
      self.text_len = len(text)
      self.words = []
      self.word = ""
  
  def parse(self) -> List:
    for i in range(self.text_len):
      cur = self.text[i]

      if cur in wordbreakers:
        self.save_word()
        self.word += cur
        self.save_word()
        continue

      self.word += cur

  def save_word(self) -> None:
    if len(self.word) > 0:
      self.words.append(self.word)
      self.word = ""
      



