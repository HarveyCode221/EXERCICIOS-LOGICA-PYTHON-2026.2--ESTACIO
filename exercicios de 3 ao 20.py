
# Exercício 3
def menu():
    print("Insira uma temperatura expressa em graus para converter pra Fahrenheit e Kelvin.\n")
    temperaturacelsius = float(input('Temperatura em celsius: '))
    calculo(temperaturacelsius)

def calculo(tcelcius: float):
    fahrenheit = tcelcius * 9/5 + 32
    kelvin = tcelcius + 273.15

    print(f"A temperatura dada foi {tcelcius}ºC \nA temperatura para fahreinte é: {fahrenheit:.2f}ºF \nA temperatura para kelvin é: {kelvin:.2f}ºK")

menu()

# exercício 4

def menu():
    print("Insira as suas notas!\n")
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    nota3 = float(input('Terceira nota: '))

    calculo(nota1, nota2, nota3)

def calculo(nota1: float, nota2: float, nota3: float):
    if nota1 >= 0 and nota1 <= 10 and nota2 >= 0 and nota2 <= 10 and nota3 >= 0 and nota3 <= 10:

        resultado = nota1 + nota2 + nota3 / 3

        if resultado >= 7:
            print("\nAprovado!")
        if resultado > 5 and resultado < 6.9:
            print("\nRecuperação...")
        if resultado < 5:
            print("\nReprovado")

    else:
        print("\nNota inválida!\n")
        menu()

menu()





# execicio 5 - idades


classificacoes = ['Criança', 'Adolescente', 'Adulto', 'Idoso']

def menu():
    
    print("Insira a sua idade para que seja lhe dado uma classificação.\n")
    idade = int(input('Idade: '))

    calculo(idade)

def calculo(idade: int):
    classiatual = " "

    if idade < 0:
        print("Idade inválida...\n")
        menu()
    else:
        if idade <= 12:
            classiatual = classificacoes[0]
        if idade >= 13 and idade <= 17:
            classiatual = classificacoes[1]
        if idade >= 18 and idade <= 59:
            classiatual = classificacoes[2]
        if idade >= 60:
            classiatual = classificacoes[3]

        print(f"Sua idade é {idade} e a sua classificação {classiatual}")

menu()

# exercicio 6 - entrada de 3 numeros

print("Insira três números \n")

num1 = float(input("digite o primeiro número: ")) # maior numero
num2 = float(input("digite o primeiro número: ")) # menor numero
num3 = float(input("digite o primeiro número: ")) # num intermediário

if num1 > num2 and num2 > num3:
    print(f"o maior numero é {num1}, o intermediário é {num2}, o menor é {num3}")
elif num1 > num3 and num3 > num2: 
    print(f"o maior numero é {num1}, o intermediário é {num3}, o menor é {num2}")
elif num2 > num1 and num1 > num3:
    print(f"o maior numero é {num2}, o intermediário é {num1}, o menor é {num3}")
elif num2 > num3 and num3 > num1:
    print(f"o maior numero é {num2}, o intermediário é {num3}, o menor é {num2}")
elif num3 > num2 and num2 > num1:
    print(f"o maior numero é {num3}, o intermediário é {num2}, o menor é {num1}")
elif num3 > num1 and num1 > num2:
    print(f"o maior numero é {num3}, o intermediário é {num1}, o menor é {num2}")




def numeros():
    while True:
        try:
            num = int(input("Digite um número inteiro: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira apenas números inteiros.")

    if num > 0:
        sinal = "positivo"
    elif num < 0:
        sinal = "negativo"
    else:
        sinal = "nulo"

    if num % 2 == 0:
        paridade = "par"
    else:
        paridade = "ímpar"

    print(f"O número {num} é {sinal} e {paridade}.")

numeros()


# exercicio 8 -> Estatística descritiva de conjunto numérico  

lista_numeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
soma_numeros = 0
numeros_positivos = 0
numeros_negativos = 0
numeros_pares = 0
numeros_impares = 0
media_aritmetica = 0


for i in range(len(lista_numeros)):
    lista_numeros[i] = int(input(f'Insira o {i + 1}º número'))

    soma_numeros += int(lista_numeros[i])
    
for i in range(len(lista_numeros)):
    if lista_numeros[i] > 0:
        numeros_positivos += 1
    elif lista_numeros[i] < 0:
        numeros_negativos += 1

    if lista_numeros[i] % 2 == 0:
        numeros_pares += 1
    else: 
        numeros_impares += 1

    media_aritimética = soma_numeros / len(lista_numeros)

print(f'a soma dos números é: {soma_numeros}')
print(f'os numeros positivos são: {numeros_positivos}')
print(f'os numeros negativos são: {numeros_negativos}')
print(f'os numeros pares são: {numeros_pares}')
print(f'os numeros impares são: {numeros_impares}')
print(f'a média aritmética é: {media_aritimética: .2f}')


# exercicio 9 ->  Geração de tabuada de multiplicação

numerox = int(input('Insira um número inteiro: '))

for i in range(1, 11):
    resultado = numerox * i 
    print(f" {numerox} x {i} = {resultado}") 


# exercicio 10 -> Análise de temperaturas registradas em uma semana

temperaturas = []

for i in range(1, 8):
    temperatura = float(input(f'Insira a {i}º temperatura: '))
    temperaturas.append(temperatura)

maior_temperatura = max(temperaturas)
menor_teperatura = min(temperaturas)

media  = sum(temperaturas) / (len(temperaturas))

# dias que a temperatur ficou acima da média
temp_dia = 0
for temp in temperaturas:
    if temp > media:
        temp_dia += 1


print("calor do djabo rgistrado: ")
print(f'maior temperatura: {maior_temperatura: .2f}')
print(f'menor temperatura: {menor_teperatura: .2f}')
print(f'temperatura média: {media: .2f}')
print(f'dias que ficaram acima da média: {temp_dia}')


# exercicio 11 -> Cadastro e inventário de produtos em estoque 

# QUESTÃO 12 - Cadastro de produtos

produtos = []

print("===== CADASTRO DE PRODUTOS =====")

for i in range(1, 6):
    print(f"\nProduto {i}")

    nome = input("Nome do produto: ")

    while True:
        try:
            preco = float(input("Preço unitário: R$ ").replace(",", "."))

            if preco >= 0:
                break
            else:
                print("O preço não pode ser negativo.")

        except ValueError:
            print("Digite um preço válido.")

    while True:
        try:
            quantidade = int(input("Quantidade em estoque: "))

            if quantidade >= 0:
                break
            else:
                print("A quantidade não pode ser negativa.")

        except ValueError:
            print("Digite uma quantidade inteira válida.")

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)

# Calculando valor total do estoque
valor_total = 0

for produto in produtos:
    valor_total += produto["preco"] * produto["quantidade"]

# Encontrando produto com maior preço
produto_mais_caro = produtos[0]

for produto in produtos:
    if produto["preco"] > produto_mais_caro["preco"]:
        produto_mais_caro = produto

print("\n===== PRODUTOS CADASTRADOS =====")

for produto in produtos:
    print(f"\nNome: {produto['nome']}")
    print(f"Preço: R$ {produto['preco']:.2f}")
    print(f"Quantidade: {produto['quantidade']}")

print(f"\nValor total do estoque: R$ {valor_total:.2f}")

print("\nProduto com maior preço unitário:")
print(f"Nome: {produto_mais_caro['nome']}")
print(f"Preço: R$ {produto_mais_caro['preco']:.2f}")

# exercicio 13 -> Agenda de contatos

contatos = []

print("===== AGENDA DE CONTATOS =====")

for i in range(1, 6):
    print(f"\nContato {i}")

    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    contatos.append(contato)

nome_busca = input("\nDigite o nome que deseja consultar: ")

encontrado = False

for contato in contatos:
    if contato["nome"].lower() == nome_busca.lower():
        print("\n===== CONTATO ENCONTRADO =====")
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"E-mail: {contato['email']}")

        encontrado = True
        break

if not encontrado:
    print("Contato não encontrado.")


# exercicio 14 => Gerenciamento de notas da turma

def ler_nota(numero_nota):
    while True:
        try:
            nota = float(
                input(f"Digite a {numero_nota}ª nota (0 a 10): ").replace(",", ".")
            )

            if 0 <= nota <= 10:
                return nota
            else:
                print("A nota deve estar entre 0 e 10.")

        except ValueError:
            print("Digite uma nota válida.")


def calcular_media(notas):
    return sum(notas) / len(notas)


estudantes = []

print("=====CADASTRO DA TURMA=====")

for i in range(1, 6):
    print(f"\nEstudante {i}")

    nome = input("Nome: ")

    notas = []

    for j in range(1, 4):
        notas.append(ler_nota(j))

    media = calcular_media(notas)

    estudante = {
        "nome": nome,
        "notas": notas,
        "media": media
    }

    estudantes.append(estudante)

# Encontrar maior e menor média
maior_media = estudantes[0]
menor_media = estudantes[0]

aprovados = 0
recuperacao = 0
reprovados = 0

for estudante in estudantes:

    if estudante["media"] > maior_media["media"]:
        maior_media = estudante

    if estudante["media"] < menor_media["media"]:
        menor_media = estudante

    if estudante["media"] >= 7:
        aprovados += 1
    elif estudante["media"] >= 5:
        recuperacao += 1
    else:
        reprovados += 1

print("====RESULTADO DA TURMA=====")

for estudante in estudantes:
    print(
        f"{estudante['nome']} - "
        f"Média: {estudante['media']:.2f}"
    )

print(f"\nMaior média: {maior_media['nome']} - {maior_media['media']:.2f}")
print(f"Menor média: {menor_media['nome']} - {menor_media['media']:.2f}")

print(f"\nAprovados: {aprovados}")
print(f"Recuperação: {recuperacao}")
print(f"Reprovados: {reprovados}")


# exercicio 15 - Cadastro de cidades

cidades = []

print("===== CADASTRO DE CIDADES =====")

for i in range(1, 6):

    print(f"\nCidade {i}")

    nome = input("Nome da cidade: ")
    estado = input("Estado (sigla): ").upper()

    while True:
        try:
            populacao = int(input("População estimada: "))

            if populacao >= 0:
                break
            else:
                print("A população não pode ser negativa.")

        except ValueError:
            print("Digite uma população inteira válida.")

    cidade = {
        "nome": nome,
        "estado": estado,
        "populacao": populacao
    }

    cidades.append(cidade)

# Encontrando maior e menor população
maior = cidades[0]
menor = cidades[0]

populacao_total = 0

for cidade in cidades:

    populacao_total += cidade["populacao"]

    if cidade["populacao"] > maior["populacao"]:
        maior = cidade

    if cidade["populacao"] < menor["populacao"]:
        menor = cidade

media = populacao_total / len(cidades)

print("\n===== DADOS DAS CIDADES =====")

for cidade in cidades:
    print(
        f"Cidade: {cidade['nome']} - "
        f"Estado: {cidade['estado']} - "
        f"População: {cidade['populacao']}"
    )

print("\n===== ANÁLISE POPULACIONAL =====")

print(
    f"Maior população: {maior['nome']} - "
    f"{maior['populacao']}"
)

print(
    f"Menor população: {menor['nome']} - "
    f"{menor['populacao']}"
)

print(f"População total: {populacao_total}")
print(f"Média populacional: {media:.2f}")


# QUESTÃO 16 - Gerenciamento de números

numeros = []

while True:

    print("\n================================")
    print("    GERENCIAMENTO DE NÚMEROS")
    print("================================")
    print("1 - Cadastrar número")
    print("2 - Listar números")
    print("3 - Exibir maior número")
    print("4 - Exibir menor número")
    print("5 - Calcular média")
    print("0 - Encerrar programa")
    print("================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        try:
            numero = float(input("Digite o número: ").replace(",", "."))
            numeros.append(numero)
            print("Número cadastrado com sucesso.")

        except ValueError:
            print("Erro: digite um número válido.")

    elif opcao == "2":

        if len(numeros) == 0:
            print("Nenhum número cadastrado.")
        else:
            print("\nNúmeros cadastrados:")

            for numero in numeros:
                print(numero)

    elif opcao == "3":

        if len(numeros) == 0:
            print("Nenhum número cadastrado.")
        else:
            print(f"Maior número: {max(numeros)}")

    elif opcao == "4":

        if len(numeros) == 0:
            print("Nenhum número cadastrado.")
        else:
            print(f"Menor número: {min(numeros)}")

    elif opcao == "5":

        if len(numeros) == 0:
            print("Nenhum número cadastrado.")
        else:
            media = sum(numeros) / len(numeros)
            print(f"Média: {media:.2f}")

    elif opcao == "0":

        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")

        # QUESTÃO 17 - Módulo math

import math

numero = float(input("Digite um número real: ").replace(",", "."))

print("\n===== CÁLCULOS MATEMÁTICOS =====")

# Raiz quadrada
if numero >= 0:
    print(f"Raiz quadrada: {math.sqrt(numero):.2f}")
else:
    print("Raiz quadrada: não existe nos números reais.")

# Valor absoluto
print(f"Valor absoluto: {math.fabs(numero):.2f}")

# Teto
print(f"Arredondamento para cima: {math.ceil(numero)}")

# Piso
print(f"Arredondamento para baixo: {math.floor(numero)}")

# Fatorial
if numero.is_integer() and numero >= 0:
    print(f"Fatorial: {math.factorial(int(numero))}")
else:
    print("Fatorial: disponível somente para inteiros não negativos.")


# QUESTÃO 18 - Simulação de dados

import random

print("===== LANÇAMENTO ÚNICO =====")

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

soma = dado1 + dado2

print(f"Primeiro dado: {dado1}")
print(f"Segundo dado: {dado2}")
print(f"Soma: {soma}")

print("\n===== 10 LANÇAMENTOS =====")

quantidade_soma_7 = 0

for i in range(1, 11):

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    soma = dado1 + dado2

    print(
        f"Lançamento {i}: "
        f"Dado 1 = {dado1}, "
        f"Dado 2 = {dado2}, "
        f"Soma = {soma}"
    )

    if soma == 7:
        quantidade_soma_7 += 1

print(f"\nA soma dos dados foi 7 em {quantidade_soma_7} lançamento(s).")


# QUESTÃO 19 - Análise de frase

frase = input("Digite uma frase: ").strip()

# Remove espaços extras entre as palavras
palavras = frase.split()

# Reconstrói a frase com apenas um espaço entre as palavras
frase_normalizada = " ".join(palavras)

if len(palavras) == 0:
    print("A frase não possui palavras.")
else:

    letra = input("Digite uma letra para pesquisar: ").strip()

    while len(letra) != 1:
        print("Digite somente uma letra.")
        letra = input("Digite uma letra para pesquisar: ").strip()

    quantidade_caracteres = len(frase_normalizada)
    quantidade_palavras = len(palavras)

    primeira_palavra = palavras[0]
    ultima_palavra = palavras[-1]

    ocorrencias = frase_normalizada.lower().count(letra.lower())

    print("\n===== ANÁLISE DA FRASE =====")

    print(f"Frase normalizada: {frase_normalizada}")
    print(f"Quantidade de caracteres: {quantidade_caracteres}")
    print(f"Quantidade de palavras: {quantidade_palavras}")
    print(f"Primeira palavra: {primeira_palavra}")
    print(f"Última palavra: {ultima_palavra}")
    print(f"Ocorrências da letra '{letra}': {ocorrencias}")
    print(f"Maiúsculas: {frase_normalizada.upper()}")
    print(f"Minúsculas: {frase_normalizada.lower()}")

    # ============================================================
# QUESTÃO 20 - SISTEMA COMPLETO DE GERENCIAMENTO ACADÊMICO
# ============================================================

estudantes = []


# ------------------------------------------------------------
# FUNÇÃO PARA LER INTEIROS POSITIVOS
# ------------------------------------------------------------

def ler_inteiro_positivo(mensagem):
    while True:
        try:
            valor = int(input(mensagem))

            if valor > 0:
                return valor

            print("Digite um número inteiro positivo.")

        except ValueError:
            print("Digite um número inteiro válido.")


# ------------------------------------------------------------
# FUNÇÃO PARA LER NOTAS
# ------------------------------------------------------------

def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem).replace(",", "."))

            if 0 <= nota <= 10:
                return nota

            print("A nota deve estar entre 0 e 10.")

        except ValueError:
            print("Digite uma nota válida.")


# ------------------------------------------------------------
# FUNÇÃO PARA CALCULAR MÉDIA
# ------------------------------------------------------------

def calcular_media(notas):
    return sum(notas) / len(notas)


# ------------------------------------------------------------
# FUNÇÃO PARA DETERMINAR SITUAÇÃO
# ------------------------------------------------------------

def determinar_situacao(media):

    if media >= 7:
        return "Aprovado"

    elif media >= 5:
        return "Recuperação"

    else:
        return "Reprovado"


# ------------------------------------------------------------
# FUNÇÃO PARA LOCALIZAR ESTUDANTE
# ------------------------------------------------------------

def buscar_estudante(nome):

    for estudante in estudantes:

        if estudante["nome"].lower() == nome.lower():
            return estudante

    return None


# ------------------------------------------------------------
# CADASTRAR ESTUDANTE
# ------------------------------------------------------------

def cadastrar_estudante():

    print("\n===== CADASTRO DE ESTUDANTE =====")

    nome = input("Nome: ").strip()

    if buscar_estudante(nome) is not None:
        print("Já existe um estudante com esse nome.")
        return

    idade = ler_inteiro_positivo("Idade: ")

    curso = input("Curso: ").strip()

    notas = []

    for i in range(1, 4):
        nota = ler_nota(f"Nota {i}: ")
        notas.append(nota)

    media = calcular_media(notas)
    situacao = determinar_situacao(media)

    estudante = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "notas": notas,
        "media": media,
        "situacao": situacao
    }

    estudantes.append(estudante)

    print("\nEstudante cadastrado com sucesso!")


# ------------------------------------------------------------
# LISTAR ESTUDANTES
# ------------------------------------------------------------

def listar_estudantes():

    print("\n===== LISTA DE ESTUDANTES =====")

    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    for i, estudante in enumerate(estudantes, start=1):

        print(f"\n--- Estudante {i} ---")
        print(f"Nome: {estudante['nome']}")
        print(f"Idade: {estudante['idade']}")
        print(f"Curso: {estudante['curso']}")

        print(
            f"Notas: "
            f"{estudante['notas'][0]:.2f}, "
            f"{estudante['notas'][1]:.2f}, "
            f"{estudante['notas'][2]:.2f}"
        )

        print(f"Média: {estudante['media']:.2f}")
        print(f"Situação: {estudante['situacao']}")


# ------------------------------------------------------------
# CONSULTAR ESTUDANTE
# ------------------------------------------------------------

def consultar_estudante():

    print("\n===== CONSULTA DE ESTUDANTE =====")

    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    nome = input("Digite o nome do estudante: ").strip()

    estudante = buscar_estudante(nome)

    if estudante is None:
        print("Estudante não encontrado.")
        return

    print("\n===== DADOS DO ESTUDANTE =====")

    print(f"Nome: {estudante['nome']}")
    print(f"Idade: {estudante['idade']}")
    print(f"Curso: {estudante['curso']}")

    print(
        f"Nota 1: {estudante['notas'][0]:.2f}\n"
        f"Nota 2: {estudante['notas'][1]:.2f}\n"
        f"Nota 3: {estudante['notas'][2]:.2f}"
    )

    print(f"Média: {estudante['media']:.2f}")
    print(f"Situação: {estudante['situacao']}")


# ------------------------------------------------------------
# ALTERAR DADOS
# ------------------------------------------------------------

def alterar_estudante():

    print("\n===== ALTERAR DADOS =====")

    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    nome_busca = input("Digite o nome do estudante: ").strip()

    estudante = buscar_estudante(nome_busca)

    if estudante is None:
        print("Estudante não encontrado.")
        return

    print("\nDeixe o campo vazio para manter o valor atual.")

    novo_nome = input(
        f"Nome [{estudante['nome']}]: "
    ).strip()

    if novo_nome:
        estudante["nome"] = novo_nome

    nova_idade = input(
        f"Idade [{estudante['idade']}]: "
    ).strip()

    if nova_idade:

        try:
            nova_idade = int(nova_idade)

            if nova_idade > 0:
                estudante["idade"] = nova_idade
            else:
                print("Idade inválida. Valor anterior mantido.")

        except ValueError:
            print("Idade inválida. Valor anterior mantido.")

    novo_curso = input(
        f"Curso [{estudante['curso']}]: "
    ).strip()

    if novo_curso:
        estudante["curso"] = novo_curso

    alterar_notas = input(
        "Deseja alterar as notas? (s/n): "
    ).lower()

    if alterar_notas == "s":

        novas_notas = []

        for i in range(1, 4):
            novas_notas.append(
                ler_nota(f"Nova nota {i}: ")
            )

        estudante["notas"] = novas_notas

        estudante["media"] = calcular_media(novas_notas)

        estudante["situacao"] = determinar_situacao(
            estudante["media"]
        )

    else:

        # Caso o nome ou outros dados tenham mudado,
        # as notas continuam iguais, então a média também.
        estudante["media"] = calcular_media(
            estudante["notas"]
        )

        estudante["situacao"] = determinar_situacao(
            estudante["media"]
        )

    print("Dados alterados com sucesso!")


# ------------------------------------------------------------
# REMOVER ESTUDANTE
# ------------------------------------------------------------

def remover_estudante():

    print("\n===== REMOVER ESTUDANTE =====")

    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    nome = input("Digite o nome do estudante: ").strip()

    estudante = buscar_estudante(nome)

    if estudante is None:
        print("Estudante não encontrado.")
        return

    print(f"\nEstudante encontrado: {estudante['nome']}")

    confirmacao = input(
        "Tem certeza que deseja remover? (s/n): "
    ).lower()

    if confirmacao == "s":

        estudantes.remove(estudante)

        print("Estudante removido com sucesso.")

    else:

        print("Operação cancelada.")


# ------------------------------------------------------------
# RELATÓRIO DA TURMA
# ------------------------------------------------------------

def gerar_relatorio():

    print("\n===== RELATÓRIO DA TURMA =====")

    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    total = len(estudantes)

    soma_medias = 0

    maior_media = estudantes[0]
    menor_media = estudantes[0]

    aprovados = 0
    recuperacao = 0
    reprovados = 0

    for estudante in estudantes:

        media = estudante["media"]

        soma_medias += media

        if media > maior_media["media"]:
            maior_media = estudante

        if media < menor_media["media"]:
            menor_media = estudante

        if media >= 7:
            aprovados += 1

        elif media >= 5:
            recuperacao += 1

        else:
            reprovados += 1

    media_geral = soma_medias / total

    print(f"Total de estudantes: {total}")

    print(
        f"Maior média: "
        f"{maior_media['nome']} - "
        f"{maior_media['media']:.2f}"
    )

    print(
        f"Menor média: "
        f"{menor_media['nome']} - "
        f"{menor_media['media']:.2f}"
    )

    print(f"Média geral da turma: {media_geral:.2f}")

    print(f"Aprovados: {aprovados}")
    print(f"Recuperação: {recuperacao}")
    print(f"Reprovados: {reprovados}")


# ------------------------------------------------------------
# MENU PRINCIPAL
# ------------------------------------------------------------

def menu():

    while True:

        print("\n========================================")
        print("           SISTEMA ACADÊMICO")
        print("========================================")
        print("1 - Cadastrar estudante")
        print("2 - Listar estudantes")
        print("3 - Consultar estudante")
        print("4 - Alterar dados")
        print("5 - Remover estudante")
        print("6 - Gerar relatório da turma")
        print("0 - Encerrar sistema")
        print("========================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            cadastrar_estudante()

        elif opcao == "2":

            listar_estudantes()

        elif opcao == "3":

            consultar_estudante()

        elif opcao == "4":

            alterar_estudante()

        elif opcao == "5":

            remover_estudante()

        elif opcao == "6":

            gerar_relatorio()

        elif opcao == "0":

            print("\nSistema encerrado.")
            break

        else:

            print("Opção inválida. Tente novamente.")


# ------------------------------------------------------------
# INÍCIO DO PROGRAMA
# ------------------------------------------------------------

menu()