import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password(length, include_uppercase, include_numbers, include_special):
    if length < (include_uppercase + include_numbers + include_special):
        raise ValueError("Password length is too short for the specified criteria.")

    password = ""

    if include_uppercase:
        password += random.choice(string.ascii_uppercase)
    if include_numbers:
        password += random.choice(string.digits)
    if include_special:
        password += random.choice(string.punctuation)

    # Fill the remaining length with any allowed characters
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    for _ in range(length - len(password)):
        password += random.choice(characters)

    password_list = list(password)
    random.shuffle(password_list)
    return "".join(password_list)

def on_generate_password():
    try:
        length = int(entry_length.get())
        include_uppercase = var_uppercase.get()
        include_numbers = var_numbers.get()
        include_special = var_special.get()
        
        password = generate_password(length, include_uppercase, include_numbers, include_special)
        label_result.config(text=f"Generated Password: {password}")
        
        # Enable the Copy to Clipboard button after generating a password
        copy_button.config(state="normal")
        copy_button.password = password  # Store the password in the button for access
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def copy_to_clipboard():
    # Copy the generated password to the clipboard
    root.clipboard_clear()
    root.clipboard_append(copy_button.password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Set up the Tkinter GUI window
root = tk.Tk()
root.title("Random Password Generator")

# Length label and entry
tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=5)
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=5)

# Uppercase checkbox
var_uppercase = tk.BooleanVar()
tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_uppercase).grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Numbers checkbox
var_numbers = tk.BooleanVar()
tk.Checkbutton(root, text="Include Numbers", variable=var_numbers).grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Special characters checkbox
var_special = tk.BooleanVar()
tk.Checkbutton(root, text="Include Special Characters", variable=var_special).grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Generate password button
generate_button = tk.Button(root, text="Generate Password", command=on_generate_password)
generate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Password display label
label_result = tk.Label(root, text="Generated Password: ")
label_result.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Copy to clipboard button, initially disabled
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, state="disabled")
copy_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
