
import pyqrcode 
from pyqrcode import QRCode 
  
  
# String which represent the QR code 
s = "Specs"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("specs.svg", scale = 8) 