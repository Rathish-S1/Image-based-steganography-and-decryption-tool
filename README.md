# Image-based-steganography-and-decryption-tool
Hide Secret Text Message Inside Image Using Python 
# 🕵️‍♂️ Hide Secret Text Message Inside Image Using Python (Tkinter GUI)

A simple **Image Steganography** tool built with **Python** and **Tkinter** that allows users to **hide** and **reveal** secret text messages inside images using the Least Significant Bit (LSB) encoding technique.

---

## 📸 Features

✅ Hide secret messages inside PNG images  
✅ Extract hidden messages from encoded images  
✅ Simple and user-friendly GUI (Tkinter)  
✅ Works entirely offline  
✅ Lightweight and open-source  

---

## 🧰 Technologies Used

- **Python 3.x**
- **Tkinter** — for GUI  
- **Pillow (PIL)** — for image manipulation  

---

## ⚙️ Installation & Setup

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/image-steganography-gui.git
   cd image-steganography-gui
Install dependencies

bash
Copy code
pip install pillow
Run the app

bash
Copy code
python steganography_gui.py
🧠 How It Works
🔒 Hiding a Message
Type your secret message in the text box.

Choose a PNG image file when prompted.

The program encodes your message into the image’s pixel data using Least Significant Bit (LSB) steganography.

Save the encoded image — it will look visually identical to the original.

🔍 Revealing a Message
Load the encoded image using the “Reveal Message” button.

The hidden message will appear in the text area.

🪄 Example Workflow
Open the app

Enter:

csharp
Copy code
This is a secret message.
Click Hide Message, choose an image → save as secret.png.

To decode, click Reveal Message and select secret.png.

Your message appears in the text box!

🧩 File Structure
bash
Copy code
📁 image-steganography-gui
├── steganography_gui.py   # Main application file
├── README.md              # Project documentation
└── sample_image.png       # (Optional) Example image
⚠️ Notes
Use .PNG files (JPEG compression may destroy hidden data).

Keep encoded images safe — anyone with this tool can decode them.

Messages are stored as binary within pixel values — no visual change occurs.

🚀 Future Improvements
Add password-based encryption/decryption

Support drag-and-drop for images

Add file-based message embedding (hide .txt or .pdf files)

🧑‍💻 Author
 Rathish.S
📧 rathishdhana85@gmail.com


