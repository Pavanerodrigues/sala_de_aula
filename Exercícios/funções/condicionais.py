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
        return "menor de idade"
    
       


   



if __name__ =="__main__":
    teste = fizz_buzz(15)
    print(teste) 

    idade = verificar_maioridade(18)
    print(idade)


