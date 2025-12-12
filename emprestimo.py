"""
Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:

O valor da renda mensal precisa ser maior que R$ 2.000,00.
O valor da parcela não pode ultrapassar 30% da renda.
Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada. O programa deve informar se o empréstimo foi 
aprovado ou negado com base nas condições acima.
"""
nome = input("Qual o seu nome?")
renda = float(input(f"Qual sua renda mensal {nome}? "))
valor = float(input(f"Qual o valor da parcela desejado {nome}? "))


if renda > 2000 and valor <= renda*0.3:
    print(f"Seu empréstimo foi aprovado {nome}")
elif renda <=2000:
    print(f"Seu empréstimo não foi aprovado. Renda insuficiente {nome}")
else:
    print(f"Seu empéstimo não foi aprovado. Parcela acima de 30% da renda {nome}")






