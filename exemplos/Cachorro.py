class Cachorro:

    nome: str
    raca: str
    idade: int

    def __init__(self, nome: str, raca: str, idade: int):
        self.nome = nome
        self.raca = raca
        self.idade = idade  

    def latir(self):
        return f"Auau!O {self.nome} está latindo"                                 "
 