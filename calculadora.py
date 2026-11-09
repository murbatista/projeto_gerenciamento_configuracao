# Projeto: Sistema de Calculadora
# Aula: Gerenciamento de Configuração

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Não é possível dividir por zero."
    return a / b

print("=== CALCULADORA ===")
print("Soma:", somar(10, 5))
print("Subtração:", subtrair(10, 5))
print("Multiplicação:", multiplicar(10, 5))
print("Divisão:", dividir(10, 5))
print("Atualização realizada para a aula prática de Gerenciamento de Configuração.")
