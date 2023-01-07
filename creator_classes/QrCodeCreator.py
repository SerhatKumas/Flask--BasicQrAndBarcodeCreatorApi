import qrcode


def generate_and_save_qr_code(qr_url):
    # Creation of Qr Code
    qr = qrcode.QRCode(
        # The size of the QR Code
        version=1,
        # The error correction used for the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        # How many pixels each “box” of the QR code is.
        box_size=10,
        # How many boxes thick the border should be
        border=4,
    )

    # Url that you want to embed is taken as parameter
    qr.add_data(qr_url)
    qr.make(fit=True)
    # Qr code creation
    # img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
    img = qr.make_image(fill_color="black", back_color="white")
    # Saving generated qr code
    img.save("qr_code.jpg")