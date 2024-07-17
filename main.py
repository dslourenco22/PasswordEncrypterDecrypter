# Password encrypter and decrypter

def encrypt(password):
    encrypted_password = ""
    for char in password:
        if char.isupper():
            encrypted_password += chr((ord(char) + 3 - 65) % 26 + 65)
        else:
            encrypted_password += chr((ord(char) + 3 - 97) % 26 + 97)
    return encrypted_password

def decrypt(password):
    decrypted_password = ""
    for char in password:
        if char.isupper():
            decrypted_password += chr((ord(char) - 3 - 65) % 26 + 65)
        else:
            decrypted_password += chr((ord(char) - 3 - 97) % 26 + 97)
    return decrypted_password

# Main program
print("Password encrypter and decrypter")
print("1. Encrypt password")
print("2. Decrypt password")
print("3. Generate password")
choice = int(input("Enter your choice (1,2,3): "))

if choice == 1:
    password = input("Enter password to encrypt: ")
    encrypted_password = encrypt(password)
    print("Encrypted password:", encrypted_password)
elif choice == 2:
    password = input("Enter password to decrypt: ")
    decrypted_password = decrypt(password)
    print("Decrypted password:", decrypted_password)
elif choice == 3:
    import random
    import string
    def generate_password(length, include_letters,       
      include_digits,include_punctuation, digits):             
      password_chars = ''
      if include_letters:
        password_chars += string.ascii_letters
      if include_digits:
        password_chars += ''.join(digits)
      if include_punctuation:
        password_chars += string.punctuation
      return ''.join(random.choice(password_chars) for i in range(length))

    password_length = int(input("Enter the desired password length: "))

    include_letters = input("Include letters in the password? (y/n) ").lower() == 'y'
    include_digits = input("Include digits in the password? (y/n) ").lower() == 'y'

    # Initialize the 'digits' list with the digits to include in the password
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    include_punctuation = input("Include punctuation in the password? (y/n)               ").lower() == 'y'
  
    password = generate_password(password_length, include_letters, include_digits,         include_punctuation, digits)
    print(password)

  


