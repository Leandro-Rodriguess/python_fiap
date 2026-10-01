idade = int(input("Digite sua idade: "))
match idade:
    case x if x < 0:
        print("Idade inválida")
    case x if x < 13:
        print("Você é uma criança")
    case x if x < 17:
        print("Você é um adolescente")
    case x if x < 60:
        print("Você é um adulto")
    case _:
        print("Você é idoso")