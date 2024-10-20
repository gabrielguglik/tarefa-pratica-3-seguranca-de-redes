from auth import gerar_qr_code, verificar_codigo_totp
from crypto_utils import derivar_chave_sessao, cifrar_comprovante, decifrar_comprovante, cifrar_mensagem, decifrar_mensagem
import os

def escolher_prato():
    print("Escolha um prato de comida:")
    pratos = ["Pizza", "Sushi", "Hambúrguer", "Salada"]
    for idx, prato in enumerate(pratos, 1):
        print(f"{idx}. {prato}")
    escolha = int(input("Escolha seu prato (número): ")) - 1
    return pratos[escolha]

def main():
    # escolhendo o prato
    prato_escolhido = escolher_prato()
    print(f"Você escolheu: {prato_escolhido}")

    # informando o numero de celular
    celular = input("Digite o número do seu celular: ")

    # gerando TOTP e QR Code
    totp, chave_secreta = gerar_qr_code(celular)

    # verificando o código inserido
    codigo = input("Digite o código TOTP: ")
    if verificar_codigo_totp(totp, codigo):
        print("Código TOTP válido!")

        # devirando chave de sessão
        chave_sessao = derivar_chave_sessao(codigo)

        # cifrando comprovante de pagamento
        comprovante = b"Comprovante de pagamento"
        nonce, comprovante_cifrado = cifrar_comprovante(chave_sessao, comprovante)

        # decifrando comprovante no sistema
        comprovante_decifrado = decifrar_comprovante(chave_sessao, nonce, comprovante_cifrado)
        print(f"Comprovante decifrado: {comprovante_decifrado.decode()}")

        # enviando mensagem cifrada
        mensagem = b"Hora de chegada do pedido: 19:30h"
        nonce, mensagem_cifrada = cifrar_mensagem(chave_sessao, mensagem)

        # decifrando mensagem no usuário
        mensagem_decifrada = decifrar_mensagem(chave_sessao, nonce, mensagem_cifrada)
        print(f"Mensagem decifrada: {mensagem_decifrada.decode()}")
    else:
        print("Código inválido!")


if __name__ == "__main__":
    main()
