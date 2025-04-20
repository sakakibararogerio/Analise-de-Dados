print("\n******************* Calculadora em Python *******************\n")

print("Selecione a opção desejada:\n")

print("1 - Soma ")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão\n")

opcao = int(input("Digite sua opção(1/2/3/4): "))

n1 = int(input("Digite o primeiro número: "))

n2 = int(input("Digite o segundo número: "))

def soma(n1, n2):
    resultado = n1 + n2
    print ("%s + %s = %s" %(n1, n2, resultado))

def subtracao(n1, n2):
    resultado = n1 - n2
    print ("%s - %s = %s" %(n1, n2, resultado))

def multiplicacao(n1, n2):
    resultado = n1 * n2
    print ("%s * %s = %s" %(n1, n2, resultado))

def divisao(n1, n2):
    if (n2 == 0):
        print("Não é possível dividir por zero")
        
    else:
        resultado = n1 / n2
        print ("%s / %s = %s" %(n1, n2, resultado))


if opcao == 1:
   soma(n1, n2)
elif opcao == 2:
    subtracao(n1, n2)
elif opcao == 3:
    multiplicacao(n1, n2)
elif opcao == 4:
    divisao(n1, n2)