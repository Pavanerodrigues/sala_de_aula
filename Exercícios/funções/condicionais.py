def fizz_buzz(numero:int):
    if numero % 3 == 0 and numero % 5 == 0:
        return "fizzbuzz"
    elif numero % 3 == 0:
        return "fizz"
    elif numero % 5 == 0:
        return "buzz"
    else:
        return numero    
  
def verificar_maioridade(idade:int):
    if idade >= 18:
        return "maior de idade"
    else:
        return "menor de idada"

def verificar_paridade(numero:int):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

def classificar_numero(numero:int):
    if numero > 0:
        return "Positivo"
    if numero < 0:
        return "Negativo"
    return "Zero"

def calcular_resultado(nota1:int, nota2:int):
    if nota1 >= 7.0:
        return "aprovado"
    else:
        return "reprovado"






if __name__ =="__main__":
    teste = fizz_buzz(15)
    print(teste) 

    idade = verificar_maioridade(18)
    print(idade) 

    Ímpar = verificar_paridade(7) 
    print(Ímpar) 
    Par = verificar_paridade(12)
    print(Par) 

    negativo = classificar_numero(-5)
    print(f"3- {negativo}")  
    
    aprovado = calcular_resultado(8.0, 6.0)
    print(f"4- {aprovado}")