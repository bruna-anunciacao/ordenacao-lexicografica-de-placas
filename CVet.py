class cVet:
    def __init__(self):
        self.vetor = []

    def inserir(self, elemento):
        self.vetor.append(elemento)

    def tamanho(self):
        return len(self.vetor)

    def imprimir(self):
        for i in range(len(self.vetor)):
            print(self.vetor[i])

    def retorne(self, i):
        return self.vetor[i]

    def RadixSort(self):
        # for para definir o dígito das placas em cada loop
        # como as placas possuem tamanho fixo o range é 7 - 1
        # o passo é invertido para pegar o bit mais significativo
        for coluna in range(7 - 1, -1, -1):
            # chama o countingsort para ordenar o vetor com o parametro coluna
            self.vetor = self.countingSort(coluna)
        # retorna o vetor ordenado
        return self.vetor

    def countingSort(self, coluna):
        # vetor saida com o tamanho do vetor original
        saida = [0] * len(self.vetor)
        tamanho = len(self.vetor)
        # cont é o vetor responsável pelo armazenamento de quais letras estão sendo ordenadas
        cont = [0] * 37
        # min é o valor da tabela ASCII da menor letra que aparece nas placas
        min = ord('A') - 1
        # for para percorrer o tamanho do vetor
        for i in range(0, tamanho):
            # letra recebe o valor do vetor[i] com o digito que está na variável coluna
            letra = self.vetor[i][coluna]
            # if responsável por garantir que a letra é número ou não
            if letra.isnumeric() == True:
                # se for então caractere é igual ao int da letra
                caractere = int(letra)
            else:
                # senão caractere é igual ao valor da letra na tabela ascii menos o minimo
                caractere = ord(letra) - min
            # armazena 1 no vetor cont no indice caractere para a contagem de letras
            cont[caractere] += 1
        # for para percorrer o tamanho do vetor cont - 1
        for i in range(len(cont) - 1):
            # a soma garante que o vetor cont não possua espaços vazios entre os índices
            cont[i + 1] += cont[i]
        # for para percorrer o tamanho do vetor original em passo -1
        # equivalente ao reversed(vetor)
        for i in range(tamanho - 1, -1, -1):
            letra = self.vetor[i][coluna]
            if letra.isnumeric() == True:
                caractere = int(letra)
            else:
                caractere = ord(letra) - min
            # saida com o indice cont[caractere] -1 e atribui o valor do vetor na posição i para saída
            # o -1 garante que todas as posições do vetor cont existem
            saida[cont[caractere] - 1] = self.vetor[i]
            # diminui -1 da posição do vetor cont
            cont[caractere] -= 1
        # retorna o vetor ordenado
        return saida


