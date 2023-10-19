"""
This code creates text editor GUI using tkinter. We can create, open, edit and save text
files using this GUI.

GUI Display: 
Text box widget to create & edit text files.
2 button -> save & close.
"""

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Create the main application window
app_window = tk.Tk()
app_window.title("CreativeCoder's Text Editor")

# Configure row and column weights for window resizing
app_window.rowconfigure(0, minsize=800, weight=1)
app_window.columnconfigure(1, minsize=800, weight=1)

# Create a text editing widget
text_editor = tk.Text(app_window)

# Create a frame for buttons
button_frame = tk.Frame(app_window, relief=tk.RAISED, bd=2)

# Define the "Open" function
def initiate_open_file():
    """Open a file for editing."""
    file_path = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not file_path:
        return
    text_editor.delete(1.0, tk.END)
    with open(file_path, "r") as input_file:
        content = input_file.read()
        text_editor.insert(tk.END, content)
    app_window.title(f"CreativeCoder's Text Editor - {file_path}")

# Define the "Save As" function
def initiate_save_file():
    """Save the current content as a new file."""
    file_path = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not file_path:
        return
    with open(file_path, "w") as output_file:
        content = text_editor.get(1.0, tk.END)
        output_file.write(content)
    app_window.title(f"CreativeCoder's Text Editor - {file_path}")

# Create buttons for opening and saving files
open_button = tk.Button(button_frame, text="Open", command=initiate_open_file)
save_button = tk.Button(button_frame, text="Save As...", command=initiate_save_file)

# Grid layout for buttons and text editor
open_button.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
save_button.grid(row=1, column=0, sticky="ew", padx=5)
button_frame.grid(row=0, column=0, sticky="ns")
text_editor.grid(row=0, column=1, sticky="nsew")

# Start the main application loop
app_window.mainloop()
