# Interpretador Sintático
## Trabalho final da disciplina Linguagens e Paradigmas de Programação.

O programa a ser executado é o _main.py_ que espera receber como entrada algumas linhas de código em C.

## Scanner ou Analisador Léxico
Representa a etapa de analise léxica do código, em que todo o texto deverá ser transformado em um dos tokens possíveis (identificador, palavra reservada, número, operador, etc) que é passado ao analisador sintático. 
Neste trabalho o _scanner.py_ de modo simbólico faz a análise de todo o conteúdo de entrada e retorna um erro caso não seja possível encaixar a palavra ou símbolo em algum dos tokens aceitos.

## Parser ou Analisador Sintático
Representa a etapa de análise sintática, em que é gerada uma árvore de sintaxe abstrata, que é usada para validar as regras aceitas por uma linguagem. 
Neste trabalho, foi usada a biblioteca específica para expressões regulares do python para validar algumas das regras da sintaxe da linguagem C.

## Saída e execução do programa em C
As instruções passadas na entrada do programa são inseridas dentro da estrutura de um programa C simples:
~~~
#include <stdio.h>
#include <stdlib.h>
int main()
{
    <>
    return 0;
}
~~~
Desse modo, a entrada recebida substituirá a string "_<>_" e o programa em seguida será executado usando o módulo _subprocess_ do python:
~~~
import subprocess 
subprocess.call(["g++","teste.c", "-o", "teste.exe"])
subprocess.call("./teste.exe")
~~~

A saída em seguida, caso não seja encontrado algum erro léxico ou sintático, a saída é impressa no console.