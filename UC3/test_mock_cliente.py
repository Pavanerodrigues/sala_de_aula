
from unittest.mock import Mock, patch
from cliente import Cliente


def test_cria_cliente():
    cliente = Cliente(
        "João",
        "11999999999",
        "joao@email.com",
        "Pessoa Física"
    )

    assert cliente.nome == "João"
    assert cliente.telefone == "11999999999"
    assert cliente.email == "joao@email.com"
    assert cliente.tipo == "Pessoa Física"


def test_cliente_com_id():
    cliente = Cliente(
        "Maria",
        "11988888888",
        "maria@email.com",
        "Pessoa Jurídica",
        10
    )

    assert cliente.id_cliente == 10


def test_cliente_sem_id():
    cliente = Cliente(
        "Pedro",
        "11977777777",
        "pedro@email.com",
        "Pessoa Física"
    )

    assert cliente.id_cliente is None


def test_representacao_cliente():
    cliente = Cliente(
        "Ana",
        "11966666666",
        "ana@email.com",
        "Pessoa Física"
    )

    assert "Cliente(nome=Ana" in str(cliente)


def test_mock_cliente():
    cliente = Mock(spec=Cliente)

    cliente.nome = "Carlos"
    cliente.telefone = "11955555555"

    assert cliente.nome == "Carlos"
    assert cliente.telefone == "11955555555"


def test_mock_cliente_metodo():
    cliente = Mock(spec=Cliente)

    cliente.__str__.return_value = "Cliente simulado"

    assert str(cliente) == "Cliente simulado"
