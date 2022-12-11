import re

regras = {
    "atribuicao::":
    r"^(\s*?(int|float|double)\s*?\w+|\s*?\w+)\s?=\s?(\w+|\d+);\s*?\Z",
    "if::":
    r"^(if|\s*?if)\s*?[(]\s?.*\s*?[)]\s?[{]\s*?$\s*?.*\s*?$\s*?[}]\Z",
    "printf::":
    r"^(printf|\s*?printf)[(]\s*?[\"]\s*?((%d|%f|%i|%s|%c|%e|%E)+\s*?\w*?\d*?[\"]\s*?,\s*?.+|\s*?\w*?\s*?[\"]|\s*?\d*\s*?[\"]|\s*?[a-zA-z_1-9]*?\s*?[\"])\s*?[)](;|;$)\Z",
    "prinf2::":
    r"^(printf|\s*?printf)[(]\s*?[\"]\s*?.*?\s*?[\"]\s*?[)](;|;$)",
    "for::":
    r"^(for|\s*?for)\s?[(]\s?((int|float|double)\s)?\w+\s?=\s?\d+\s?[;]\s\w+\s?(<|>|>=|<=)\s?\d+[;]\s?\w+([+]{2}|--|-=\d|[+]=\d)\s?[)]\s?[{]\s*?$\s*?.*?$\s*?([}]|[}]\s*?)\Z"
}


def testeRegras(texto: str) -> re.Match:
    """ O objetivo desta função é testar se a instrução/linha diz 
      respeito a algumas das regras pre-definidas. """
    if (re.search(".*?(for|if).*?", texto) and len(texto) > 3):
        instrucoes, texto = removeInstrucoes(texto)
    else:
        instrucoes = ""

    for k, r in regras.items():
        resultado = re.search(r, texto, flags=re.MULTILINE)
        if resultado:
            if instrucoes:
                testeRegras(instrucoes)
            return resultado, k
    raise SyntaxError("Sintaxe incorreta encontrada em: " + "\n" + texto)


def removeInstrucoes(texto: str) -> str:
    """ O objetivo dessa função é separar as instruções que se encontram entre { }
    para que possam ser analisadas de forma independente da parte mais exterior do 
    bloco a que pertence. """
    strInstrucoes = ""
    if(re.search(".*?(for|if).*?", texto)):
        instrucoes = texto.split("\n")
        n = len(instrucoes)
        instrucoes = instrucoes[1:n - 1]
        n = len(instrucoes) - 1

        for i, inst in enumerate(instrucoes):
            if inst:
                if (i < n):
                    strInstrucoes += str(inst) + "\n"
                elif (i == n):
                    strInstrucoes += str(inst).replace("\n", "")

    texto = texto.replace(strInstrucoes, "")
    return strInstrucoes, texto
