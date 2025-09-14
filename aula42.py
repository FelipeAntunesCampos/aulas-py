frase = 'Python é uma linguagem de programação interpretada, de alto nível e de código aberto, conhecida pela sua simplicidade, versatilidade e legibilidade, o que a torna ideal tanto para iniciantes quanto para profissionais. Desenvolvida por Guido van Rossum no final dos anos 80, é utilizada numa vasta gama de áreas, incluindo desenvolvimento web, ciência de dados, inteligência artificial (IA), Machine Learning (ML), automação de tarefas e muito mais.'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apreceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)
    
    if letra_atual == ' ':
        i += 1
        continue

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apreceu_mais_vezes = letra_atual


    i += 1

print('A letra que apareceu mais vezes foi 'f'"{letra_apreceu_mais_vezes}" que apareceu 'f'{qtd_apareceu_mais_vezes}x')
