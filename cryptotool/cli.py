import argparse
from cryptotool.keygen import gen_symmetric_key, gen_rsa_keys
from cryptotool.symmetric import load_symmetric_key, encrypt_file, decrypt_file
from cryptotool.hashing import sha256_hash_file
from cryptotool.asymmetric import sign_file, verify_signature

parser = argparse.ArgumentParser(description="📦 Cryptotool CLI")
sub = parser.add_subparsers(dest="cmd")

# Keygen
sub.add_parser("gen-sym", help="Generate symmetric (Fernet) key")
sub.add_parser("gen-rsa", help="Generate RSA key pair")

# Symmetric encrypt/decrypt
enc = sub.add_parser("enc", help="Encrypt file")
enc.add_argument("infile")
enc.add_argument("outfile")
dec = sub.add_parser("dec", help="Decrypt file")
dec.add_argument("infile")
dec.add_argument("outfile")

# Hash
h = sub.add_parser("hash", help="SHA-256 hash file")
h.add_argument("file")

# Sign / Verify
s = sub.add_parser("sign", help="Sign file with RSA private key")
s.add_argument("file")
v = sub.add_parser("verify", help="Verify signature")
v.add_argument("file")
v.add_argument("sigfile")

if __name__ == "__main__":
    args = parser.parse_args()
    if args.cmd == "gen-sym":
        gen_symmetric_key()
    elif args.cmd == "gen-rsa":
        gen_rsa_keys()
    elif args.cmd == "enc":
        key = load_symmetric_key()
        encrypt_file(args.infile, args.outfile, key)
    elif args.cmd == "dec":
        key = load_symmetric_key()
        decrypt_file(args.infile, args.outfile, key)
    elif args.cmd == "hash":
        sha256_hash_file(args.file)
    elif args.cmd == "sign":
        sign_file(args.file)
    elif args.cmd == "verify":
        verify_signature(args.file, args.sigfile)
    else:
        parser.print_help()
