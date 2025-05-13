def selection_sort(lista): #Função que implementa o selection sort com a intenção de ordenar a lista
    tamanho = len(lista) #Obtém o tamanho da lista pra ser usado noa loops
    
    # Percorre cada posição da lista
    for i in range(tamanho):
        menor = i  # Vamos supor que o menor número está na posição i
        
        # Procurando o menor número no restante da lista
        for j in range(i + 1, tamanho):
            if lista[j] < lista[menor]: # Compara o elemento na posição j com o elemento na posição 'menor'
                menor = j  # Achamos um número menor, guardamos a posição dele
        
        # Trocando os números de lugar
        lista[i], lista[menor] = lista[menor], lista[i]

#main
n =  [2, 150, 3, 0, 9, 48, 8, 35, 5] # Cria uma lista desordenada para teste
selection_sort(n) # Chama a função selection_sort para ordenar a lista n
print("Lista ordenada: " , n) # Vai mostrar [0, 2, 3, 5, 8, 9, 35, 48, 150]
