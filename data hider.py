from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image
import os

# ---------- Functions ----------

def hide_message():
    message = secret_text.get("1.0", END)
    if not message.strip():
        messagebox.showwarning("Warning", "Please enter a secret message!")
        return
    
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("PNG files", "*.png")])
    if not file_path:
        return

    img = Image.open(file_path)
    encoded = img.copy()
    width, height = img.size
    index = 0

    binary_message = ''.join(format(ord(i), '08b') for i in message)
    binary_message += '1111111111111110'  # end marker

    for row in range(height):
        for col in range(width):
            if index < len(binary_message):
                pixel = list(img.getpixel((col, row)))
                for n in range(3):  # modify R, G, B
                    if index < len(binary_message):
                        pixel[n] = pixel[n] & ~1 | int(binary_message[index])
                        index += 1
                encoded.putpixel((col, row), tuple(pixel))
            else:
                break
    
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        encoded.save(save_path)
        messagebox.showinfo("Success", "Message hidden and image saved!")

def reveal_message():
    file_path = filedialog.askopenfilename(title="Select Encoded Image", filetypes=[("PNG files", "*.png")])
    if not file_path:
        return

    img = Image.open(file_path)
    binary_data = ""
    width, height = img.size

    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for n in range(3):
                binary_data += str(pixel[n] & 1)

    # Split binary data into 8-bit chunks
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]

    decoded = ""
    for byte in all_bytes:
        decoded_char = chr(int(byte, 2))
        decoded += decoded_char
        if decoded.endswith("þ"):  # end marker
            break

    secret_text.delete("1.0", END)
    secret_text.insert(END, decoded[:-1])  # remove marker

# ---------- GUI ----------

root = Tk()
root.title("Image Steganography - Hide Secret Message")
root.geometry("600x400")
root.config(bg="#222831")

Label(root, text="Secret Message:", fg="white", bg="#222831", font=("Arial", 14)).pack(pady=10)
secret_text = Text(root, width=60, height=10, wrap=WORD, font=("Arial", 12))
secret_text.pack(pady=10)

frame = Frame(root, bg="#222831")
frame.pack(pady=20)

Button(frame, text="Hide Message", command=hide_message, bg="#00adb5", fg="white", font=("Arial", 12), width=15).grid(row=0, column=0, padx=10)
Button(frame, text="Reveal Message", command=reveal_message, bg="#393e46", fg="white", font=("Arial", 12), width=15).grid(row=0, column=1, padx=10)

root.mainloop()
