from config.tokens import tokens as tokens_list
import re
class Words2Tokens():
  def __init__(self,words) -> None:
    self.words = words
    self.words_len = len(words)
    self.tokens = []
    self.lineno = 0

  def parse(self):
    for i in range(self.words_len):
      #last = self.words[i-1] if i > 0 else None
      cur = self.words[i]
      #next = self.words[i+1] if i < self.words_len else None
      if cur in [" "," "]:
        continue

      if cur in ["\n"]:
        self.lineno += 1
        self.tokens.append(cur)
        continue

      keyword = None
      for token in tokens_list:
        if re.match(token["regex"], cur):
          keyword = token["keyword"]
          break
      
      self.tokens.append(keyword)

      if keyword is None:
        print("ERROR unidentified token %s at line no %d"%(cur,self.lineno))
      

      