# Encryption_Decryption
Encryption and Decryption Script with Fernet
 This Python script uses the `cryptography` library to encrypt and decrypt messages securely. It
 provides interactive prompts for encryption and decryption and allows users to save the encrypted
 message and key to a text file for later use.
 Features- Encryption: Input a message, and the script generates an encrypted version using a random
 Fernet key.- Decryption: Input the encrypted message and the corresponding key to retrieve the original
 message.- Save to File: Option to save the encrypted message and the key to a text file for later use.
 Prerequisites- Python 3.6 or higher.- The `cryptography` library installed. You can install it via pip:
  pip install cryptography
 How to Use
 1. Run the Script:
   Execute the script in a Python environment:
   python script.py
 2. Encryption:
   - Enter a message when prompted.
   - The script will generate and display an encrypted message and the encryption key.
3. Save Option:
   - The script will ask if you want to save the encrypted message and key in a `.txt` file.
   - If you choose "yes", specify a filename, and the data will be saved.
 4. Decryption:
   - Input the encrypted message and the corresponding key when prompted.
   - If the key matches, the original message will be displayed. If not, an error message will appear.
 Example Interaction
 Encryption Key (Save this to decrypt): qTx8An3P5BQ2JgfXvLZ5Kh9b6FM4JtgtDUsK3nXyIkE=
 Enter a message to encrypt: Hello, world!
 Encrypted:
 gAAAAABkwKJX-H_j8kRj8Pn9xrz9tbz3N_r2f5oNcIv-BM82D2PvzShVCsB6P5TEmF9V8U=
 Do you want to save the encrypted message and key in a text file? (yes/no): yes
 Enter the filename (with .txt extension): encrypted_data.txt
 Encrypted message and key saved in encrypted_data.txt
 Enter the encrypted message to decrypt:
 gAAAAABkwKJX-H_j8kRj8Pn9xrz9tbz3N_r2f5oNcIv-BM82D2PvzShVCsB6P5TEmF9V8U=
 Enter the encryption key: qTx8An3P5BQ2JgfXvLZ5Kh9b6FM4JtgtDUsK3nXyIkE=
 Decrypted: Hello, world!
 File Structure- Script: The main Python script.- Output Files: If the save option is chosen, encrypted messages and keys are saved in the specified
`.txt` file.
 Error Handling- If the wrong key is provided or the encrypted message is tampered with, the script displays an
 error:
  Decryption failed. Possible reasons: Incorrect key or corrupted data.
 Notes- Save the encryption key securely. Without it, decryption is not possible.- The encrypted message and key are sensitive. Do not share them carelessly.
 License
 This script is free to use and distribute. Attribution is appreciated but not required.
