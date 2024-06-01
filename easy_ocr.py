import easyocr
import json    
import os 

reader = easyocr.Reader(['en'], gpu=True)  # Specify the language(s) you want to recognize

l = os.listdir("./image_dataset/")


extracted_text = {}

def text_extracted(img_path):
    
# image_path = './image_dataset/0MRBE4KyXro.jpg'


    result = reader.readtext(img_path)


    for detection in result:
        extracted_text[img_path] = detection[1]


# image_path = './image_dataset/0MRBE4KyXro.jpg'


for i in l:
    text_extracted(f"./image_dataset/{i}")
    
    


with open("./extractedtext.json", 'w') as json_file:    
    json.dump(extracted_text, json_file, indent=4)
