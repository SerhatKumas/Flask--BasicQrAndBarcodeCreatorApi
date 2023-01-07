# import EAN13 from barcode module
from barcode import EAN13

# import ImageWriter to generate an image file
from barcode.writer import ImageWriter


# Barcode creator and saver method
def generate_and_save_barcode(barcode_number):
    # Creation of barcode
    my_code = EAN13(barcode_number, writer=ImageWriter())

    # Our barcode is ready. Let's save it.
    my_code.save("barcode")
