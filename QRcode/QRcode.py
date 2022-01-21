import qrcode

img = qrcode.make("Hello World ! ! !\nMy name is Aaquib Kudchikar :)\nI live in INDIA and love to go on adventures.")
img.save("hello.jpg")