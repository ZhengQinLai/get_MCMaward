import pdfplumber
import os
import time
import fitz
import pytesseract
from PIL import Image
import pandas as pd
import re
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
num=2207691
path=str(num)+'.png'
file_name="./certificates/"+str(num)+'.pdf'
try:
    doc = fitz.open(file_name)
except fitz.fitz.FileDataError:
    award="Do not find"
pix = doc.load_page(0).get_pixmap()
pix.save(path)
img=Image.open(path)
text = pytesseract.image_to_string(img,'eng')
os.remove(path)
print(len(text.split("\n")))
print(text.split("\n"))