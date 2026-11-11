class Cliente:
    def __init__(self, nome: str, telefone: str, email: str, tipo: str, id_cliente: int = None):
        self.id_cliente = id_cliente
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.tipo = tipo
    
    def __str__(self):
        return f"Cliente(nome={self.nome}, telefone={self.telefone}, email={self.email}, tipo={self.tipo})"
    
    def __repr__(self):
        return (f"Cliente(id_cliente={self.id_cliente!r}, " f"nome={self.nome!r}," f"telefone={self.telefone!r}," f"email={self.email!r}," f"tipo={self.tipo!r})"

     )
    
#Cadastrar cliente
def inserir_cliente(self, conexao):
    cursor = None

    try:
        cursor = conexao.cursor()

        sql = """INSERT INTO cliente (nome, telefone, email, tipo)
                 VALUES (%s, %s, %s, %s)
                 RETURNING id_cliente;"""

        valores = (self.nome, self.telefone, self.email, self.tipo)

        cursor.execute(sql, valores)

        self.id_cliente = cursor.fetchone()[0]

        conexao.commit()

        print("Cliente cadastrado com sucesso!")

        return self.id_cliente

    except Exception as erro:
        conexao.rollback()

        print(f"Erro ao cadastrar cliente: {erro}")

        return None

    finally:
        if cursor is not None:
            cursor.close()

#Listar clientes
@staticmethod
def listar_clientes(conexao):
    cursor = None

    try:
        cursor = conexao.cursor()

        sql = """SELECT id_cliente, nome, telefone, email, tipo
                 FROM cliente
                 ORDER BY id_cliente;"""

        cursor.execute(sql)
        resultados = cursor.fetchall()

        clientes = []

        for registro in resultados:
            cliente = Cliente(
                nome=registro[1],
                telefone=registro[2],
                email=registro[3],
                tipo=registro[4],
                id_cliente=registro[0]
            )

            clientes.append(cliente)

        return clientes

    except Exception as erro:
        print(f"Erro ao listar clientes: {erro}")
        return []

#Atualizar cliente
def atualizar_cliente(self, conexao):
    cursor = None

    try:
        cursor = conexao.cursor()

        sql = """UPDATE cliente
                  SET nome = %s, telefone = %s, email = %s, tipo = %s
                  WHERE id_cliente = %s;"""

        valores = (self.nome, self.telefone, self.email, self.tipo, self.id_cliente)

        cursor.execute(sql, valores)

        if cursor.rowcount == 0:
            conexao.rollback()
            print("Cliente não encontrado")
            return False
        
            conexao.commit()
            print("Cliente atualizado com sucesso!")
            return True

    except Exception as erro:
        conexao.rollback()

        print(f"Erro ao atualizar cliente: {erro}")

        return False

    finally:
        if cursor is not None:
            cursor.close()
            
#Excluir cliente
@staticmethod
def excluir_cliente(id_cliente: int, conexao):
    cursor = None

    try:
        cursor = conexao.cursor()

        sql = """DELETE FROM cliente WHERE id_cliente = %s"""

        cursor.execute(sql, (id_cliente,))

        if cursor.rowcount == 0:
            conexao.rollback()
            print("Cliente não encontrado")
            return False

        conexao.commit()
        print("Cliente excluído com sucesso!")
        return True

    except Exception as erro:
        conexao.rollback()
        print(f"Erro ao excluir cliente: {erro}")
        return False

    finally:
        if cursor is not None:
            cursor.close()