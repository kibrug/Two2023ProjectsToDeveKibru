# text recognition
import cv2
import pytesseract
# read image
img = cv2.imread('photo.png')

# configurations
#config = ('-l eng --oem 1 --psm 3')
# pytesseract path
config=pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

text = pytesseract.image_to_string(img, config=config)

# print results
text = text.split('\n')
print(text)