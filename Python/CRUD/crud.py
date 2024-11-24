usuarios = []

def criar_usuario(nome, idade):
    usuario = {
        "id": len(usuarios) + 1,
        "nome": nome,
        "idade": idade,
    }
    usuarios.append(usuario)

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado")
        return
    


        