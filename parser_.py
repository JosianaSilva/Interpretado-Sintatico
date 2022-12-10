import re
regras = {  
    "atribuicao::": r"^((int|float|double)\s?\w+|\w+)\s?=\s?(\w+|\d+);\Z",
    "if::" : r"^if\s*?[(]\s?.*\s*?[)]\s?[{]\s*?$\s*?.+\s*?$\s*?[}]\Z",
    "printf::" : r"^printf[(]\s*?[\"](%d|%f|%i|%s|%c|%e|%E)+[\"]\s*?,\s*?.+\s*?[)];\Z",
    "for::": r"^for\s?[(]\s?((int|float|double)\s)?\w+\s?=\s?\d+\s?[;]\s\w+\s?(<|>|>=|<=)\s?\d+[;]\s?\w+([+]{2}|--|-=\d|[+]=\d)\s?[)]\s?[{]\s*?$\s*?.+$\s*?[}]\Z"
}


def testeRegras(texto: str) -> re.Match:
    """ O objetivo desta função é testar se a instrução/linha diz 
    respeito a algumas das regras pre-definidas. """
    for k, r in regras.items():
        resultado = re.search(r, texto, flags=re.MULTILINE)
        if resultado:
            return resultado, k
    raise SyntaxError("Sintaxe incorreta encontrada em: " + "\n" + texto)
