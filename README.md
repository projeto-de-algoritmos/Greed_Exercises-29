# Integrantes
| Nome |  Matrícula
| :------: | :-------:
| [Fernando Vargas](https://github.com/SFernandoS) | 180016491
| [Matheus Perillo](https://github.com/MatheusPerillo) | 190093421

# Introdução 
Este repositório foi criado para o desenvolvimento do segundo módulo de Greedy da disciplina Projeto de Algoritmos do Professor Maurício Serrano. Ele aborda os algoritmos como o do Huffman e Interval Partitioning.
Portanto fizemos a resolução de alguns exercícios em Judges.

# Apresentação

[Link para a apresentação da dupla 29]() 

# Foram feitos os exercícios no LeetCode

## [535. Encode and Decode TinyURL](https://leetcode.com/problems/encode-and-decode-tinyurl/description/)

O algoritmo utilizado para codificar e decodificar as URLs no problema "Encode and Decode TinyURL" é baseado no algoritmo de compressão de dados chamado Huffman. Esse algoritmo visa reduzir o tamanho da URL longa ao atribuir códigos binários mais curtos aos caracteres mais frequentes e códigos mais longos aos caracteres menos frequentes. A entrada consiste em uma URL longa válida, enquanto a saída é a URL curta gerada pelo processo de codificação ou a URL longa original restaurada pelo processo de decodificação usando a mesma classe Codec. Esse algoritmo permite uma codificação eficiente da URL longa em uma sequência de caracteres mais curta e a posterior decodificação dessa sequência para recuperar a URL original.

![Network Delay Time](/images/535.png)

## [1109. Corporate Flight Bookings](https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/)

A solução proposta para o problema das reservas de voos utiliza uma abordagem gananciosa, inspirada no algoritmo de Interval Partition. Em vez de percorrer todos os voos para atualizar os assentos a cada reserva, optamos por uma estratégia que minimiza o número de operações realizadas. Ao percorrer as reservas, adicionamos a quantidade de assentos reservados no voo inicial e subtraímos a mesma quantidade no voo seguinte ao término do intervalo da reserva, acumulando as alterações de assentos. Dessa forma, conseguimos obter o número total de assentos reservados para cada voo, evitando iterações desnecessárias.

![Minimum Score of a Path Between Two Citie](/images/1109.png)


# Instalação

Pré-Requisitos: Os códigos devem ser rodados na própria plataforma do leetcode, tendo em vista o uso de uma classe Solution, bem como o uso correto dos inputs por parte da plataforma.

Caso queira rodar local, é necessário somente chamar o método da classe com os paramêtros condizente com a assinatura de acordo com a linguagem desenvolvida.


# Uso
## Passo 1: Copiar o código
Entre na pasta do exercício específico, clique no arquivo e copie-o.

## Passo 2: Entrar na página do exercício
Ao clicar no título de cada questão presente neste README, você será redirecionado para a página da questão na plataforma LeetCode

## Passo 3: Alterar linguagem
Selecione a linguagem.

## Passo 4: Colar o código
Cole o código copiado no editor.

## Passo 5: Rodar o código
Abaixo do editor de código, clique em Run para executar o código.