from cryptography.fernet import Fernet

def load_symmetric_key(path="keys/symmetric.key"):
    return open(path, "rb").read()

def encrypt_file(input_path, output_path, key):
    f = Fernet(key)
    data = open(input_path, "rb").read()
    token = f.encrypt(data)
    with open(output_path, "wb") as out:
        out.write(token)
    print(f"[+] File encrypted → {output_path}")

def decrypt_file(input_path, output_path, key):
    f = Fernet(key)
    token = open(input_path, "rb").read()
    data = f.decrypt(token)
    with open(output_path, "wb") as out:
        out.write(data)
    print(f"[+] File decrypted → {output_path}")
