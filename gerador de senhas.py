import random
import string


def gerar_senha(comprimento, incluir_numeros=False, incluir_letras_maiusculas=False, incluir_letras_minusculas=False,
                incluir_caracteres_especiais=False):
    caracteres = ''

    if incluir_numeros:
        caracteres += string.digits
    if incluir_letras_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_letras_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_caracteres_especiais:
        caracteres += string.punctuation

    if not caracteres:
        print("Erro: Nenhum critério selecionado para gerar a senha.")
        return

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha


# Teste 01
senha_teste_01 = gerar_senha(8, incluir_numeros=True, incluir_caracteres_especiais=True)
print("Teste 01:", senha_teste_01)

# Teste 02
senha_teste_02 = gerar_senha(12, incluir_numeros=True)
print("Teste 02:", senha_teste_02)

# Teste 03
senha_teste_03 = gerar_senha(16, incluir_letras_maiusculas=True, incluir_numeros=True)
print("Teste 03:", senha_teste_03)

# Teste 04
senha_teste_04 = gerar_senha(20, incluir_letras_minusculas=True, incluir_numeros=True,
                             incluir_caracteres_especiais=True)
print("Teste 04:", senha_teste_04)

# Teste 05
senha_teste_05 = gerar_senha(6, incluir_letras_maiusculas=True, incluir_letras_minusculas=True, incluir_numeros=True,
                             incluir_caracteres_especiais=True)
print("Teste 05:", senha_teste_05)
