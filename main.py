import CVet

# inicia o arquivo .piv e armazena na variável
abrir = open("PIVs-10000.piv", "r")
# lê as linhas de f e armazena em dados como um vetor
dados = abrir.readlines()
# cria um vetor na classe CVet para armazenar as placas
placas = CVet.cVet()
# retira o \n como ultimo elemento das placas
linhas = [x.strip('\n') for x in dados]
# for para inserir através da operação da classe
for i in linhas:
    placas.inserir(i)
# aplica o radixsort no vetor da classe
placas.RadixSort()
# inicia um processo de escrita para armazenar as placas ordenadas em um arquivo .piv
with open('placas_ordenadas.piv', 'w') as saida:
    for i in range(placas.tamanho()):
        saida.write(str(placas.retorne(i)) + '\n')