import qrcode

data = 'Hello World'
img = qrcode.make(data)
img.save('C:/Users/maxim/OneDrive/Desktop/New folder (2)/myqrcode.png')
