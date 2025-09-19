senhaSecreta = 'etinho'
letras_acertadas = ''
numero_tentativas = 0
numero_erros = 0

while True:
  letra_digitada = input('Digite apenas uma letra ')
  numero_tentativas += 1

  if len(letra_digitada) > 1:
      print("Digite apenas uma letra!")
      continue

  if letra_digitada not in senhaSecreta: # Corrected line
    numero_erros += 1

  if letra_digitada in senhaSecreta:
   letras_acertadas += letra_digitada

  for letra_secreta in senhaSecreta:
   if letra_secreta in letras_acertadas:
     print(letra_secreta)
   else:
     print('*')

  if letras_acertadas == senhaSecreta:
    print(f'Parabéns você acertou a Senha Secreta!!!')
    break

print(f'Senha secreta: {senhaSecreta}')
print(f'Número de tentativas: {numero_tentativas}')
print(f'erros: {numero_erros}')
