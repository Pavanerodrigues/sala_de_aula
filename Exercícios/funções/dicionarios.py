
def contar_maiores_de_idade(pessoas: list[tuple[str,int]]):
    count = 0

    for nome, idade in pessoas:
        if idade >= 18:
            count += 1

    return count 


def calcular_estoque_total(produtos):
    return sum(produtos.values())



def filtrar_aprovados(notas_alunos:dict):
    aprovados = [] 

    for nome, nota in notas_alunos.items():
        if nota >= 7.0:
            aprovados.append(nome)
    
    return aprovados
                      
                      
                      
                      
                      
                    






if __name__ == '__main__':
    maiores_idade = contar_maiores_de_idade([("Ana", 17), ("Bruno", 22), ("Carla", 19)])
    print(maiores_idade)

    estoque_total = calcular_estoque_total({"caneta": 10, "caderno": 5, "borracha": 8})
    print(estoque_total)

    aprovados = filtrar_aprovados({"Alice": 8.5, "Bruno": 5.0, "Carla": 7.0})
    print(aprovados)






