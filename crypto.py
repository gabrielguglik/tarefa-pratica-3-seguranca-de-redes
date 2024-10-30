import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

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
