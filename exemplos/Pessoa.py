class Pessoa:

    nome: str
    cidade: str

    def __init__(self, nome: str, cidade: str):
        self.nome = nome
        self.cidade = cidade

    def apresentar(self):
        print("Olá, meu nome é {nome} e moro em {cidade}.")
    