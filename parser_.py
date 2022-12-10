import re
regras = {  
    "atribuicao": r"^\w+\s?=\s?(\w+|\d+);\Z",
    "for": r"^for\s?[(]\s?((int|float|double)\s)?\w+\s?=\s?\d+\s?[;]\s\w+\s?(<|>|>=|<=)\s?\d+[;]\s?\w+([+]{2}|--|-=\d|[+]=\d)\s?[)]\s?[{]$\s+?.+$\s+?[}]\Z"
}

txt = "for (float var = 100; var >= 10; var++){ a = 2; }"
txt2 = "a = 20;"
txt3 = """for (int var = 100; var >= 10; var--) {
    a = 2; 
    }"""
txt4 = """for (int var = 100; var >= 10; var--){\n}"""

def testeRegras(texto: str) -> re.Match:
    """ O objetivo desta função é testar se a instrução/linha diz 
    respeito a algumas das regras pre-definidas. """
    for k, r in regras.items():
        resultado = re.search(r, texto, flags=re.MULTILINE)
        if resultado:
            return resultado, k
    raise SyntaxError("Sintaxe incorreta encontrada em:\n" + texto)


print(testeRegras(txt3))

# txt = "4 > 5;"
# x = re.search("\d\s[>|<]\s\d;", txt)
# print(x)
