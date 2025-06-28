# Cryptotool

*Simple CLI for common cryptography tasks in Python.*

---

## 📖 Deskripsi

`cryptotool` adalah command-line interface (CLI) tool berbasis Python yang memudahkan operasi kriptografi dasar, meliputi:

* **🔑 Generate Keys**

  * Symmetric key (Fernet)
  * Asymmetric key pair (RSA)
* **🔒 Encrypt / Decrypt File**

  * File encryption/decryption menggunakan symmetric key
* **🛡️ Hashing**

  * Hitung SHA-256 hash dari file
* **✍️ Digital Signature**

  * Generate dan verifikasi signature menggunakan RSA

Dengan `cryptotool`, kamu dapat dengan cepat mengamankan file, memverifikasi integritas data, serta mempelajari dasar-dasar kriptografi.

---

## 🚀 Fitur Utama

| Perintah              | Deskripsi                                      |
| --------------------- | ---------------------------------------------- |
| `gen-sym`             | Generate symmetric (Fernet) key                |
| `gen-rsa`             | Generate RSA key pair (private & public)       |
| `enc <in> <out>`      | Encrypt file `<in>` → `<out>`                  |
| `dec <in> <out>`      | Decrypt file `<in>` → `<out>`                  |
| `hash <file>`         | Compute SHA-256 hash of `<file>`               |
| `sign <file>`         | Sign `<file>` → output signature file (`.sig`) |
| `verify <file> <sig>` | Verify signature `<sig>` for `<file>`          |

---

## 🛠️ Instalasi

1. **Clone repository**

   ```bash
   git clone https://github.com/delfiboyz/cryptotool.git
   cd cryptotool
   ```

2. **Buat dan aktifkan virtual environment**

   ```bash
   python3 -m venv .venv              # buat venv
   source .venv/bin/activate         # Linux/macOS
   # .\.venv\\Scripts\\activate    # Windows PowerShell
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🗂️ Struktur Direktori

```plaintext
cryptotool/               # Root project
├── README.md             # Dokumentasi ini
├── requirements.txt      # Daftar dependency
├── .gitignore            # file untuk ignore
├── keys/                 # (kosong di repo, untuk menyimpan key runtime)
├── cryptotool/           # Package utama
│   ├── __init__.py
│   ├── keygen.py         # Generate symmetric & RSA keys
│   ├── symmetric.py      # Encrypt & decrypt menggunakan Fernet
│   ├── hashing.py        # SHA-256 hashing
│   ├── asymmetric.py     # Digital signature & verification
│   └── cli.py            # Entry-point CLI (argparse)
└── examples/             # Contoh file untuk testing
    └── sample.txt
```

> **Catatan:** Pastikan folder `keys/` terdaftar di `.gitignore` agar key pribadi tidak ter-commit ke Git.

---

## 💡 Penggunaan

1. **Generate semua key**

   ```bash
   python -m cryptotool.cli gen-sym
   python -m cryptotool.cli gen-rsa
   ```

   * Hasil: file `keys/symmetric.key`, `keys/private_rsa.pem`, `keys/public_rsa.pem`.

2. **Encrypt & Decrypt**

   ```bash
   python -m cryptotool.cli enc examples/sample.txt examples/sample.enc
   python -m cryptotool.cli dec examples/sample.enc examples/decrypted.txt
   ```

3. **Hashing**

   ```bash
   python -m cryptotool.cli hash examples/sample.txt
   ```

   * Output: SHA-256 digest dari file.

4. **Sign & Verify**

   ```bash
   python -m cryptotool.cli sign examples/sample.txt
   python -m cryptotool.cli verify examples/sample.txt examples/sample.txt.sig
   ```

---

## 🤝 Kontribusi

1. Fork repository ini.
2. Buat branch fitur baru: `git checkout -b feature/nama-fitur`.
3. Commit perubahan: `git commit -m "Tambah fitur ..."`.
4. Push ke branch: `git push origin feature/nama-fitur`.
5. Buka pull request.

Kami akan dengan senang hati mereview dan menggabungkan kontribusi kamu!

---

## 📄 Lisensi

Project ini menggunakan lisensi MIT. Lihat file [LICENSE](LICENSE) untuk detail.

---

Selamat mencoba dan semoga bermanfaat! 🎉
