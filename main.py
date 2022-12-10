import re
from scanner import analisadorLexico, analiseTexto
from parser_ import testeRegras

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

print()

testeLexico1 = """int i = 0;
for(i = 0; i < 10; i++){
    printf("%d", i);
}"""
testeLexico2 = """for (int var = 100; var >= 10; var--) {
    a = 2;
    }"""

print(analiseTexto(testeLexico1))
print(analiseTexto(testeLexico2))

print()

txt = "for (float var = 100; var >= 10; var++){ a = 2; }"
txt2 = "double a = 20;"
txt3 = """for (int var = 100; var >= 10; var--) {
    a = ;
    }"""
txt4 = """for (int var = 100; var >= 10; var--){\n}""" 
# este txt4 é pra gerar um Erro, pois não tem instruções entre { e }
txt5 = """if (a == b) {
    printf("%s",a);
    }"""
txt6 = """printf("%d", num);"""

try:
    print(testeRegras(txt3))
except SyntaxError as error:
    print("SyntaxError")
    print(error.args[0])