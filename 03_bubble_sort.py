# ALGORITMO DE ORDENAÇÃO BULBBLE SORT
#
# Percorre a lista a ser ordenada em sucessivas passadaas, 
# trocando elementos adjacentes entre si quando a segunda for
# menor que o primeiro. Efetua tantas passadas quanto necessárias 
# até que, na última passada, nenhuma troca seja efetuada.

def bubble_sort(lista):
    """
        Função que implementa o algoritmo de ordenação Bubble Sort
    """
    while True:     # Loop eterno
        trocou = false
        # Loop na lista até o PENULTIMO elemento len(lista) - 2
        # Ex. em uma lista de 10 elementos, len(lista) == 10.
        # A última posição estará em len(lista) - 1, ou seja 9.
        # A penultima posição estará em len(lista) - 2, ou seja 8.
        for i in range(len(lista) - 2): # Inicía nova passada
            if lista[i + 1] < lista[i]: # É necessário trocar
                lista[i + 1], lista[i] = lista[i], lista[i + 1] # Faz a troca
                trocou = True

        # Se houve troca, a lista está ordenada e podemos interromper 
        # Se o loop while
        if not trocou: # trocou == false
            break   # Interrompe o while
