#Flask module import
from flask import Flask, request
#Qr creation class import from project files
from creator_classes import QrCodeCreator
#Barcode creation class import from project files
from creator_classes import BarcodeCreator

app = Flask(__name__)

#Api welcome message end point
@app.route('/')
def welcome_message_page():  # put application's code here
    welcome_message = "See barcode/api  or  qrCode/api  for endpoints you can use"
    return welcome_message

#Qr code end points information end point
@app.route('/qrCode/api')
def show_qr_code_api():
    api_message = "For generating qr code => /qrCode?qr-code-url=(Your qr code url)"
    return api_message

#Qr code creation and downloader end point
@app.route('/qrCode')
def create_and_save_qr_code():
    qr_url = request.args.get("qr-code-url")
    barcode_message = "Barcode is generated and downloaded into your computer"
    QrCodeCreator.generate_and_save_qr_code(qr_url)
    return barcode_message

#Barcode end points information end point
@app.route('/barcode/api')
def show_barcode_api():
    api_message = "For generating barcode => /barcode?barcode-number=(Your 12 character barcode number)"
    return api_message

#Barcode creation and downloader end point
@app.route('/barcode')
def create_and_save_barcode():
    barcode_number = request.args.get("barcode-number")
    barcode_message = "Barcode is generated and downloaded into your computer"
    BarcodeCreator.generate_and_save_barcode(barcode_number)
    return barcode_message

#Flask runner
if __name__ == '__main__':
    app.run()
