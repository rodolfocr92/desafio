
io = float(input("Insira sua idade atual: "))
ia = float(input("Insira a idade que deseja sacar o investimento: "))
vf = float(input("Insira o montante final do investimento: "))
i = float(input("Insira a taxa de juros mensais em número decimal: "))

meses = (ia - io)*12

dep = (vf*i)/((1+i)**meses - 1)
depr = round(dep, 2)
print("Valor do depósito mensal: R$" + str(depr))



