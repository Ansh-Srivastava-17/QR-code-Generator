import qrcode
import image
qr = qrcode.QRCode(
    version =15,   #HIGHER THE NUMBER BIGGER THE IMAGE MORE COMLICATED QR CODE
    box_size=10,    #SIZE OF THE QR CODE BOX
    border=5,       #WHITE PART OF IMAGE
)
data="ansh IS A GREAT PROGRAMMER"
# IN THIS DATA FILE I CAN WRITE ANY TEXT OR EVEN ANY URL ALSO
qr.add_data(data)
qr.make(fit = True)
img= qr.make_image(fill="black",back_color="white")
img.save("test2.png")