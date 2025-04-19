#Dicionarios com nomes associados
nomes = {185465454655: "Ana",
    879846551356: "João",
    321323213546: "Maria",
    132513213213: "Carlos",
    202300513218: "Beatriz",
    202312345645: "Lucas",
    202304171017: "Hayner"}

# Função para buscar o nome
def buscar_nome(numero):
    if numero in nomes:
        return nomes[numero]
    else:
        return "Número não encontrado!"

# Receber número do usuário
numero_usuario = int(input("Digite o número para buscar seu nome: "))

# Exibir o nome
nome = buscar_nome(numero_usuario)
print(f"Seu nome é: {nome}")

