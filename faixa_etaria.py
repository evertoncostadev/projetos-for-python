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

# Exemplo de uso:
classificar_faixas_etarias(7)
