from auth import gerar_qr_code
from crypto import derivar_chave_sessao, cifrar_comprovante, decifrar_comprovante, cifrar_mensagem, decifrar_mensagem
from utils import calcular_horario_chegada, enviar_pedido_restaurante, escolher_prato, solicitar_codigo_totp


def main():
    # Escolhendo o prato
    prato_escolhido = escolher_prato()
    print(f"Você escolheu: {prato_escolhido}")

    # Informando o número de celular
    celular = input("Digite o número do seu celular: ")

    # Gerando TOTP e QR Code
    totp, chave_secreta = gerar_qr_code(celular)

    # Solicitando e validando o código TOTP
    codigo = solicitar_codigo_totp(totp)

    # Derivando chave de sessão
    chave_sessao = derivar_chave_sessao(codigo)

    # Cifrando comprovante de pagamento
    comprovante = b"Comprovante de pagamento"
    nonce, comprovante_cifrado = cifrar_comprovante(chave_sessao, comprovante)

    # Decifrando comprovante no sistema
    comprovante_decifrado = decifrar_comprovante(chave_sessao, nonce, comprovante_cifrado)
    print(f"Comprovante decifrado: {comprovante_decifrado.decode()}")

    # Enviando pedido para o restaurante
    if enviar_pedido_restaurante(prato_escolhido):
        print("Calculando horário de chegada...")

    # Calculando a hora de chegada
    hora_chegada = calcular_horario_chegada(prato_escolhido)

    # Enviando mensagem cifrada
    mensagem = f"Hora de chegada do pedido: {hora_chegada}".encode()
    nonce, mensagem_cifrada = cifrar_mensagem(chave_sessao, mensagem)

    # Decifrando mensagem no usuário
    mensagem_decifrada = decifrar_mensagem(chave_sessao, nonce, mensagem_cifrada)
    print(f"Mensagem decifrada: {mensagem_decifrada.decode()}")


if __name__ == "__main__":
    main()
