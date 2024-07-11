import qrcode
phone = "9846906232"
message = "Hey, what's up?"

sms = f"SMSTO:{phone}:{message}"
img = qrcode.make(sms)
type(img)  # qrcode.image.pil.PilImage
img.save("sms.png")