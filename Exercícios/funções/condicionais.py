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
        return f"Valor final: R% {valor_compra * 0.85}"
     else:
         return f"Valor final: R%{valor_compra * 0.95}" 
     

def conceito_nota(nota: float):
    if nota >= 9 and nota < 10:
        return "A"
    if nota >= 7 and nota < 9:
        return "B" 
    if nota > 5 and nota < 7:
        return "C"
    else:
        return "F"
          
def tipo_triangulo(a:int, b:int, c:int):
    if (a + b> c) and (a + c >b) and (b + c > a):
        if a == b == c:
            return "Equilatero"
        elif a == b or a == c or b == c:
            return "Isosceles"
        else:
            return "Escalano"
    else: 
        return "Não é um triangulo"    

def calcular_imposto(salario: float):
    if salario <= 2000.00:
        return f"Isento: R$ {0.0}"
    elif salario > 2000.00 and salario <= 4000.00:
        return f"Valor do imposto: R$ {(salario - 2000)*0.1}"
    else:
        return f"Valor do imposto: R$ {(salario - 4000)*0.2 + 200}"  
            
        

         
        


      
    
         
         
 










if __name__ =="__main__":
    teste = fizz_buzz(15)
    print(teste) 

    idade = verificar_maioridade(18)
    print(idade) 

    impar = verificar_paridade(7) 
    print(impar) 
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

    vip = calcular_desconto(150.0, True) 
    print(f"6- {vip}")
    nao_vip = calcular_desconto(100.0, False)
    print(f"6- {nao_vip}")

    B = conceito_nota(8.5) 
    print(f"7- {B}")
    F = conceito_nota(4.2)
    print(f"7- {F}")

    Equilatero = tipo_triangulo(5, 5, 5)
    print(f"8- {Equilatero}")
    Nao_triangulo = tipo_triangulo(1, 2, 10)
    print(f"8- {Nao_triangulo}") 
                                   
    Isento = calcular_imposto(1800.0)
    print(f"9- {Isento}")
    Dez_por_cento = calcular_imposto(3000.0)
    print(f"9- {Dez_por_cento}")
    Vinte_por_cento = calcular_imposto(5000.0)
    print(f"9- {Vinte_por_cento}")








