tokens = [
  {"keyword" : "DataType" , "regex" : r"var"},
  {"keyword" : "Identifier" , "regex" : r"[a-zA-Z\_]+[a-zA-Z\_\d]*"},
  {"keyword" : "CompairsionOperator" , r"regex" : "=="},
  {"keyword" : "AssignmentOperator" , r"regex" : "="},
  {"keyword" : "Value" , "regex" : r".?[\d]+"},
  {"keyword" : "Terminator" , "regex" : r";"},
  {"keyword" : "ArithmaticOperator" , "regex" : r"\+"},
  {"keyword" : "RoundBracketOpen" , "regex" : r"\("},
  {"keyword" : "RoundBracketClose" , "regex" : r"\)"},
]