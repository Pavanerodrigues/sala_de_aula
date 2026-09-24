def dobrar(numeros:[]):
    for numero in numeros:
        numero = numero * 2
        print(numero)

def filtrar_pares(numeros: list):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)

    return pares        
    
def contar_negativos(numeros: list):
    count = 0
    for numero in numeros:
        if numero < 0:
            count+=1
    return count
        
def somar_maiores_que(numeros: list, limite: int):
    soma = 0
    for numero in numeros:
        if numero > limite:
            soma+=numero

    return soma

def zerar_negativos(numeros: list):
    aux = numeros.copy()

    for numero in numeros:
        if numero < 0:
            indice = numeros.index(numero)
            aux[indice] = 0
    
    return aux

def contem_valor(lista: list, alvo):
    indice = 0

    while indice < len(lista):
        if lista[indice] == alvo:
            return True
        indice += 1
    
    return False

def contar_aprovados(notas: list):
    count = 0 
    for nota in notas:
        if nota >= 7:
            count+=1 
    return count
    
def filtrar_palavras_curtas(palavras: lista, tamanho_maximo: int):
    filtro = [] 
    for palavra in palavras:
        if len(palavra) <= tamanho_maximo:
            filtro.append(palavra) 
    return filtro        
















if __name__=="__main__":
    dobrar([1,2,3,4,5])
    
    numeros_pares = filtrar_pares([1, 2, 3, 4, 5, 6])
    print(numeros_pares)

    numeros_negativo = contar_negativos([10, -3, 0, -5, 8, -1])
    print(numeros_negativo) 

    numeros_maiores = somar_maiores_que([10, 5, 20, 3, 15], 8)
    print(numeros_maiores) 

    numeros_negativo = zerar_negativos([4, -2, 7, -9, 0])
    print(numeros_negativo)

    alvo = contem_valor(["maçã", "banana", "uva"],"banana")
    print(alvo)

    alunos = contar_aprovados([8.5, 5.0, 7.0, 6.5,9.0])
    print(alunos)

    palavras_curtas = filtrar_palavras_curtas(["sol", "computador", "python", "mar"], 6)
    print(palavras_curtas)

