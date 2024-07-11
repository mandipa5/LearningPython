import qrcode
email_address = "mandipa.thapa0927@gmail.com"
subject = "Mail using Python"
body = "Hey, it's my first mail using Python"
mail = f"mailto:{email_address}?subject={subject}&body={body}"
img = qrcode.make(mail)
type(img)  # qrcode.image.pil.PilImage
img.save("mail.png")