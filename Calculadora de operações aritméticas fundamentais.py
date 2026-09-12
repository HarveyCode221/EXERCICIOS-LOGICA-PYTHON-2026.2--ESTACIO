def principal():
    print("Bem vindo a calculadora, digite um número.")
    numero1 = float(input('Digite o primeiro número'))
    numero2 = float(input('Digite o segundo número'))

    if numero2 == 0:
        print("Divisão por 0 não permitida")
        print(f"A adição é {numero1 + numero2} \nA subtração é {numero1 - numero2} \nA multiplicação é {numero1 * numero2} \nA potenciação é {numero1 ** numero2}")

    else:
        print(f"A adição é {numero1 + numero2} \nA subtração é {numero1 - numero2} \nA multiplicação é {numero1 * numero2} \nA divisão é {numero1 / numero2} \nA divisão inteira é {numero1 // numero2} \nO resto da divisão é {numero1 % numero2} \nA potenciação é {numero1 ** numero2}")

principal()