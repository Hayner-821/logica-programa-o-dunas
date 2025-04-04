#entrada de notas
nota1 = float(input('Digite a primeira nota: '))    
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

#Cauculo da media de notas
media = (nota1 + nota2) / 2

print(f'A média é: {media}')
if media >= 6:
    print('Aprovado')
elif media >= 8:
    print('Aprovado com louvor')
elif media >= 5:
    print('Aprovado com recuperação')
elif media <= 4:
    print('repetiu')
else:
    print('Reprovado, estude mais filho!')
print('Fim do programa')


