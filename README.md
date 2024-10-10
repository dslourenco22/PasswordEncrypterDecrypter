# Password Encrypter and Decrypter

This is a simple Python program that allows users to encrypt, decrypt, and generate passwords. The program offers three functionalities:

1. **Encrypt password**: Shifts each character of the password by 3 positions using Caesar cipher.
2. **Decrypt password**: Reverses the encryption by shifting each character back by 3 positions.
3. **Generate password**: Allows the user to create a random password with custom length and character set options.

## Features

- **Encryption and Decryption**:
  - Uses a simple Caesar cipher to encrypt passwords by shifting characters by a fixed number of positions (3 positions).
  - Can encrypt and decrypt both upper- and lower-case letters.

- **Password Generator**:
  - Generates a random password based on user preferences.
  - Users can specify the length of the password and whether to include:
    - Letters (uppercase and lowercase)
    - Digits (0-9)
    - Punctuation (special characters)

## Usage

To use the program, simply run the Python script and follow the prompts. The user can choose to either encrypt a password, decrypt a password, or generate a new password.

### Running the Program

```bash
python password_encrypter_decrypter.py
