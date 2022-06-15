import qrcode

image_path = "C:/Users/sarah/Documents/uni/final-year-project/qr-code-attendance-angular/src/assets/img/users"


def generate_qrcode(id):
    # Generating QR code
    qr_code = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_M,
                            box_size=10, border=4)  # create class and specify parameters

    # Add QR Code Data
    qr_code.add_data(id)
    qr_code.make(fit=True)

    # Wrap QR Code in Image
    qr_image = qr_code.make_image(fill_color='black', back_color='white')
    # qr_image.save(f"{image_path}/{id}.png")
    qr_image.save(f"{image_path}/{id}.png")
    filepath = f"{image_path}/{id}.png"
    print(filepath)


generate_qrcode("EXAMPLE")
