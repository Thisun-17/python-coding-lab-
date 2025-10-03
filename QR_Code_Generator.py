import qrcode

data = input("Enter the data or URL to encode in the QR code: ").strip()
filename = input("Enter the filename to save the QR code (e.g., 'qrcode.png'): ").strip()

# Create QR code instance
qr = qrcode.QRCode(
    box_size=10,
    border=4,
)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)
print(f"QR code saved as {filename}")