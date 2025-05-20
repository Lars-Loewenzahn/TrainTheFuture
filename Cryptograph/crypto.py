class SimpleEncryptor:
    def __init__(self):
        # self.key = key.encode()  # Textschlüssel in Bytes umwandeln
        self.a = "password"
        print("Encryptor initilised")

    def _xor_bytes(self, data: bytes) -> bytes:
        return bytes([b ^ self.key[i % len(self.key)] for i, b in enumerate(data)])

    def encrypt_file(self, key: str, input_path: str, output_path: str):
        self.key = key.encode() 
        with open(input_path, "rb") as f:
            data = f.read()
        encrypted = self._xor_bytes(data)
        with open(output_path, "wb") as f:
            f.write(encrypted)

    def decrypt_file(self,key: str,  input_path: str, output_path: str):
        # XOR ist symmetrisch: gleiche Methode wie beim Verschlüsseln
        self.key = key
        self.encrypt_file(key, input_path, output_path)

if __name__ == "__main__":
    encyptor = SimpleEncryptor()
    encyptor.encrypt_file("password", "Cryptograph/test_file.py", "Cryptograph/encypted_test_file.txt")
    encyptor.decrypt_file("password", "Cryptograph/encypted_test_file.txt", "Cryptograph/decrypted_test_file.py")
