# Palíndromo: é um texto que, quando lido de trás para frente,
# mantém o mesmo conteúdo (desprezando acentos e espaçamento) 

# texto = "SOCORRAM-ME, SUBI NO ÔNIBUS EM MARROCOS"
texto = "BATATINHA QUANDO NASCE ESPALHA RAMA PELO CHÂO"

pilha = [] 

# Percurso do palíndromo, colocando cada letra na lista
for letra in texto:
    pilha.append(letra) # append() sempre acrescenta por ÚLTIMO

# pilha.insert(10, 'y')
# pilha.insert(19, 'g')
# pilha.insert(6, 'ç')

print(pilha)

inverso = ""

# Remoção de elementos em posições que não são a final 
# del pilha[11]   # Remove a posição 11
# del pilha[21]   # Remove a posição 21
# del pilha[8]   
# del pilha[25]   


# Retira cada letra da lista, de trás para frente, e coloca no inverso
while len(pilha) > 0:
    inverso += pilha.pop()  # pop() retira sempre o ÚLTIMO elemento

print(inverso)

# PILHA
# A pilha é um tipo abstrato de dados (TAD) que permite a entrada e a saída 
# de dados apenas na sua estremidade final. Como consequência, ela segue a 
# regra LIFO (last in, fist out - último a entrar, primeiro a sair), e tem
# acessolimitado aos seus elementos.

