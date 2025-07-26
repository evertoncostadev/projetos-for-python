'''Descrição:
A empresa XYZ percebeu que muitos funcionários estão usando senhas fracas, o que pode colocar em risco a segurança das informações corporativas. Para evitar problemas, a equipe de TI desenvolveu este programa em Python para verificar o nível de segurança das senhas usadas pelos colaboradores.

O programa analisa uma lista de senhas e classifica cada uma delas como Fraca, Média ou Forte, com base em critérios comuns de segurança:

Tamanho mínimo (8 caracteres ou mais)

Presença de letras minúsculas

Presença de letras maiúsculas

Presença de números

Presença de caracteres especiais (ex: !@#$%)

Cada critério atendido soma pontos para a senha, e a soma define sua classificação.

Para isso, o programa utiliza:

Função para organizar e reutilizar a lógica de verificação

Expressões regulares (re) para detectar padrões específicos na senha

Estruturas condicionais (if e elif) para aplicar as regras de avaliação

Laço de repetição (for) para percorrer todas as senhas da lista

No final, o sistema imprime a classificação de cada senha, ajudando a equipe a identificar quais precisam ser reforçadas.'''

import re

def verificar_forca_senha(senha):
    pontos = 0
    
    if len(senha) >= 8:
        pontos += 1
    if re.search(r'[a-z]', senha):
        pontos += 1
    if re.search(r'[A-Z]', senha):
        pontos += 1
    if re.search(r'[0-9]', senha):
        pontos += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
        pontos += 1
    
    if pontos <= 2:
        return "Fraca"
    elif pontos == 3 or pontos == 4:
        return "Média"
    else:
        return "Forte"

senhas = ['1234', 'abc123', 'senha2025', 'oi', 'supersegura!']

for senha in senhas:
    status = verificar_forca_senha(senha)
    print(f'A senha ({senha}) é {status}.')
    
