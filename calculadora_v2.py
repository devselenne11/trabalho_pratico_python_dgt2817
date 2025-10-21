# calculadora_v2.py
# Trabalho Prático – Refatoração da Calculadora
# Requisitos: funções (adição, subtração, multiplicação, divisão com guarda),
# estrutura condicional (if/elif/else) e laço while controlando a saída (S/N).

# 1) Variável de controle da aplicação
saida = ''  # continuará no laço enquanto não for 'n' ou 'N'


# 2) Funções aritméticas
def adicao(a, b):
    """Retorna a soma de a e b."""
    return a + b


def subracao(a, b):
    """Retorna a subtração de a por b."""
    return a - b


def multiplicacao(a, b):
    """Retorna o produto entre a e b."""
    return a * b


def divisao(a, b):
    """
    Retorna a divisão de a por b.
    Se o divisor for 0, retorna a mensagem de erro solicitada.
    (Tecnicamente só o divisor 0 inviabiliza a operação — tratamos esse caso.)
    """
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a / b


# 3) Função calculadora (decide qual operação executar)
def calculadora(num1, num2, operacao):
    """
    Recebe (num1, num2, operacao) e executa a operação solicitada.
    'operacao' pode ser o símbolo (+, -, *, /) ou o nome ('adicao', 'subracao', 'multiplicacao', 'divisao').
    Retorna o resultado numérico OU uma string de erro, dependendo da operação.
    """
    op = operacao.strip().lower()

    # Aceita tanto símbolos quanto nomes
    if op in ('+', 'adicao', 'adição'):
        resultado = adicao(num1, num2)
    elif op in ('-', 'subracao', 'subtração', 'subtracao'):
        resultado = subracao(num1, num2)
    elif op in ('*', 'x', 'multiplicacao', 'multiplicação', 'vezes'):
        resultado = multiplicacao(num1, num2)
    elif op in ('/', 'divisao', 'divisão'):
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida. Use +, -, *, / ou os nomes: adicao, subracao, multiplicacao, divisao."

    return resultado


# 4) Loop principal (continua até a usuária responder N/n)
while str(saida).strip().lower() != 'n':
    # Coleta segura dos números (garante que sejam válidos)
    while True:
        try:
            num1 = float(input("Digite o primeiro número: ").replace(',', '.'))
            break
        except ValueError:
            print("Entrada inválida. Digite um número válido (ex.: 10, 3.5).")

    while True:
        try:
            num2 = float(input("Digite o segundo número: ").replace(',', '.'))
            break
        except ValueError:
            print("Entrada inválida. Digite um número válido (ex.: 10, 3.5).")

    # Operação
    print("\nEscolha a operação:")
    print("  +  (ou 'adicao')")
    print("  -  (ou 'subracao')")
    print("  *  (ou 'multiplicacao')")
    print("  /  (ou 'divisao')")

    operacao = input("Operação desejada: ")

    # Chamada da função calculadora
    resultado = calculadora(num1, num2, operacao)

    # Exibição do resultado
    print("\nResultado da operação:", resultado)

    # Pergunta de continuidade (S/N)
    # Dica ao usuário para evitar ambiguidade
    saida = input("\nDeseja realizar outra operação? (S/N): ")
    print()  # linha em branco para legibilidade

print("Aplicativo encerrado. Obrigada por utilizar a calculadora!")
