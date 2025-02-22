# 🔐 Image Steganography Tool
Welcome to the **Image Steganography Tool**, a powerful yet simple application to **hide secret messages inside images** and **reveal them with a password**! 🕵️‍♂️🖼️

## 🚀 Features

- **Encrypt Messages:** Embed your secret message into any image.
- **Password Protection:** Secure your messages with a password.
- **Decrypt Messages:** Retrieve hidden messages using the correct password.
- **User-Friendly GUI:** Simple interface for encryption, terminal-based decryption.

## 📂 Project Structure
```
📦 Image Steganography Tool
├── stego_encrypt.py       # Main GUI application for encryption
├── stego_decrypt.py       # Terminal-based decryption script
├── mypic.jpg              # Image used for encryption of message
├── encryption_data.txt    # Stores the encrypted message and password
├── encryptedImage.jpg     # Output image with hidden message
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## 💻 How to Use

### 1. Installation
Clone the repository and install the required packages:
```
git clone https://github.com/Deeptig9138/image-steganography-tool.git
cd image-steganography-tool
pip install -r requirements.txt
```

### 2. Encryption (GUI)
Run the stego.py file to launch the GUI:
```
python stego.py
```
- Select an Image 🖼️
-Enter your Secret Message ✨
- Set a Password 🔐
- Click 'Encrypt and Save' ✅

### 3. Decryption (Terminal)
Run the stego_decrypt.py file to decrypt the message:
```
python stego_decrypt.py
```
Enter the Password to view the hidden message.

## 🧠 How it Works
- Message Embedding: Pixels in the image are manipulated to store ASCII values of characters.
- Password Protection: Prevents unauthorized message retrieval.
- Message Extraction: Reads pixel data to reconstruct the hidden message.

### Example of Encrypted Image
![Encrypted Image](https://github.com/Deeptig9138/My_Project_Image-Steganography-Tool/blob/main/Images/encrypted.png)

### Example of Decrypted Image
![Decrypted Image](https://github.com/Deeptig9138/My_Project_Image-Steganography-Tool/blob/main/Images/decrypted.png)

## 🤖 Contributing
Feel free to submit issues and pull requests. Contributions are always welcome!

## 📄 License
This project is licensed under the MIT License.

Made by Deepti Gupta
