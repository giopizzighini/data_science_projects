print("**************** CALCULADORA PYTHON ********************")
print("")
print("Escolha uma opção: \n1 - Soma \n2 - Subtração \n3 - Divisão \n4 - Multiplicação")
x = int(input("\nDigite: "))
a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))

def soma(a,b):
    return a+b
def sub(a,b):
    return(a-b)
def div(a,b):
    return (a/b)
def mult(a,b):
    return (a*b)

if x == 1:
    print("\nO resultado é", soma(a,b))
elif x == 2:
    print("\nO resultado é", sub(a,b))
elif x == 3:
    print("\nO resultado é", div(a,b))
elif x == 4:
    print("\nO resultado é", mult(a,b))
else:
    print("Numero errado! Digite um número entre 1 e 4!")





