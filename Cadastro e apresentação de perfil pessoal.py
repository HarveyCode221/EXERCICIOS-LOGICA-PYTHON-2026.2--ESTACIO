def menu():
    print("Bem-vindo ao Cadastro de Perfil Pessoal.")
    nome = str(input('Insira o seu nome completo: '))
    idade = int(input('Insira a sua idade: '))
    altura = float(input('Insira a sua altura: '))
    cidade = str(input('Escreva o nome da sua cidade: '))

    validate(nome, idade, altura, cidade)

def validate(nome: str, idade: int, altura: float, cidade: str):
    #print("Seu nome é " + nome + " Sua idade é " + idade + " Sua altura é " + altura + " Sua cidade é " + cidade)
    if idade < 0 or altura < 0:
        print("Idade ou altura inválidos\n")
        menu()
    else:
        nome = nome.capitalize()
        cidade = cidade.capitalize()
        print(f"Seu nome é: {nome} \nsua idade é: {idade} \nsua altura é: {altura} \nsua cidade é: {cidade}")

menu()