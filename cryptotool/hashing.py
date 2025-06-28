import hashlib

def sha256_hash_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    digest = h.hexdigest()
    print(f"[+] SHA-256({path}) = {digest}")
    return digest
