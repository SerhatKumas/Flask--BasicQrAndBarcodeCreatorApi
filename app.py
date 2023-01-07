from flask import Flask
from creator_classes import QrCodeCreator
app = Flask(__name__)


@app.route('/')
def welcome_message_page():  # put application's code here
    welcome_message = "WELCOME TO QR CODE AND BARCODE CREATOR"
    return welcome_message


if __name__ == '__main__':
    app.run()
