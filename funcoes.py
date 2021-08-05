# Função é um trecho de código que tem um nome e pode
# receber informações externas para fazer seu trabalho.
# Opcionalmente, uma função pode também produzir um valor
# de resultado.
# Uma função é definida apenas uma vez e pode ser utilizada
# (chamada) várias vezes, evitando repetições de código.
# Existem funções já providas pela linguagem, como, por exemplo,
# len(), range() e sort(), e podemos definir também nossos próprias
# funções

def imc(peso, altura): # Definição (ou declaração) da função
    """
        Função que calcula o índice de massa Corpórea (IMC)
    """
    # Trechos entre aspas triplas são um tipo especial de 
    # comentario chamado docstring, e servem para documentar 
    # o propósito de uma função ou classe.
    return peso / altura ** 2 # Peso / (Altura)²

# float(): Converte o valor informado em um número com casas decimais
# (flooting point)
p = float(input('Informe o peso da pessoa: '))
a = float(input('Informe a altura da pessoa: '))

# Fazendo uma chamada à função imc()
resultado = imc(p, a)

print(f"I IMC calculado é {resultado}.")