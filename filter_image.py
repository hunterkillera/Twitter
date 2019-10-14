import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image
import os
import cv2
import glob

folders = glob.glob('D:\Twitter\image')
imagenames__list = []
for folder in folders:
    for f in glob.glob(folder+'/*.jpg'):
        imagenames__list.append(f)

read_images = []
for image in imagenames__list:
    read_images.append(cv2.imread(image, cv2.IMREAD_GRAYSCALE))

#images = [cv2.imread(file) for file in glob.glob("path/to/files/*.png")]
    images = Image.open(image)
    text = pytesseract.image_to_string(images)
    if len(text) >10:
        os.remove(image)
    print(text)