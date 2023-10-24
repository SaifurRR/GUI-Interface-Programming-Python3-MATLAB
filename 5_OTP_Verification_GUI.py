"""
This code creates an OTP GUI with Python programming language using the 'tkinter' package. 
The generate_otp method generates a random 4-digit OTP when you click the "Generate OTP" 
button, and the OTP is displayed. The verify_otp method compares the entered OTP with the
generated OTP and displays a verification result.

GUI Display: 
Generate OTP button: generates random OTP
Verify OTP button: verifies generated OTP
"""
import tkinter as tk
import random

# OTPVerification class for creating the OTP verification GUI
class OTPVerification:
    def __init__(self, root):
        self.root = root
        self.root.title("OTP Verification")

        self.generated_otp = None

        # Label for OTP input
        self.label = tk.Label(root, text="Enter OTP:")
        self.label.pack()

        # Entry field for OTP input
        self.otp_entry = tk.Entry(root)
        self.otp_entry.pack()

        # Button to generate OTP
        self.generate_button = tk.Button(root, text="Generate OTP", command=self.generate_otp)
        self.generate_button.pack()

        # Button to verify OTP
        self.verify_button = tk.Button(root, text="Verify OTP", command=self.verify_otp)
        self.verify_button.pack()

        # Label to display the verification result
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    # Method to generate a random 4-digit OTP
    def generate_otp(self):
        self.generated_otp = random.randint(1000, 9999)  # Generate a random 4-digit OTP
        self.result_label.config(text=f"Generated OTP: {self.generated_otp}")

    # Method to verify the entered OTP
    def verify_otp(self):
        user_otp = self.otp_entry.get()
        if user_otp == str(self.generated_otp):
            self.result_label.config(text="OTP Verified")
        else:
            self.result_label.config(text="OTP Verification Failed")

# Main function to create the GUI
def main():
    root = tk.Tk()
    app = OTPVerification(root)
    root.mainloop()

if __name__ == "__main__":
    main()
