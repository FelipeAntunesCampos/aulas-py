def calculo():
  print("Selecione a operação:")
  print("1. Adição")
  print("2. Subtração")
  print("3. Multiplicação")
  print("4. Divisão")

calculo();

escolha = input("Digite sua escolha (1/2/3/4): ")

valor1 = float(input("Digite o valor desejado "))
valor2 = float(input("Digite o segundo valor "))


if escolha == '1':
    resultado = valor1 + valor2
    print(resultado)
elif escolha =='2':
    resultado = valor1 + valor2 
    print(resultado)
elif escolha =='3':
    resultado = valor1 + valor2 
    print(resultado)
elif escolha =='4':
    resultado = valor1 + valor2 
    print(resultado)
else: 
    print('Você deve selecionar alguma operação') 
