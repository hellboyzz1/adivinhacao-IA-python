"""12/04/2026"""
import random

numero_secreto = random.randint(1, 100)
tentativas = 0
acertou = False

print("Bem vindo ao meu jogo.")
print("Tente adivinhar o numero em que pensei. ")

#pedir um loop para o usuario tentar adivinhar.

while not acertou:
    try:
     palpite = int(input("\n Qual o seu palpite?: "))
     tentativas += 1
     if palpite == numero_secreto:
        print(f"Parabens, você acertou!, o numero era: {numero_secreto}")
        print(f"Você fez {tentativas} tentativas.")
        acertou = True

     elif palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
     else:
        print("Muito alto! Tente novamente.")
    except ValueError:
     print("Por favor, Digite um numero inteiro valido.")