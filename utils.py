from auth import verificar_codigo_totp
from datetime import datetime, timedelta
from datetime import datetime, timedelta


def escolher_prato():
    pratos = ["Pizza", "Sushi", "Hambúrguer", "Salada"]
    while True:
        print("Escolha um prato de comida:")
        for idx, prato in enumerate(pratos, 1):
            print(f"{idx}. {prato}")
        try:
            escolha = int(input("Escolha seu prato (número): ")) - 1
            if escolha < 0 or escolha >= len(pratos):
                raise ValueError("Escolha inválida. Tente novamente.")
            return pratos[escolha]
        except (ValueError, IndexError):
            print("Opção inválida! Por favor, escolha um número válido.")


def enviar_pedido_restaurante(prato):
    print(f"Pedido de {prato} enviado para o restaurante.")
    return True


def calcular_horario_chegada(prato):
    tempo_atual = datetime.now()
    if prato == "Pizza":
        tempo_extra = timedelta(minutes=30)
    elif prato == "Sushi":
        tempo_extra = timedelta(minutes=40)
    elif prato == "Hambúrguer":
        tempo_extra = timedelta(minutes=25)
    elif prato == "Salada":
        tempo_extra = timedelta(minutes=20)
    else:
        tempo_extra = timedelta(minutes=60)  # valor padrão

    hora_chegada = tempo_atual + tempo_extra
    return hora_chegada.strftime("%H:%M")


def solicitar_codigo_totp(totp):
    while True:
        codigo = input("Digite o código TOTP: ")
        if verificar_codigo_totp(totp, codigo):
            print("Código TOTP válido!")
            return codigo
        else:
            print("Código inválido! Tente novamente.")

