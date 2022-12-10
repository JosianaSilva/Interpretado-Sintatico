palavras_reservadas = [
  "for", "int", "if", "else", "while", "int", "float", "double"
]
operadores = [
  "=", "+", "++", "--", "-", "*", ">", "<",">=", "<=", "/", ";", ":", "%", "$", "&", "@"
  ]

regras = [
    "for({type} {id} = {numero}; {id} {operador_comparacao} {numero}; {id} {operador_incremento}) { }",
    "if({id} {operador_comparacao} {id}) {  }",
    "if({id} {operador_comparacao} {numero}) {  }",
    "if({id} {operador_comparacao} {id}) {  } else if()*"
]

def analisadorLexico(palavra):
  if (palavra[0].isnumeric()):
    for charactere in list(palavra)[1:]:
      if (charactere.isnumeric() == False and charactere != "."):
        raise NameError("Nome da variável inválido: "+ palavra)
    return "Type: numero"

  if (palavra in palavras_reservadas):
    return "Type: palavra reservada"

  if (palavra in operadores):
    return "Type: operador"

  if (not palavra[0].isalpha()):
    raise NameError("Nome da variável inválido: "+ palavra)
  else:
    for charactere in list(palavra):
      if (charactere in operadores):
        raise NameError("Nome da variável inválido: "+ palavra)
    return ("Type: Identificador")


