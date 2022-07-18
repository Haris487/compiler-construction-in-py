from lib2to3.pgen2 import token
from config.syntax import syntax

class CheckCfg():
  def __init__(self,tokens) -> None:
    self.tokens = tokens
    self.lineNo = 1

  def parse(self):
    tokenSet = self.tokens[:]
    while(True):
      tokenSet = self.verifyStatement(tokenSet,syntax)
      if len(tokenSet) == 0:
        return True

  def verifyStatement(self,tokenSet,syntaxTree):
    if syntaxTree == True:
      return tokenSet
    if len(tokenSet) == 0:
      raise Exception("Unexpected End of file at line no %d "%(self.lineNo)) 
    if tokenSet[0] == '\n':
      self.lineNo+= 1
      return self.verifyStatement(tokenSet[1:],syntaxTree)
    for k in syntaxTree:
      if tokenSet[0] == k:
        return self.verifyStatement(tokenSet[1:],syntaxTree[k])
    raise Exception("Unexpected token '%s' at line no %d "%(tokenSet[0],self.lineNo))    