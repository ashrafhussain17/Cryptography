file1 = open("plaintext.txt", "r")
plain = file1.read()

file2 = open("key.txt", "r")
key = file2.read()
key_len = len(key)

plain_text = []
cipher_text = []
cipher_text_space = []

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

for i in plain:
    if ('A' <= i <= 'Z') or ('a' <= i <= 'z'):
        plain_text.append(i)

for i in range(len(plain_text)):
    index = (characters.find(plain_text[i]) + characters.find(key[i % key_len])) % 52
    cipher_text.append(characters[index])
    if i % 5 == 0 and i != 0:
        cipher_text_space.append(' ')
    cipher_text_space.append(characters[index])

print("Cipher Text: ", end="")
print("".join(cipher_text))

print("Cipher Text with 5 characters : ", end='')
print("".join(cipher_text_space))

ciphertext = open("ciphertext.txt", "w")
ciphertext.write("".join(cipher_text_space))
ciphertext.close()
# Decryption:
ciphertext_read = open("ciphertext.txt", "r")
output_cipher = ciphertext_read.read()

out = output_cipher.replace(" ", "")
out_len = len(out)

decrypt_message = []

for i in range(out_len):
    ot_index = characters.find(out[i]) - characters.find(key[i % key_len]) % 52
    decrypt_message.append(characters[ot_index])
print("Decrypt Message: " + "".join(decrypt_message))

