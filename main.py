import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        messagebox.showerror("Error", "Please select at least one character type.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def evaluate_strength(password):
    length = len(password)
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    digits = any(char.isdigit() for char in password)
    special = any(char in string.punctuation for char in password)
    
    strength = 0
    if length >= 8:
        strength += 1
    if uppercase:
        strength += 1
    if lowercase:
        strength += 1
    if digits:
        strength += 1
    if special:
        strength += 1
    
    return strength

def copy_to_clipboard():
    password = password_output.get("1.0", tk.END).strip()
    pyperclip.copy(password)
    messagebox.showinfo("Success", "Password copied to clipboard!")

def generate_password_gui():
    length = int(length_entry.get())
    use_uppercase = uppercase_var.get() == 1
    use_lowercase = lowercase_var.get() == 1
    use_digits = digits_var.get() == 1
    use_special = special_var.get() == 1
    
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
    
    if password:
        password_output.config(state=tk.NORMAL)
        password_output.delete('1.0', tk.END)
        password_output.insert(tk.END, password)
        password_output.config(state=tk.DISABLED)
        
        strength = evaluate_strength(password)
        strength_label.config(text=f"Password strength: {strength} out of 5")

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Enter the length of the password:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

uppercase_var = tk.IntVar()
uppercase_check = tk.Checkbutton(root, text="Include uppercase letters", variable=uppercase_var)
uppercase_check.pack()

lowercase_var = tk.IntVar()
lowercase_check = tk.Checkbutton(root, text="Include lowercase letters", variable=lowercase_var)
lowercase_check.pack()

digits_var = tk.IntVar()
digits_check = tk.Checkbutton(root, text="Include digits", variable=digits_var)
digits_check.pack()

special_var = tk.IntVar()
special_check = tk.Checkbutton(root, text="Include special characters", variable=special_var)
special_check.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password_gui)
generate_button.pack()

password_output = tk.Text(root, height=2, width=30, state=tk.DISABLED)
password_output.pack()

copy_button = tk.Button(root, text="Copy Password", command=copy_to_clipboard)
copy_button.pack()

strength_label = tk.Label(root, text="")
strength_label.pack()

root.mainloop()
