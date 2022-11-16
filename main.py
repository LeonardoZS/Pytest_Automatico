#Leonardo Zaniboni Silva 11801049
import pytest      
def fibonacci(x):                                           #Definindo a função fibonacci
    if x==0: return 0                                       
    if x==2 or x==1 :return 1
    else: return fibonacci(x-1) + fibonacci(x-2)

def fatorial(x):                                            #Definindo a função fatorial
    if x<2:return 1
    else: return x*fatorial(x-1)

#Definindo a função que irá checar se o resultado bate com o arquivo certo
def test_certo():
    linha = [] ; erro = False ; count = 1
    with open('output_certo.txt') as output:
        dados = output.read()                               #lendo o arquivo
    for i in range(len(dados)):                             #varrendo o arquivo
        if dados[i] == "\n":                                #contando em qual linha a varredura esta
            count = count + 1
        if dados[i] == saida[i]: pass                       #comparando os resultados
        else:
            linha.append(count)                             #armazenando as linhas em caso de erro
            erro = True
    assert erro == False, print(f"A comparação resultou em {len(linha)} erros diferentes, onde cada um deles seguem presentes nas seguintes linhas {linha}, em ordem. Lembrar de considerar as linhas vazias do arquivo fornecido!!!!!!!!!.")

#Definindo a função que irá checar se o resultado apresenta erros quando comparado com arquivo errado
def test_errado():
    linha = [] ; erro = False ; count = 1
    with open('output_errado.txt') as output:
        dados = output.read()
    for i in range(len(dados)):
        if dados[i] == "\n":
            count = count + 1
        if dados[i] == saida[i]: pass
        else:
            linha.append(count)
            erro = True
    assert erro == False, print(f"A comparação resultou em {len(linha)} erros diferentes, onde cada um deles seguem presentes nas seguintes linhas {linha}, em ordem. Lembrar de considerar as linhas vazias do arquivo fornecido!!!!!!!!!.")

input = [1,2,4,9,7]                                         #dados de entrada
fibo = [] ; fact = []                                       #inicializando os vetores
saida = f"# fact Fib\n"                                     #montando o cabecario
for i in range(len(input)):                                 
    fibo.append(fibonacci(int(input[i])))                   #calculando o fibonacci
    fact.append(fatorial(int(input[i])))                    #calculando o fatorial
    saida = saida + f"\n{input[i]} {fact[i]} {fibo[i]}\n"   #escrevendo os resultados na string saida