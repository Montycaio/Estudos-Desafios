# Lista para armazenar os usuários (simulando um banco de dados)
usuarios = []

def criar_usuario(nome, idade):
    """
    Função para criar um novo usuário
    """
    usuario = {
        "id": len(usuarios) + 1,
        "nome": nome,
        "idade": idade
    }
    usuarios.append(usuario)
    print(f"Usuário {nome} criado com sucesso!")

def listar_usuarios():
    """
    Função para mostrar todos os usuários
    """
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    
    print("\nLista de Usuários:")
    for usuario in usuarios:
        print(f"ID: {usuario['id']}, Nome: {usuario['nome']}, Idade: {usuario['idade']}")

def buscar_usuario(id):
    """
    Função para buscar um usuário pelo ID
    """
    for usuario in usuarios:
        if usuario['id'] == id:
            print(f"\nUsuário encontrado:")
            print(f"ID: {usuario['id']}, Nome: {usuario['nome']}, Idade: {usuario['idade']}")
            return usuario
    print("Usuário não encontrado.")
    return None

def atualizar_usuario(id, novo_nome, nova_idade):
    """
    Função para atualizar os dados de um usuário
    """
    usuario = buscar_usuario(id)
    if usuario:
        usuario['nome'] = novo_nome
        usuario['idade'] = nova_idade
        print(f"Usuário {id} atualizado com sucesso!")

def deletar_usuario(id):
    """
    Função para deletar um usuário
    """
    for i, usuario in enumerate(usuarios):
        if usuario['id'] == id:
            usuarios.pop(i)
            print(f"Usuário {id} deletado com sucesso!")
            return
    print("Usuário não encontrado.")

# Exemplo de uso do CRUD
def menu():
    while True:
        print("\n=== MENU DO SISTEMA ===")
        print("1. Criar usuário")
        print("2. Listar usuários")
        print("3. Buscar usuário")
        print("4. Atualizar usuário")
        print("5. Deletar usuário")
        print("6. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))
            criar_usuario(nome, idade)
        
        elif opcao == "2":
            listar_usuarios()
        
        elif opcao == "3":
            id = int(input("Digite o ID do usuário: "))
            buscar_usuario(id)
        
        elif opcao == "4":
            id = int(input("Digite o ID do usuário: "))
            nome = input("Digite o novo nome: ")
            idade = int(input("Digite a nova idade: "))
            atualizar_usuario(id, nome, idade)
        
        elif opcao == "5":
            id = int(input("Digite o ID do usuário: "))
            deletar_usuario(id)
        
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()