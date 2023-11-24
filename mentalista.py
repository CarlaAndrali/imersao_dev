import random

def jogo_adivinhacao():
    numero_secreto = random.randint(0, 1000)
    tentativas = 0

    while True:
        tentativa = input("Digite o valor do seu chute (ou 'sair' para encerrar): ")

        if tentativa.lower() == 'sair':
            print("Você desistiu. O número secreto era:", numero_secreto)
            break

        try:
            chute = int(tentativa)
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        tentativas += 1

        if chute == numero_secreto:
            print(f"Parabéns!! Você acertou em {tentativas} tentativa(s) ❤")
            break
        elif chute > 1000 or chute < 0:
            print("ERRO! Você deve digitar um número de 0 a 1000!")
        elif chute > numero_secreto:
            print("Errou! Tente novamente... Dica: o número secreto é menor 😎")
        elif chute < numero_secreto:
            print("Errou! Aqui vai uma dica: o número secreto é maior 😉")

# Iniciar o jogo
jogo_adivinhacao()
