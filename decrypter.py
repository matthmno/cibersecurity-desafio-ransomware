import os
import pyaes

# Nome do arquivo criptografado
file_name = "atividade.txt.ransomwaretroll"
new_file_name = "atividade1.txt"

# Abrir o arquivo criptografado
with open(file_name, "rb") as file:
    file_data = file.read()

# Chave de descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# Remover o arquivo criptografado
os.remove(file_name)

# Criar o arquivo descriptografado
with open(new_file_name, "wb") as new_file:
    new_file.write(decrypt_data)

print(f"[+] Arquivo descriptografado: {new_file_name}")
