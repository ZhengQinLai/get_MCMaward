import pdfplumber
import os
import time
import fitz
import pytesseract
from PIL import Image
import pandas as pd
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
num=2207155
path=str(num)+'.png'
file_name=str(num)+'.pdf'
doc = fitz.open(file_name)
pix = doc.load_page(0).get_pixmap()
pix.save(path)
img=Image.open(path)
text = pytesseract.image_to_string(img,'eng')
print(text)
if re.search("Honorable", text, flags=0):
    award='H'
elif re.search("Finalist", text, flags=0):
    award='F'
elif re.search("Outstanding", text, flags=0):
    award='O'
elif re.search("Meritorious", text, flags=0):
    award='M'
elif re.search("Disqualified", text, flags=0):
    award='Dq'
elif re.search("Successful", text, flags=0):
    award='S'
elif re.search("Unsuccessful", text, flags=0):
    award='U'
print(award)