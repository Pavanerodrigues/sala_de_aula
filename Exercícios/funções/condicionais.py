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

def maior_de_dois(a:int, b: int):
    if a > b:
        return "O primeiro é maior"
    elif b > a:
        return "O segundo é maior"
    else:
        return "São iguais"
        
def calcular_desconto(valor_compra:float, cliente_vip:bool):
     if cliente_vip or valor_compra > 200:
        return "desconto = 15%"
     
     else: 
         return "desconto = 5%"






def conceito_nota(nota:float):
    if nota >= 9 and nota < 10:
        return "A"
    if nota >= 7 and nota < 9:
        return "B" 
    if nota > 5 and nota < 7:
        return "C"
    else:
        return "F"
    
      
    
         
         
 










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

    maior = maior_de_dois(10, 20)
    print(f"5- {maior}")
    iguais = maior_de_dois(5, 5)
    print(f"5- {iguais}")

    true = calcular_desconto(150.0, True) 
    print(f"6- {true}")
    false = calcular_desconto(100.0, False)
    print(f"6- {false}")

    B = conceito_nota(8.5) 
    print(f"7- {B}")
    F = conceito_nota(4.2)
    print(f"7- {F}")







