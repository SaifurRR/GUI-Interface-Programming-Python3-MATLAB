"""
This code creates a Number System Base Conversion GUI with Python programming language using the 'tkinter' package. 

GUI Display: 
-Enter number
-Select Base to convert 'From'
-Select Base to convert 'To'
-Click convert to execute conversion
"""

import tkinter as tk

# Function to perform the base conversion
def convert_base():
    try:
        num = entry_number.get()  # Get the user input number
        from_base = int(entry_from_base.get())  # Get the source base
        to_base = int(entry_to_base.get())  # Get the target base
        result = int(num, from_base)  # Convert the input number to base 10
        result = format(result, '0' + str(to_base) + 'b')  # Convert to the target base
        label_result.config(text=result)  # Display the result
    except ValueError:
        label_result.config(text="Invalid input")

# Create the main application window
app = tk.Tk()
app.title("Number Base Converter")

# Create labels and entry fields for user input
label_number = tk.Label(app, text="Enter a number:")
label_number.grid(row=0, column=0)
entry_number = tk.Entry(app)
entry_number.grid(row=0, column=1)

label_from_base = tk.Label(app, text="From base:")
label_from_base.grid(row=1, column=0)
entry_from_base = tk.Entry(app)
entry_from_base.grid(row=1, column=1)

label_to_base = tk.Label(app, text="To base:")
label_to_base.grid(row=2, column=0)
entry_to_base = tk.Entry(app)
entry_to_base.grid(row=2, column=1)

# Create a button to perform the conversion
convert_button = tk.Button(app, text="Convert", command=convert_base)
convert_button.grid(row=3, column=0, columnspan=2)

# Create a label to display the result
label_result = tk.Label(app, text="")
label_result.grid(row=4, column=0, columnspan=2)

app.mainloop()
