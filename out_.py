
def gerarCodigoC(texto: str):
    estrutura = """#include <stdio.h>
#include <stdlib.h>
int main()
{
    <>
    return 0;
}
""".replace("<>", texto)
    with open("teste.c", "w") as arquivo:
        arquivo.write(estrutura)
    return arquivo


t = """for(int var = 0; var < 10; var++){
        printf("%d ", var);
    }"""


def executarCodigoC(texto: str):
    gerarCodigoC(texto)
    with open("teste.exe", "w") as arquivo:
        arquivo.write("")
    import subprocess
    subprocess.call(["g++", "teste.c", "-o", "teste.exe"])
    subprocess.call("./teste.exe")
