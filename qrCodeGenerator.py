import qrcode
import os

data = input("Enter the text or URL: ").strip()
filename = input("Enter the filename: ").strip()
directory = input("Enter the directory to save the file: ").strip()

# Ensure the directory exists
if not os.path.exists(directory):
    os.makedirs(directory)

filepath = os.path.join(directory, filename)

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")
image.save(filepath)
print(f"QR code saved as {filepath}")