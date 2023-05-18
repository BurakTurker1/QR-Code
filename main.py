import pyqrcode
url= input("enter url:")
qr_code=pyqrcode.create(url)
qr_code.svg('QR code',scale=5)
