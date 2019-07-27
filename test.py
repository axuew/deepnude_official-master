import pytesseract
from PIL import Image
image = Image.open('test.png')
code = pytesseract.image_to_string(image)
print(code)