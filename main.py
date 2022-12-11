#import re
from scanner import analiseTexto
from parser_ import testeRegras
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

print("Realizando a análise léxica..")
try:
  analiseTexto(texto)
except NameError as erro:
  print(erro)
  exit(1)

print("Realizando a análise sintática..\n")
try:
  testeRegras(texto)
except SyntaxError as erro:
  print(erro.args[0])
  exit(2)

print("""
SAÍDA DO PROGRAMA:
""")
try:
  gerarCodigoC(texto)
  executarCodigoC()
except OSError as erro:
  print(erro.args[0])
