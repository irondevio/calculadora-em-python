# calculadora.py - versão brasileira, meio bagunçada mas funciona

def mostrar_menu():
    print("\n=== CALCULADORA === ")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "nao da pra dividir por zero amigao"
    return a / b

while True:
    mostrar_menu()
    opcao = input("escolhe uma opcao ai: ")
    
    if opcao == "5":
        print("falou")
        break
    
    if opcao not in ["1", "2", "3", "4"]:
        print("opcao invalida carai")
        continue
    
    try:
        num1 = float(input("primeiro numero: "))
        num2 = float(input("segundo numero: "))
    except:
        print("numero invalido, coloca numero direito")
        continue
    
    if opcao == "1":
        print(f"resultado: {somar(num1, num2)}")
    elif opcao == "2":
        print(f"resultado: {subtrair(num1, num2)}")
    elif opcao == "3":
        print(f"resultado: {multiplicar(num1, num2)}")
    elif opcao == "4":
        print(f"resultado: {dividir(num1, num2)}")
