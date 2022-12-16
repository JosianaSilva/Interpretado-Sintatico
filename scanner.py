palavras_reservadas = [
    "for", "int", "if", "else", "while", "int", "float", "double", "printf"
]
operadores = [
    "=", "+", "++", "--", "-", "*", ">", "<", ">=", "<=", "/", "%", "$", "&"
]

simbolos = [
    ";", ":", ",", "@", "(", ")", "\"", "{", "}"
]

sequenciasDeEscape = [
    "%d", "%f", "%s", "%c", "%e", "%E", "%i", "%u"
]


def __separadorCaracteres(texto_): return texto_.replace("(", " ( ").replace(")", " ) ").replace(
    ";", " ; ").replace("++", " ++ ").replace("--", " -- ").replace("\"", " \" ").replace("=", " = ")


def __separadorLinhas(texto_): return texto_.split("\n")


def getToken(palavra: str) -> str:
    if palavra:
        if (palavra[0].isnumeric()):
            for charactere in list(palavra):
                if (charactere.isnumeric() == False and charactere != "."):
                    raise NameError("Nome da variável inválido: " + palavra)
            return "numero"

        if (palavra in palavras_reservadas):
            return "palavra reservada"

        if (palavra in sequenciasDeEscape):
            return "sequência de escape"

        if (palavra in operadores):
            return "operador"

        if (palavra in simbolos):
            return "simbolo"

        if (palavra[0].isalpha() or palavra[0] == "*"):
            for charactere in list(palavra)[1:]:
                if (charactere in operadores or charactere in simbolos):
                    raise NameError("Nome da variável inválido: " + palavra)
            return ("identificador")
        else:
            raise NameError("Nome da variável inválido: " + palavra)


def analisaTexto(texto_: str) -> str:
    texto_ = __separadorCaracteres(texto_)
    texto_ = __separadorLinhas(texto_)

    resultado = ""
    for linha in texto_:
        for elemento in linha.split():
            try:
                resultado = getToken(elemento)
                print(elemento + " " + resultado)
            except NameError as erro:
                raise erro
        return "A sentença está lexicamente correta"