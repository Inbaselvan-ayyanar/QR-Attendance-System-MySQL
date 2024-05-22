
import qrcode
import cv2

qr= qrcode.QRCode(version=1, box_size=10, border=5)

data1 = input()
data2 = input()
data=data1+" "+data2
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="white")
path=data2+".png"
img.save(path)

