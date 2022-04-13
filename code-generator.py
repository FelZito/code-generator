import pyqrcode
link = str(input("Informe o link: "))
name_png = str(input("Informe um nome para o arquivo: "))
qrcode = pyqrcode.create(link)
qrcode.png(name_png + ".png", scale=5)
print("QR Code gerado!")