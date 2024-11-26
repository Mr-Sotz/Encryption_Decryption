from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher_suite = Fernet(key)
# Print the key (you can use it later for decryption if needed)
print(f"Encryption Key (Save this to decrypt): {key.decode()}")

# Input a message for encryption
message = input("\nEnter a message to encrypt: ").encode()

# Encrypt the message
encrypted_message = cipher_suite.encrypt(message)
print(f"Encrypted: {encrypted_message.decode()}")

# Prompt to save the encrypted message and key in a text file
save_option = input("\nDo you want to save the encrypted message and key in a text file? (yes/no): ").strip().lower()
if save_option == "yes":
    filename = input("Enter the filename (with .txt extension): ").strip()
    try:
        with open(filename, "w") as file:
            file.write(f"Encryption Key: {key.decode()}\n")
            file.write(f"Encrypted Message: {encrypted_message.decode()}\n")
        print(f"Encrypted message and key saved in {filename}")
    except Exception as e:
        print(f"Failed to save the file: {e}")

# Input the encrypted message for decryption
encrypted_input = input("\nEnter the encrypted message to decrypt: ").encode()

# Input the encryption key for decryption
key_input = input("Enter the encryption key: ").encode()

try:
    # Initialize a Fernet instance with the provided key
    decryption_cipher = Fernet(key_input)
    decrypted_message = decryption_cipher.decrypt(encrypted_input)
    print(f"Decrypted: {decrypted_message.decode()}")
except Exception as e:
    print("Decryption failed. Possible reasons: Incorrect key or corrupted data.")
