import qrcode
from data_sets import data_set_one

# Todo - set up, finish

""" Data contained within the QR code """

data = data_set_one
picture = qrcode.make(data)
picture.save('[INSET FOLDER PATH]')