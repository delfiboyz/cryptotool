from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

def gen_symmetric_key(path="keys/symmetric.key"):
    key = Fernet.generate_key()
    with open(path, "wb") as f:
        f.write(key)
    print(f"[+] Symmetric key saved to {path}")

def gen_rsa_keys(priv_path="keys/private_rsa.pem", pub_path="keys/public_rsa.pem"):
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    priv = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    pub = key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open(priv_path, "wb") as f:
        f.write(priv)
    with open(pub_path, "wb") as f:
        f.write(pub)
    print(f"[+] RSA private key: {priv_path}")
    print(f"[+] RSA public key : {pub_path}")
