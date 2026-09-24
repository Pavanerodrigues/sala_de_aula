Class Carta:

remetente:str
destinatario:str
conteudo:str

def __init__(self, remetente:str, destinatario:str, conteudo:str):
    self.conteudo = conteudo
    self.remetente = remetente
    self.destinatario = destinatario

    #Instancia 
    carta = Carta("Pavane", "neta","filhos")
