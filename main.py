from auth import gerar_qr_code
from client.encrypt_message import cifrar_mensagem
from client.encrypt_receipt import cifrar_comprovante
from crypto import derivar_chave_sessao, derivar_iv
from server.decrypt_receipt import decifrar_comprovante
from server.decrypt_message import decifrar_mensagem
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

    # Derivando chave de sessão e salt
    chave_sessao, salt = derivar_chave_sessao(codigo)

    # Derivando o IV para o comprovante usando o código TOTP e salt
    iv_comprovante = derivar_iv(codigo, salt)

    # Cifrando comprovante de pagamento
    comprovante = b"Comprovante de pagamento"
    comprovante_cifrado = cifrar_comprovante(chave_sessao, comprovante, iv_comprovante)

    # Decifrando comprovante no sistema
    comprovante_decifrado = decifrar_comprovante(chave_sessao, iv_comprovante, comprovante_cifrado)
    print(f"Comprovante decifrado: {comprovante_decifrado.decode()}")

    # Enviando pedido para o restaurante
    if enviar_pedido_restaurante(prato_escolhido):
        print("Calculando horário de chegada...")

    # Calculando a hora de chegada
    hora_chegada = calcular_horario_chegada(prato_escolhido)

    # Derivando o IV para a mensagem usando o código TOTP e salt
    iv_mensagem = derivar_iv(codigo, salt)

    # Enviando mensagem cifrada
    mensagem = f"Hora de chegada do pedido: {hora_chegada}".encode()
    mensagem_cifrada = cifrar_mensagem(chave_sessao, mensagem, iv_mensagem)

    # Decifrando mensagem no usuário
    mensagem_decifrada = decifrar_mensagem(chave_sessao, iv_mensagem, mensagem_cifrada)
    print(f"Mensagem decifrada: {mensagem_decifrada.decode()}")

if __name__ == "__main__":
    main()
