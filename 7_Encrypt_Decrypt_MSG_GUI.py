"""
In this code, we create a GUI using Tkinter for encrypting and decrypting messages.
It uses a basic Caesar cipher with a fixed shift of 3 for encryption and decryption. 

GUI Display: 
Encrypt button: to encrypt the message.
Decrypt button: to decrypt the message.
"""

import tkinter as tk

# Caesar cipher function for encryption and decryption
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Check if the character is alphabetic
            shift_amount = shift % 26  # Ensure the shift stays within the alphabet (26 letters)
            if char.islower():  # Check if the character is lowercase
                shifted = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            else:
                shifted = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            result += shifted
        else:
            result += char  # Leave non-alphabetic characters unchanged
    return result

# MessageEncryptDecrypt class for the GUI
class MessageEncryptDecrypt:
    def __init__(self, root):
        self.root = root
        self.root.title("Message Encryption and Decryption")

        self.label = tk.Label(root, text="Enter a message:")
        self.label.pack()

        self.message_entry = tk.Entry(root)
        self.message_entry.pack()

        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt_message)
        self.encrypt_button.pack()

        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt_message)
        self.decrypt_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    # Method to encrypt the message
    def encrypt_message(self):
        message = self.message_entry.get()
        encrypted_message = caesar_cipher(message, 3)  # Using Caesar cipher with a shift of 3
        self.result_label.config(text=f"Encrypted message: {encrypted_message}")

    # Method to decrypt the message
    def decrypt_message(self):
        encrypted_message = self.message_entry.get()
        decrypted_message = caesar_cipher(encrypted_message, -3)  # Decrypt by shifting back 3
        self.result_label.config(text=f"Decrypted message: {decrypted_message}")

# Main function to create the GUI
def main():
    root = tk.Tk()
    app = MessageEncryptDecrypt(root)
    root.mainloop()

if __name__ == "__main__":
    main()
