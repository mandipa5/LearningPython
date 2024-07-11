import qrcode
##QRLink
wifi_type = "WPA"
wifi_ssid = "netis_2.4G_AA6CD7"
wifi_password = "password"
wifi = f"WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};;"
img = qrcode.make(wifi)
type(img)  # qrcode.image.pil.PilImage
img.save("wifi.png")