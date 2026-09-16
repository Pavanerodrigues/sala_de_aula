def formatar_saudacao(nome: str , cidade: str):
    return f"Olá {nome}, seja bem vindo(a) a {cidade}"

def calcular_perimetro(largura: float, altura: float):
    perimetro = 2 * (largura + altura)
    return perimetro

def fahrenheit_para_celsius(temp_f: float):
    temp_celsius = (temp_f - 32) *(5/9)
    return temp_celsius

def calcular_gorjeta_por_pessoas(conta: float, porcentagem_gorjeta:float, pessoas:int):
    gorjeta = (conta * (porcentagem_gorjeta / 100)) / pessoas
    return gorjeta

def resumo_circulo(raio:float):
    pi =3.14159
    area = pi * (raio**2)
    return f"umcirculo de raio {raio} tem área de {area:.2f}"

def resumo_juros_compostos(capital:float, taxa:float, anos:int):
    M = capital *(1+taxa/100)**anos
    return f"Após{anos} anos,R$ {capital}, cresce para R${M:.2f}"






if __name__ == '__main__':
    variavel = formatar_saudacao("Alice", "Porto Alegre")
    print(variavel)
    perimetro = calcular_perimetro(altura=10, largura=5)
    print(f"2 - {perimetro}")

    temperatura_celsius = fahrenheit_para_celsius(68)
    print (f"3 -{temperatura_celsius}")

    gorjeta = calcular_gorjeta_por_pessoas(100, 15, 3)
    print (f"4 - {gorjeta}")
    
    resumo= resumo_circulo(3.0) 
    print (f"5 - {resumo}") 

    resumo = resumo_juros_compostos(1000.0, 5.0, 3)
    print(f"6 - {resumo}")