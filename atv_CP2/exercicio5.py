type = input("Digite o tipo de pedido (troca, suporte ou devolução): ").strip().lower()
prioridade = int(input("Digite a prioridade (1, 2 ou 3): "))
 
match (type, prioridade):
    case ("troca" | "devolução", 1):
        print("Setor: Pós-venda")
        print("Prazo: Atendimento imediato")
    case ("troca" | "devolução", 2):
        print("Setor: Pós-venda")
        print("Prazo: Até 4 horas.")
    case ("troca" | "devolução", 3):
        print("Setor: Pós-venda")
        print("Prazo: Até um dia útil.")
 
 
    case ("suporte", 1):
        print("Setor: Técnico")
        print("Prazo: Atendimento imediato")
    case ("suporte", 2):
        print("Setor: Técnico")
        print("Prazo: Até 4 horas")
    case ("suporte", 3):
        print("Setor: Técnico")
        print("Prazo: Até 1 dia útil")
 
    case _:
        print("Tipo ou prioridade inválidos")
   