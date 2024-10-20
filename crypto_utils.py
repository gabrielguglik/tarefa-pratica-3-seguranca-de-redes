import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Derivação da chave de sessão usando PBKDF2
def derivar_chave_sessao(codigo_totp):
    password = codigo_totp.encode()  # Usar o código TOTP como senha
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    chave_sessao = kdf.derive(password)
    return chave_sessao

# Cifrar o comprovante usando AES-GCM
def cifrar_comprovante(chave_sessao, comprovante):
    aesgcm = AESGCM(chave_sessao)
    nonce = os.urandom(12)  # Gera um nonce aleatório
    comprovante_cifrado = aesgcm.encrypt(nonce, comprovante, None)
    return nonce, comprovante_cifrado

# Decifrar o comprovante usando AES-GCM
def decifrar_comprovante(chave_sessao, nonce, comprovante_cifrado):
    aesgcm = AESGCM(chave_sessao)
    comprovante_decifrado = aesgcm.decrypt(nonce, comprovante_cifrado, None)
    return comprovante_decifrado

# Cifrar uma mensagem usando AES-GCM
def cifrar_mensagem(chave_sessao, mensagem):
    aesgcm = AESGCM(chave_sessao)
    nonce = os.urandom(12)
    mensagem_cifrada = aesgcm.encrypt(nonce, mensagem, None)
    return nonce, mensagem_cifrada

# Decifrar uma mensagem usando AES-GCM
def decifrar_mensagem(chave_sessao, nonce, mensagem_cifrada):
    aesgcm = AESGCM(chave_sessao)
    mensagem_decifrada = aesgcm.decrypt(nonce, mensagem_cifrada, None)
    return mensagem_decifrada