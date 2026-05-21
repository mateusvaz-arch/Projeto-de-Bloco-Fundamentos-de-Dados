import datetime

def adicionar_tarefa(lista_tarefas, descricao, prazo_final, urgencia="Baixa", status="A Fazer"):

    # Gera um ID incremental baseado no tamanho da lista
    novo_id = len(lista_tarefas) + 1
    data_criacao = datetime.date.today().strftime("%d/%m/%Y")
    
    # Utilizando um dicionário para armazenar os metadados da tarefa
    nova_tarefa = {
        "id": novo_id,
        "descricao": descricao,
        "data_criacao": data_criacao,
        "status": status,
        "prazo_final": prazo_final,
        "urgencia": urgencia
    }
    
    lista_tarefas.append(nova_tarefa)
    return novo_id

def listar_tarefas(lista_tarefas, apenas_pendentes=False):
   
    if not lista_tarefas:
        print("Nenhuma tarefa cadastrada na lista no momento.")
        return False

    encontrou_tarefa = False
    print("\n Lista de Tarefas")
    print(25*"--")
    

    for tarefa in lista_tarefas:
        if apenas_pendentes and tarefa["status"] == "Concluída":
            continue
        
        encontrou_tarefa = True
        print(f"[{tarefa['id']}] {tarefa['descricao']}")
        print(f"    Criada em: {tarefa['data_criacao']} | Prazo: {tarefa['prazo_final']}")
        print(f"    Status: {tarefa['status']} | Urgência: {tarefa['urgencia']}")
        print("--" * 25)
    
    if not encontrou_tarefa:
        print("Nenhuma tarefa pendente encontrada.")
        
    return encontrou_tarefa

def marcar_concluida(lista_tarefas, tarefa_id):
    
    for tarefa in lista_tarefas:
        if tarefa["id"] == tarefa_id:
            tarefa["status"] = "Concluída"
            return True
    return False

def remover_tarefa(lista_tarefas, tarefa_id):
    """
    Remove definitivamente uma tarefa da lista através do seu ID.

    Parâmetros:
    lista_tarefas (list): A lista principal contendo as tarefas.
    tarefa_id (int): O identificador único da tarefa a ser deletada.

    Retorna:
    bool: Retorna True se a tarefa foi removida, False se o ID não for encontrado.
    """
    for i, tarefa in enumerate(lista_tarefas):
        if tarefa["id"] == tarefa_id:
            del lista_tarefas[i] # Remove o item 
            return True
    return False

def main():
    
    tarefas = []
    
    # while para manter o programa em execução até o usuário escolher sair
    while True:
        print("\n" + "="*35)
        print("SISTEMA DE GERENCIAMENTO DE TAREFAS")
        print("1. Adicionar Tarefa")
        print("2. Listar Todas as Tarefas")
        print("3. Listar Apenas Tarefas Pendentes")
        print("4. Marcar Tarefa como Concluída")
        print("5. Remover Tarefa")
        print("6. Sair do Programa")
        print("="*35)
        
        opcao = input("Escolha uma opção do menu: ")
        
        if opcao == "1":
            descricao = input("Descrição da tarefa: ")
            prazo = input("Prazo final [ex: 20/05/2026]: ")
            urgencia = input("Nível de urgência (Baixa |Média | Alta): ")
            
            # Condicional testando o uso de parâmetros padrão e argumentos nomeados 
            if not urgencia:
                novo_id = adicionar_tarefa(lista_tarefas=tarefas, descricao=descricao, prazo_final=prazo)
            else:
                novo_id = adicionar_tarefa(lista_tarefas=tarefas, descricao=descricao, prazo_final=prazo, urgencia=urgencia)
                
            print(f"\nTarefa adicionada! O ID da sua tarefa é: {novo_id}")
            
        elif opcao == "2":
            listar_tarefas(tarefas)
            
        elif opcao == "3":
            # Uso de argumento nomeado opcional
            listar_tarefas(tarefas, apenas_pendentes=True)
            
        elif opcao == "4":
            try:
                id_tarefa = int(input("Digite o ID da tarefa que deseja concluir: "))
                if marcar_concluida(tarefas, tarefa_id=id_tarefa):
                    print(f"\n Tarefa {id_tarefa} marcada como concluída!")
                else:
                    print(f"\nErro! Tarefa com ID {id_tarefa} não encontrada.")
            except ValueError:
                print("\nErro! Por favor, digite um número de ID válido.")
                
        elif opcao == "5":
            try:
                id_tarefa = int(input("Digite o ID da tarefa a ser removida: "))
                if remover_tarefa(tarefas, tarefa_id=id_tarefa):
                    print(f"\nTarefa {id_tarefa} removida da lista!")
                else:
                    print(f"\nErro! Tarefa com ID {id_tarefa} não encontrada.")
            except ValueError:
                print("\nErro! Por favor, digite um número de ID válido.")
                
        elif opcao == "6":
            print("\nAté logo!")
            break
            
        else:
            print("\nErro! Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()