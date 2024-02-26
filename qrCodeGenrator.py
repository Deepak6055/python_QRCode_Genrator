import qrcode
from PIL import Image

def generate_qr_code(url, file_name='qr_code.png'):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(file_name)

    print(f"QR Code generated and saved as {file_name}")

if __name__ == "__main__":
    url = input("Enter the URL to encode: ")
    file_name = input("Enter the file name to save the QR code as (default: qr_code.png): ")

    if not file_name:
        generate_qr_code(url)
    else:
        generate_qr_code(url, file_name)
