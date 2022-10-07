| Aluna - Bruna Anunciação de Santana | Matrícula - 221216927 |

---
1. Resumo do projeto
2. Escolha do algoritmo
3. Justificativa
4. Complexidade
---
**Resumo do projeto** 

- Na entrada do projeto, ocorre a leitura do arquivo com as placas desordenadas. 
- Logo após, as placas são armazenadas em um vetor que faz parte da classe. 
- Ainda na classe, está implementado a ordenação das placas através do Radix Sort e Counting Sort. 
- E então no main, ocorre a ordenação da lista e a saída em um arquivo .piv, no mesmo formato da entrada.
---
**Escolha do algoritmo de ordenação**

O algoritmo de ordenação escolhido foi o Radix Sort, que ordena os elementos do vetor através dos dígitos. Houve uma mudança para que o algoritmo possa ordenar letras e números. 

---
**Justificativa**

A escolha do Radix Sort foi baseada nos requisitos do problema, era necessário um algoritmo que ordenasse de maneira lexicográfica e que houvesse a disponibilidade da implementação de paralelismo. 

Durante pesquisas sobre a ordenação lexicográfica[^1], existia a referencia sobre o radix sort como um algoritmo capaz de executar a ordenação. 

O radix sort, segundo as referências bibliográficas do professor[^2], é um bom algoritmo para usar paralelismo. 

Outro ponto citado no problema, era a recomendação de evitar ordenações com complexidades O(n(log(n)) e O(n²) por causa do volume de dados. O que não ocorre no radix sort.

Durante a construção do algoritmo, foi utilizado como referência um projeto de radix sort para strings[^3].

---
**Complexidade**

A complexidade do Radix Sort é O(nk), utilizando um algoritmo estável como o Counting Sort. Ou seja, o Radix Sort é um algoritmo de ordenação linear O(n).

---
**Referências bibliográficas**

[^1]:http://www.cs.umd.edu/~soheil/cmsc351/files/11-1-sort2.pdf
[^2]: https://mgarland.org/files/papers/nvr-2008-001.pdf
[^3]: https://stackoverflow.com/questions/60968950/radix-sort-for-strings-in-pytho

http://www.inf.ufsc.br/~r.mello/ine5384/19-OrdenacaoDados5.pdf

