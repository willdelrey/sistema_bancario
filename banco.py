import random as rd
import sys
from tabulate import tabulate as tb

def age(idade):
    if idade<18:
        print(f"{nome}, você é menor de idade e não tem acesso")
        sys.exit("saindo...")
def menu_principal(acao):
    if acao==1 or acao==2:
        acao=int(input("o que deseja fazer agora ?\n 1-Ver saldo. \n 2- Sacar. \n 0-Sair."))
        return(acao)
    else:
        return(SystemExit)
print("Banco Will".center(40, "#"))
nome=str.title(input("Qual o seu nome? "))
idade=int(input(f"Olá, {nome}, Seja bem vindo ao banco will\n Qual a sua idade? "))
if idade<18:
    age(idade)
elif idade>=18:
    saldo=rd.uniform(0, 10000)
    acao=int(input(f"seu saldo é R${saldo:.2f}.\nO que deseja fazer?\n 1-Ver extrato. \n 2- Sacar. \n 3-depositar. \n 0-Sair."))
    if acao==1:
        print(f"seu saldo é de R${saldo:.2f}")
        menu_principal(acao)
    elif acao==2:
        print(f"seu saldo é de R${saldo:.2f}")
        saque=float(input("Qual o valor do saque? R$"))
        novo_saldo=(saldo-saque)
        print(f"seu novo saldo é R${novo_saldo:.2f}")
        menu_principal(acao)
    elif acao==3:
        print(f"seu saldo é de R${saldo:.2f}")
        saque=float(input("Qual o valor do depósito? R$"))
        novo_saldo=(saldo + saque)
        print(f"seu novo saldo é R${novo_saldo:.2f}")
        menu_principal(acao)
    else:
        print("opção inválida")
        sys.exit("saindo...")