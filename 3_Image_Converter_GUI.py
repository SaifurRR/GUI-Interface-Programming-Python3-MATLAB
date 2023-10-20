"""
This code uses the 'tkinter' and 'PIL' libraries to create an Image Converter GUI with Python.
The code is programmed to convert jpg -> png and vice versa.

GUI Display: 
Select the Image button: to browse files from the local device
Convert Format: select jpg or png file type to convert the selected image.
"""
import tkinter as tk
from tkinter import filedialog
from PIL import Image

# Create a Tkinter window
root = tk.Tk()
canvas1 = tk.Canvas(root, width=300, height=250, bg='azure3', relief='raised')
canvas1.pack()

# Label for the application
label1 = tk.Label(root, text="Image Format Converter", bg='azure3')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

def openImage():
    global im1
    import_file_path = filedialog.askopenfilename(filetypes=[("Image Files", ("*.jpg", "*.png"))])
    im1 = Image.open(import_file_path)

# Button to select an image file
browse_button = tk.Button(text="Select Image", command=openImage, bg="royalblue", fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browse_button)

def convertImage():
    global im1
    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")])
    im1.save(export_file_path)

# Button to convert the image to the other format
convert_button = tk.Button(text="Convert Format", command=convertImage, bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=convert_button)

# Start the main Tkinter loop
root.mainloop()

