import qrcode
img = qrcode.make('Mandipa Thapa')
type(img)  # qrcode.image.pil.PilImage
img.save("mandipa.png")
