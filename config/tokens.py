tokens = [
  ## KEYWORDS
  {"keyword" : "abstract" , "regex" : r"^abstract$"},
  {"keyword" : "base" , "regex" : r"^base$"},
  {"keyword" : "break" , "regex" : r"^break$"},
  {"keyword" : "case" , "regex" : r"^case$"},
  {"keyword" : "char" , "regex" : r"^char$"},
  {"keyword" : "class" , "regex" : r"^class$"},
  {"keyword" : "continue" , "regex" : r"^continue$"},
  {"keyword" : "default" , "regex" : r"^default$"},
  {"keyword" : "do" , "regex" : r"^do$"},
  {"keyword" : "else" , "regex" : r"^else$"},
  {"keyword" : "event" , "regex" : r"^event$"},
  {"keyword" : "extern" , "regex" : r"^extern$"},
  {"keyword" : "finally" , "regex" : r"^finally$"},
  {"keyword" : "float" , "regex" : r"^float$"},
  {"keyword" : "foreach" , "regex" : r"^foreach$"},
  {"keyword" : "goto" , "regex" : r"^goto$"},
  {"keyword" : "implicit" , "regex" : r"^implicit$"},
  {"keyword" : "int" , "regex" : r"^int$"},
  {"keyword" : "internal" , "regex" : r"^internal$"},
  {"keyword" : "lock" , "regex" : r"^lock$"},
  {"keyword" : "Namespace" , "regex" : r"^Namespace$"},
  {"keyword" : "null" , "regex" : r"^null$"},
  {"keyword" : "operator" , "regex" : r"^operator$"},
  {"keyword" : "override" , "regex" : r"^override$"},
  {"keyword" : "private" , "regex" : r"^private$"},
  {"keyword" : "public" , "regex" : r"^public$"},
  {"keyword" : "uncheched" , "regex" : r"^uncheched$"},
  {"keyword" : "uncheched" , "regex" : r"^uncheched$"},
  {"keyword" : "sbyte" , "regex" : r"^sbyte$"},
  {"keyword" : "set" , "regex" : r"^set$"},
  {"keyword" : "sizeof" , "regex" : r"^sizeof$"},
  {"keyword" : "strict" , "regex" : r"^strict$"},
  {"keyword" : "struct" , "regex" : r"^struct$"},
  {"keyword" : "this" , "regex" : r"^this$"},
  {"keyword" : "typeof" , "regex" : r"^typeof$"},
  {"keyword" : "ulong" , "regex" : r"^ulong$"},
  {"keyword" : "unsafe" , "regex" : r"^unsafe$"},
  {"keyword" : "using" , "regex" : r"^using$"},
  {"keyword" : "virtual" , "regex" : r"^virtual$"},
  {"keyword" : "as" , "regex" : r"^as$"},
  {"keyword" : "bool" , "regex" : r"^bool$"},
  {"keyword" : "byte" , "regex" : r"^byte$"},
  {"keyword" : "catch" , "regex" : r"^catch$"},
  {"keyword" : "checked" , "regex" : r"^checked$"},
  {"keyword" : "const" , "regex" : r"^const$"},
  {"keyword" : "decimal" , "regex" : r"^decimal$"},
  {"keyword" : "delegate" , "regex" : r"^delegate$"},
  {"keyword" : "double" , "regex" : r"^double$"},
  {"keyword" : "enum" , "regex" : r"^enum$"},
  {"keyword" : "explicit" , "regex" : r"^explicit$"},
  {"keyword" : "fixed" , "regex" : r"^fixed$"},
  {"keyword" : "for" , "regex" : r"^for$"},
  {"keyword" : "get" , "regex" : r"^get$"},
  {"keyword" : "if" , "regex" : r"^if$"},
  {"keyword" : "in" , "regex" : r"^in$"},
  {"keyword" : "interface" , "regex" : r"^interface$"},
  {"keyword" : "is" , "regex" : r"^is$"},
  {"keyword" : "long" , "regex" : r"^long$"},
  {"keyword" : "new" , "regex" : r"^new$"},
  {"keyword" : "object" , "regex" : r"^object$"},
  {"keyword" : "out" , "regex" : r"^out$"},
  {"keyword" : "params" , "regex" : r"^params$"},
  {"keyword" : "protected" , "regex" : r"^protected$"},
  {"keyword" : "readonly" , "regex" : r"^readonly$"},
  {"keyword" : "return" , "regex" : r"^return$"},
  {"keyword" : "sealed" , "regex" : r"^sealed$"},
  {"keyword" : "short" , "regex" : r"^short$"},
  {"keyword" : "stackaloc" , "regex" : r"^stackaloc$"},
  {"keyword" : "string" , "regex" : r"^string$"},
  {"keyword" : "string" , "regex" : r"^str$"},
  {"keyword" : "switch" , "regex" : r"^switch$"},
  {"keyword" : "throw" , "regex" : r"^throw$"},
  {"keyword" : "try" , "regex" : r"^try$"},
  {"keyword" : "unit" , "regex" : r"^unit$"},
  {"keyword" : "ref" , "regex" : r"^ref$"},
  {"keyword" : "ushort" , "regex" : r"^ushort$"},
  {"keyword" : "value" , "regex" : r"^value$"},
  {"keyword" : "volatile" , "regex" : r"^volatile$"},
  {"keyword" : "while" , "regex" : r"^while$"},

  ## Literals
  {"keyword" : "intLiteral" , "regex" : r"^\d+$"},
  {"keyword" : "booleanLiteral" , "regex" : r"^(true)|(false)$"},
  {"keyword" : "floatLiteral" , "regex" : r"^[+-]?(\d*[.])?\d+$"},
  {"keyword" : "charLiteral" , "regex" : r"^\'\\?.\'$"},
  {"keyword" : "stringLiteral" , "regex" : r'^"([^"])*"$'},
  ## Operators


  {"keyword" : "arithmeticOperator" , "regex" : r"^\+$"},
  {"keyword" : "arithmeticOperator" , "regex" : r"^-$"},
  {"keyword" : "arithmeticOperator" , "regex" : r"^\*$"},
  {"keyword" : "arithmeticOperator" , "regex" : r"^/$"},
  {"keyword" : "arithmeticOperator" , "regex" : r"^%$"},
  {"keyword" : "logicalOperator" , "regex" : r"^\\|\\|$"},
  {"keyword" : "logicalOperator" , "regex" : r"^&&$"},
  {"keyword" : "logicalOperator" , "regex" : r"^!$"},
  {"keyword" : "logicalOperator" , "regex" : r"^\\|$"},
  {"keyword" : "logicalOperator" , "regex" : r"^&$"},
  {"keyword" : "logicalNotOperator" , "regex" : r"^!$"},
  {"keyword" : "assignmentOperator" , "regex" : r"^=$"},

  {"keyword" : "compareOperator" , "regex" : r"^>=$"},
  {"keyword" : "compareOperator" , "regex" : r"^<=$"},
  {"keyword" : "compareOperator" , "regex" : r"^==$"},
  {"keyword" : "compareOperator" , "regex" : r"^>$"},
  {"keyword" : "compareOperator" , "regex" : r"^<$"},




  ## Puntuations
  {"keyword" : "semicolon" , "regex" : r"^;$"},
  {"keyword" : "colon" , "regex" : r"^:$"},
  {"keyword" : "comma" , "regex" : r"^,$"},
  {"keyword" : "dot" , "regex" : r"^\.$"},
  {"keyword" : "paranthesesOpen" , "regex" : r"^\($"},
  {"keyword" : "paranthesesClose" , "regex" : r"^\)$"},
  {"keyword" : "bracketOpen" , "regex" : r"^\[$"},
  {"keyword" : "bracketClose" , "regex" : r"^\]$"},
  {"keyword" : "braceOpen" , "regex" : r"^{$"},
  {"keyword" : "braceClose" , "regex" : r"^}$"},

  ## Identifier
  {"keyword" : "identifier" , "regex" : r"^[A-Za-z_][A-Za-z_\d]*$"},


]
