
def menu():
    print("Insira uma temperatura expressa em graus para converter pra Fahrenheit e Kelvin.\n")
    temperaturacelsius = float(input('Temperatura em celsius: '))
    calculo(temperaturacelsius)

def calculo(tcelcius: float):
    fahrenheit = tcelcius * 9/5 + 32
    kelvin = tcelcius + 273.15

    print(f"A temperatura dada foi {tcelcius}ºC \nA temperatura para fahreinte é: {fahrenheit:.2f}ºF \nA temperatura para kelvin é: {kelvin:.2f}ºK")

menu()