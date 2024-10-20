import pyotp
import qrcode

def gerar_qr_code(celular):
    # Gerar chave secreta e código TOTP
    chave_secreta = pyotp.random_base32()
    totp = pyotp.TOTP(chave_secreta)

    # Gerar URI do QR Code
    qr_data = totp.provisioning_uri(celular, issuer_name="iFood Simulação")

    # Gerar e exibir o QR Code
    qr = qrcode.make(qr_data)
    qr.save("qrcode.png")  # Pillow será responsável por salvar a imagem

    return totp, chave_secreta

def verificar_codigo_totp(totp, codigo):
    # Verificar se o código inserido é válido
    return totp.verify(codigo)