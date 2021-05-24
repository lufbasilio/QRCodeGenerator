import png
import pyqrcode
from pyqrcode import QRCode

file = open ("arquivo.txt" )
for line in file.readlines():

    s = line

    Stringformat = s.replace("\n","")
    url = pyqrcode.create(Stringformat)
    url.png(Stringformat+'.png',scale=6)

file.close()
