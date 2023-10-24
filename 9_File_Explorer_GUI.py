"""
This code provides a simple file explorer GUI using Tkinter. Users can click the "Browse" button to select a directory. 

The selected directory is displayed in a label, and the list of files and folders in that directory is displayed in a list box.

GUI Display: 
Browse button: to navigate to a folder in the local directory.
"""

import tkinter as tk
from tkinter import filedialog
import os

# FileExplorer class for creating the file explorer GUI
class FileExplorer:
    def __init__(self, root):
        self.root = root
        self.root.title("File Explorer")

        # Label to display the selected directory
        self.label = tk.Label(root, text="Selected Directory:")
        self.label.pack()

        # Label to display the selected directory path
        self.selected_dir_label = tk.Label(root, text="")
        self.selected_dir_label.pack()

        # Button to browse and select a directory
        self.browse_button = tk.Button(root, text="Browse", command=self.browse_directory)
        self.browse_button.pack()

        # Listbox to display the list of files and folders in the selected directory
        self.file_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10)
        self.file_listbox.pack()

    # Method to open a file dialog and select a directory
    def browse_directory(self):
        selected_directory = filedialog.askdirectory()  # Open a file dialog to select a directory
        self.selected_dir_label.config(text=f"Selected Directory: {selected_directory}")

        # List files in the selected directory
        self.list_files(selected_directory)

    # Method to list files in the selected directory
    def list_files(self, directory):
        self.file_listbox.delete(0, tk.END)  # Clear the listbox
        files = os.listdir(directory)
        for file in files:
            self.file_listbox.insert(tk.END, file)

# Main function to create the GUI
def main():
    root = tk.Tk()
    app = FileExplorer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
