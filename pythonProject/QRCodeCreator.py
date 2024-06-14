import pyqrcode

url = input("Enter the url: ")
qr_code = pyqrcode.create(url)
qr_code.svg("QRCode.svg")
