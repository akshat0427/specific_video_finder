#  pytesseract

from PIL import Image
import json
import pytesseract
from natsort import natsorted
import os

# If Tesseract is not in your PATH, include the following line with the path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'



l = os.listdir("./image_dataset/")




# Open an image file

result = {}

for i in l:
    
    image_path = f'./image_dataset/{i}'

    image = Image.open(image_path)
    
    text = pytesseract.image_to_string(image)

    result[i] = text
    

with open("./extractedtext2.json", 'w') as json_file:
    
    json.dump(result, json_file, indent=4)