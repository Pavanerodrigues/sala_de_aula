from relatorio import Aluguel,RelatorioDoMes, total_do_cliente
def test_todos_alugueis_mesmo_cliente():
    #Cenário
    alugueis =[
        Aluguel("Ana", "Fifa", 20),
        Aluguel("Ana", "Skyrim", 30),
        Aluguel("Ana", "GTA", 10)
    ] 



    



    #Ação 

    total =total_do_cliente(alugueis=alugueis, RelatorioDoMes)

    #Validação
 
    assert total == 60

    

def test_alugueis_com_valores(*valores):
    #Cenário
    alugueis = [
        Aluguel("Ana", "FIFA 25", 30.0),
        Aluguel("Bruno", "Zelda", 40.0),
        Aluguel("Carla", "Mario Kart", 25.0),
        Aluguel("Ana", "FIFA 25", 30.0),
    ]



     #Ação

    total =total_do_cliente(alugueis=alugueis, cliente="Ana")

    #Validação
    assert total == 30
    

    relatorio.avaliar(alugueis_com_valores(25.0, 30.0, 40.0))