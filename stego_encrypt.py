import cv2
import os
import webbrowser
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox

# Define the directory to save the encrypted image and data
SAVE_DIR = r"D:\internships\AICTE\Cybersecurity\Stenography"

# Encryption Function
def encrypt_image(img_path, msg, password):
    img = cv2.imread(img_path)

    if img is None:
        messagebox.showerror("Error", f"Cannot load image at {img_path}")
        return

    d = {chr(i): i for i in range(256)}

    max_capacity = img.shape[0] * img.shape[1] * 3
    if len(msg) >= max_capacity:
        messagebox.showerror("Error", "Message is too long to fit in the image.")
        return

    msg += '\0'  # Add a terminator to handle decryption end

    n, m, z = 0, 0, 0
    for char in msg:
        img[n, m, z] = d[char]
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= img.shape[1]:
                m = 0
                n += 1

    # Save the encrypted image in the specified directory
    encrypted_img_path = os.path.join(SAVE_DIR, "encryptedImage.jpg")
    cv2.imwrite(encrypted_img_path, img)
    messagebox.showinfo("Success", "Message encrypted and image saved successfully!")

    # Save the password and encrypted message in encryption_data.txt
    encrypted_data_path = os.path.join(SAVE_DIR, "encryption_data.txt")
    with open(encrypted_data_path, "w") as f:
        f.write(f"{password}\n{msg}")

    # Display the encrypted image at a smaller size (e.g., 800x600)
    resized_img = cv2.resize(img, (800, 600))
    cv2.imshow("Encrypted Image", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    img_path_entry.delete(0, "end")
    img_path_entry.insert(0, file_path)

def start_encryption():
    img_path = img_path_entry.get()
    msg = message_entry.get()
    password = password_entry.get()
    if img_path and msg and password:
        encrypt_image(img_path, msg, password)
    else:
        messagebox.showerror("Error", "Please fill all fields.")

# GUI Setup for Encryption
app = Tk()
app.title("Image Encryption")
app.geometry("500x250")

Label(app, text="Select Image:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
img_path_entry = Entry(app, width=50)
img_path_entry.grid(row=1, column=0, padx=10, pady=5)
Button(app, text="Browse", command=browse_image).grid(row=1, column=1, padx=10, pady=5)

Label(app, text="Secret Message:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
message_entry = Entry(app, width=50)
message_entry.grid(row=3, column=0, padx=10, pady=5, columnspan=2)

Label(app, text="Password:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
password_entry = Entry(app, width=50, show="*")
password_entry.grid(row=5, column=0, padx=10, pady=5, columnspan=2)

Button(app, text="Encrypt and Save", command=start_encryption).grid(row=6, column=0, columnspan=2, pady=20)

app.mainloop()