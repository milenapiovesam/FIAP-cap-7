
anos = float(input("Há quantos anos você fuma? "))
valorMaco = float(input("Qual o valor altual do maço de cigarro? "))
macosDia = float(input("Qual a média de maços que você costuma fumar em um dia? "))


montante = macosDia * valorMaco * 365 * anos 

if (montante > 50000):
    print (f"Com o valor R${montante:.2f}, você poderia ter comprado um carro zero.")
elif (montante >= 20000): 
    print (f"Com o valor R${montante:.2f}, você poderia ter comprado um carro popular usado.")
else:
    print (f"Com o valor de R${montante:.2f}, você poderia ter dado entrada em um carro.")
