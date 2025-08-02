'''Descrição
Este script coleta e analisa as notas finais de 7 alunos, classificando cada um como aprovado ou reprovado, com base na seguinte regra:

Alunos com nota maior ou igual a 7 são aprovados.
Alunos com nota inferior a 7 são reprovados.

Durante a execução, o programa:
Solicita a nota de cada aluno por meio de um laço for,
Utiliza variáveis e vai contando quantos alunos foram aprovados e reprovados,
Soma as notas apenas dos alunos aprovados, a fim de calcular posteriormente a média.

Ao final:
Exibe a quantidade total de aprovados e reprovados,
Caso tenha pelo menos um aprovado, calcula e apresenta a média das notas dos aprovados,
Se nenhum aluno tiver sido aprovado, o programa informa que não houve nenhum aprovado.'''

quantidadeAprovados = 0
somaAprovados = 0
quantidadeReprovado = 0

for nota in range(1, 8):
    notasAlunos = float(input(f'{nota} - Qual é a sua nota final? '))

    if notasAlunos >= 7:
        quantidadeAprovados += 1
        somaAprovados += notasAlunos
    else:
        quantidadeReprovado += 1

print(f'\n{quantidadeAprovados} aluno(s) foram aprovados.')
print(f'{quantidadeReprovado} aluno(s) foram reprovados.')

if quantidadeAprovados > 0:
    media = somaAprovados / quantidadeAprovados
    print(f'A média das notas dos aprovados é: {media:.2f}')
else:
    print('Não houve nenhum aprovado.')

