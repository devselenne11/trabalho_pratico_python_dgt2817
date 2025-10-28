# estruturas_condicao2.py
# Microatividade 2 – Estrutura condicional if, elif e else
# Autora: Môfi

# Atribuindo o valor inicial à variável tempoExperiencia
tempoExperiencia = 3

# Estrutura condicional para verificar o nível de conhecimento
if tempoExperiencia < 2:
    print("Nível de conhecimento júnior.")
elif tempoExperiencia > 2 and tempoExperiencia < 5:
    print("Nível de conhecimento pleno.")
else:
    print("Nível de conhecimento sênior.")