# Solicita ao usuário que informe uma string
texto = input("Digite uma string: ")

# Converte a string para minúsculas e conta a ocorrência da letra 'a'
ocorrencias_a = texto.lower().count('a')

# Verifica se existe a letra 'a' na string
if ocorrencias_a > 0:
    print(f"A letra 'a' aparece {ocorrencias_a} vezes na string.")
else:
    print("A letra 'a' não foi encontrada na string.")
