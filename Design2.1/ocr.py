from PIL import Image
import os

I = Image.open('img.png')
L = I.convert('L')
L.save("img_b.png")