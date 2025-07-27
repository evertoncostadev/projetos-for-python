'''Descrição:
Este programa solicita ao usuário a idade de 7 pessoas, uma por uma, e classifica cada uma delas em uma das seguintes faixas etárias:
   
    - Criança:      de 0 a 12 anos
    - Adolescente:  de 13 a 17 anos
    - Adulto:       de 18 a 59 anos
    - Idoso:        60 anos ou mais

O programa utiliza a estrutura de repetição `for` para percorrer o número de pessoas, e `while` com 
`break` para validar a entrada de dados, garantindo que o usuário digite uma idade válida (um número inteiro positivo).

Ao final, o programa exibe a quantidade de pessoas em cada faixa etária, desde que tenha pelo menos uma em cada categoria.
O bejetivo é relembrar e arquivar esses projetos publicamente e ao mesmo tempo  praticar as estruturas de repetição `for` e `while`, o uso de `break` para controle de fluxo, e o uso de 
 condicionais (`if`, `elif`) em Python. Também desenvolve lógica de classificação e validação de dados inseridos pelo usuário.'''


def classificar_faixas_etarias(quantidade):
    criancas = adolescentes = adultos = idosos = 0

    for i in range(1, quantidade + 1):
        while True:
            try:
                idade = int(input(f'Digite a idade da {i}ª pessoa: '))
                break
            except ValueError:
                print('Por favor, digite uma idade válida.')

        if idade <= 12:
            criancas += 1
        elif 13 <= idade <= 17:
            adolescentes += 1
        elif 18 <= idade <= 59:
            adultos += 1
        else:
            idosos += 1

    if criancas: print(f'{criancas} criança(s).')
    if adolescentes: print(f'{adolescentes} adolescente(s).')
    if adultos: print(f'{adultos} adulto(s).')
    if idosos: print(f'{idosos} idoso(s).')
        
classificar_faixas_etarias(7)
