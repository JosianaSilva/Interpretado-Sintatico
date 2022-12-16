#import re
from scanner import analisaTexto
from parser_ import identificaRegra
from out_ import gerarCodigoC, executarCodigoC

linhasEntrada = []

print("""DIGITE A ENTRADA:
Pressione Ctrl + Z para sair
""")
while(True):
    try:
        linha = input("> ")
    except EOFError:
        break
    linhasEntrada.append(linha)
texto = "\n".join(linhasEntrada)

try:
    print("Realizando a análise léxica..")
    analisaTexto(texto)
    print("Realizando a análise sintática..\n")
    identificaRegra(texto)

    print("""
SAÍDA DO PROGRAMA:
""")
    executarCodigoC(texto)
except NameError as erro:
    print("\nErro léxico:\n"+ erro.args[0])
    exit(1)
except SyntaxError as erro:
    print("\nErro sintático:\n" + erro.args[0])
    exit(2)   
except OSError as erro:
    print(erro.args[0])
