# estruturas_repeticao1.py
# Microatividade 3 – Estrutura de repetição while
# Autora: Môfi

# Variável inicial (string vazia)
entrada_idade = ''

# Enquanto o valor for diferente de '0', o laço continua
while str(entrada_idade) != '0':
    # Solicita uma entrada do usuário
    entrada_idade = input("Digite um número qualquer ou 0 para sair: ")

    # Exibe o valor digitado
    print("Número digitado:", entrada_idade)

print("Programa encerrado.")
