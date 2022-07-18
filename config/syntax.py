########## ARITHEMATIC OPERATIONS
stringArithematicOperation = {
  "stringLiteral" : {
    "arithmeticOperator" : {
    },
    "semicolon" : True
  }
}

stringArithematicOperation["stringLiteral"]["arithmeticOperator"] = stringArithematicOperation


syntax = {
  ########## VARIABLE DECLARATION AND INITIALIZATION
  ##### FOR STRING
  "string" : {
    "identifier" : {
      "assignmentOperator" : stringArithematicOperation,
      "semicolon" : True
    }
  },
  ##### FOR FLOAT
  "float" : {
    "identifier" : {
      "assignmentOperator" : {
        "floatLiteral" : {
          "semicolon" : True
        }
      },
      "semicolon" : True
    }
  },

  ##### FOR CHAR
  "char" : {
    "identifier" : {
      "assignmentOperator" : {
        "charLiteral" : {
          "semicolon" : True
        }
      },
      "semicolon" : True
    }
  },

  ##### FOR INT
  "int" : {
    "identifier" : {
      "assignmentOperator" : {
        "intLiteral" : {
          "semicolon" : True
        }
      },
      "semicolon" : True
    }
  },

  ##### FOR BOOLEAN
  "bool" : {
    "identifier" : {
      "assignmentOperator" : {
        "booleanLiteral" : {
          "semicolon" : True
        }
      }
    }
  },

  ########## VARIABLE INITIALIZATION
  "identifier" : {
    "assignmentOperator" : {
      "stringLiteral" : {
        "semicolon" : True
      },
      "floatLiteral" : {
        "semicolon" : True
      },
      "charLiteral" : {
        "semicolon" : True
      },
      "intLiteral" : {
        "semicolon" : True
      },
      "booleanLiteral" : {
          "semicolon" : True
      }
    }
  },

  ########## LOOP
  "while" : {
    "paranthesesOpen" : {
      "identifier" : {
        "compareOperator" : {
          "identifier" : {
            "paranthesesClose" : {
              "braceOpen" : True
            }
          }
        }
      }
    }
  },
  "braceClose" : True
}