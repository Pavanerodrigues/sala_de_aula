from tests.relatorio import (
    Aluguel,
    RelatorioDoMes,
    total_do_cliente,
    alugueis_com_valores
)


def test_todos_alugueis_mesmo_cliente():
    # Cenário
    alugueis = [
        Aluguel("Ana", "Fifa", 20),
        Aluguel("Ana", "Skyrim", 30),
        Aluguel("Ana", "GTA", 10)
    ]

    # Ação
    total = total_do_cliente(alugueis, "Ana")

    # Validação
    assert total == 60


def test_alugueis_com_valores():
    # Cenário
    alugueis = alugueis_com_valores(25.0, 30.0, 40.0)

    # Ação
    relatorio = RelatorioDoMes()
    relatorio.avaliar(alugueis)

    # Validação
    assert relatorio.maior == 40.0
    assert relatorio.menor == 25.0



