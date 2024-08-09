nota1 : float
nota2 : float
media : float

nota1 = float(input('Digite a nota 1 ...'))
nota2 = float(input('Digite a nota 2 ...'))

media = (nota1 + nota2) / 2

if media > 5 :
    print('Aprovado!')
elif media > 3 and media < 5 :
    print('Recuperação')
else :
    print('Reprovado!')

print('A média é...', media)