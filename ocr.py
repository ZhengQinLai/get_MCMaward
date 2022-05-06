import pdfplumber
import os
import time
import fitz
import pytesseract
from PIL import Image
import pandas as pd
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
a=pd.read_excel(io=r"1.xlsx",sheet_name=0)
a.insert(a.shape[1], 'award', 0)
a=a.set_index("Control Number",drop=False)
for num in a["Control Number"]:
    path=str(num)+'.png'
    file_name=str(num)+'.pdf'
    try:
        doc = fitz.open(file_name)
    except fitz.fitz.FileDataError:
        award="Do not find"
        a.loc[num,'award']=award
        continue
    pix = doc.load_page(0).get_pixmap()
    pix.save(path)
    img=Image.open(path)
    text = pytesseract.image_to_string(img,'eng')
    os.remove(path)
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
    a.loc[num,'award']=award
    print(num)
a.to_csv("./award.csv",encoding='utf-8-sig',index=True)
    


