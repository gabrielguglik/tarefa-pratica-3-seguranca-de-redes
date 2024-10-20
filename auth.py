import pyotp
import qrcode

def gerar_qr_code(celular):
    # gerando chave secreta e código TOTP
    chave_secreta = pyotp.random_base32()
    totp = pyotp.TOTP(chave_secreta)

    # gerando URI do QR Code
    qr_data = totp.provisioning_uri(celular, issuer_name="iFood Simulação")

    # gerando e exibindo o QR Code
    qr = qrcode.make(qr_data)
    qr.save("qrcode.png")  # usando pillow para salvar a imagem

    return totp, chave_secreta

def verificar_codigo_totp(totp, codigo):
    # verificando se o código inserido é válido
    return totp.verify(codigo)