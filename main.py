from scanner import analisadorLexico

print(analisadorLexico("var1"))
print(analisadorLexico("1.5"))
print(analisadorLexico("se"))
print(analisadorLexico("="))

try:
    print(analisadorLexico("&Var"))
except NameError:
    print("Nome inválido")

try:
    print(analisadorLexico("1var"))
except NameError:
    print("Nome inválido")