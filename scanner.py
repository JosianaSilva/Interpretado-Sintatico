palavras_reservadas = [
  "for", "int", "if", "else", "while", "int", "float", "double", "printf"
]
operadores = [
  "=", "+", "++", "--", "-", "*", ">", "<",">=", "<=", "/", "%", "$", "&"
  ]

simbolos = [
   ";", ":", ",", "@", "(", ")", "\"", "{", "}"
]

sequenciasDeEscape = [ 
  "%d", "%f", "%s", "%c", "%e", "%E", "%i"
]


__separadorCaracteres = lambda texto_: texto_.replace("(", " ( ").replace(")", " ) ").replace(";", " ; ").replace("++", " ++ ").replace("--", " -- ").replace("\"", " \" ").replace(r"[\n]", "#")

__separadorLinhas = lambda texto_: texto_.split("\n")

def analisadorLexico(palavra: str) -> str:
  if palavra:
    if (palavra[0].isnumeric()):
      for charactere in list(palavra)[1:]:
        if (charactere.isnumeric() == False and charactere != "."):
          raise NameError("Nome da variável inválido: "+ palavra)
      return "Type: numero"

    if (palavra in palavras_reservadas):
      return "Type: palavra reservada"
    
    if (palavra in sequenciasDeEscape):
      return "Type: sequência de escape"

    if (palavra in operadores):
      return "Type: operador"

    if (palavra in simbolos):
      return "Type: simbolos"

    if (not palavra[0].isalpha()):
      raise NameError("Nome da variável inválido: "+ palavra)
    else:
      for charactere in list(palavra):
        if (charactere in operadores):
          raise NameError("Nome da variável inválido: "+ palavra)
      return ("Type: Identificador")

def analiseTexto(texto_):
    texto_ = __separadorCaracteres(texto_)
    texto_ = __separadorLinhas(texto_)

    resultado = ""    
    for linha in texto_:
        for elemento in linha.split():
            try:
                resultado = analisadorLexico(elemento)
            except NameError:    
                return "NameError\tErro léxico encontrado em: " + elemento
        return "A sentença está lexicamente correta"
