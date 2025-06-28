from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

def sign_file(path, priv_key_path="keys/private_rsa.pem"):
    # load private key
    priv = serialization.load_pem_private_key(
        open(priv_key_path, "rb").read(),
        password=None
    )
    data = open(path, "rb").read()
    signature = priv.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    sig_path = path + ".sig"
    with open(sig_path, "wb") as f:
        f.write(signature)
    print(f"[+] Signature saved to {sig_path}")
    return sig_path

def verify_signature(path, sig_path, pub_key_path="keys/public_rsa.pem"):
    pub = serialization.load_pem_public_key(open(pub_key_path, "rb").read())
    data = open(path, "rb").read()
    signature = open(sig_path, "rb").read()
    try:
        pub.verify(
            signature,
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("[+] Signature is VALID ✅")
        return True
    except Exception:
        print("[-] Signature is INVALID ❌")
        return False
