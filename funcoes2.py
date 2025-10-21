# funcoes2.py
# Microatividade 6 – Utilização de argumentos em funções
# Autora: Môfi

# Definição da função com parâmetro
def loginUsuario(perfil):
    # Converte o valor recebido para minúsculas para evitar erro de digitação
    if perfil.lower() == 'admin':
        print("Bem-vindo, Administrador.")
    else:
        print("Bem-vindo, Usuário.")

# Chamadas da função com diferentes argumentos
loginUsuario("Admin")
loginUsuario("admin")
loginUsuario("User")
loginUsuario("usuário")
