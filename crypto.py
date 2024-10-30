import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# derivando chave de sessão usando PBKDF2
def derivar_chave_sessao(codigo_totp):
    password = codigo_totp.encode()  # usandp o código TOTP como senha
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    chave_sessao = kdf.derive(password)
    return chave_sessao, salt  # Retornar o salt para o IV

# derivando o IV a partir do código TOTP e do salt
def derivar_iv(codigo_totp, salt):
    iv_kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=12,  # tamanho do nonce/IV para AES-GCM
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    iv = iv_kdf.derive(codigo_totp.encode())
    return iv

# cifrando o comprovante usando AES-GCM
def cifrar_comprovante(chave_sessao, comprovante, iv):
    aesgcm = AESGCM(chave_sessao)
    comprovante_cifrado = aesgcm.encrypt(iv, comprovante, None)
    return comprovante_cifrado

# decifrando o comprovante usando AES-GCM
def decifrar_comprovante(chave_sessao, iv, comprovante_cifrado):
    aesgcm = AESGCM(chave_sessao)
    comprovante_decifrado = aesgcm.decrypt(iv, comprovante_cifrado, None)
    return comprovante_decifrado

def cifrar_mensagem(chave_sessao, mensagem, iv):
    aesgcm = AESGCM(chave_sessao)
    mensagem_cifrada = aesgcm.encrypt(iv, mensagem, None)
    return mensagem_cifrada

# decifrando uma mensagem usando AES-GCM com IV derivado
def decifrar_mensagem(chave_sessao, iv, mensagem_cifrada):
    aesgcm = AESGCM(chave_sessao)
    mensagem_decifrada = aesgcm.decrypt(iv, mensagem_cifrada, None)
    return mensagem_decifrada