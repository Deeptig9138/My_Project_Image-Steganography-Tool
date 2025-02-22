import os

# Define the directory where encrypted data is stored
SAVE_DIR = r"D:\internships\AICTE\Cybersecurity\Stenography"

def decrypt_message(password):
    try:
        # Load encryption data from the specified directory
        encrypted_data_path = os.path.join(SAVE_DIR, "encryption_data.txt")
        with open(encrypted_data_path, "r") as f:
            stored_password = f.readline().strip()
            encrypted_message = f.readline().strip()
    except FileNotFoundError:
        print("Error: Encryption data not found.")
        return

    # Validate the password
    if password != stored_password:
        print("Error: Incorrect password.")
        return

    # Display the decrypted message
    decrypted_message = encrypted_message.rstrip('\0')  # Remove the terminator if present
    print(f"Decrypted Message: {decrypted_message}")

# Get password input from the terminal
password = input("Enter the password to decrypt the message: ")
decrypt_message(password)