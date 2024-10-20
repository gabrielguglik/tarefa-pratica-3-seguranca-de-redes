from auth import gerar_qr_code, verificar_codigo_totp
from crypto_utils import derivar_chave_sessao, cifrar_comprovante, decifrar_comprovante, cifrar_mensagem, decifrar_mensagem
import os

def escolher_prato():
    pratos = ["Pizza", "Sushi", "Hambúrguer", "Salada"]
    for idx, prato in enumerate(pratos, 1):
        print(f"{idx}. {prato}")
    escolha = int(input("Escolha seu prato (número): ")) - 1
    return pratos[escolha]

def main():
    # Passo 1: Escolher prato
    prato_escolhido = escolher_prato()
    print(f"Você escolheu: {prato_escolhido}")

    # Passo 2: Pedir celular
    celular = input("Digite o número do seu celular: ")

    # Passo 3: Gerar TOTP e QR Code
    totp, chave_secreta = gerar_qr_code(celular)

    # Passo 4: Verificar código inserido pelo usuário
    codigo = input("Digite o código TOTP: ")
    if verificar_codigo_totp(totp, codigo):
        print("Código TOTP válido!")

        # Passo 6: Derivar chave de sessão
        chave_sessao = derivar_chave_sessao(codigo)

        # Passo 7: Cifrar comprovante de pagamento
        comprovante = b"Comprovante de pagamento"
        nonce, comprovante_cifrado = cifrar_comprovante(chave_sessao, comprovante)

        # Passo 8: Decifrar comprovante no sistema
        comprovante_decifrado = decifrar_comprovante(chave_sessao, nonce, comprovante_cifrado)
        print(f"Comprovante decifrado: {comprovante_decifrado.decode()}")

        # Passo 9: Enviar mensagem cifrada
        mensagem = b"O pedido chegara as 19:30"
        nonce, mensagem_cifrada = cifrar_mensagem(chave_sessao, mensagem)

        # Passo 10: Decifrar mensagem no usuário
        mensagem_decifrada = decifrar_mensagem(chave_sessao, nonce, mensagem_cifrada)
        print(f"Mensagem decifrada: {mensagem_decifrada.decode()}")
    else:
        print("Código inválido!")


if __name__ == "__main__":
    main()
