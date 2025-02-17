# Função para imprimir uma mensagem
def welcome ():
    print("Bem vindo ao sistema de filmes!")

def calculate_average():
    num_ratings = int(input("Digite quantas avaliaçoes deseja fazer pro filme:\n"))
    total = 0
    for i in range (num_ratings):
        note = float(input("Digite a nota para o filme:\n"))
        total += note