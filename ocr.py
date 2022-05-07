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
a.insert(a.shape[1],'University',0)
a=a.set_index("Control Number",drop=False)
for num in a["Control Number"]:
    path=str(num)+'.png'
    file_name="./certificates/"+str(num)+'.pdf'
    try:
        doc = fitz.open(file_name)
    except fitz.fitz.FileDataError:
        award="Do not find,Maybe U"
        a.loc[num,'award']=award
        continue
    pix = doc.load_page(0).get_pixmap()
    pix.save(path)
    img=Image.open(path)
    text = pytesseract.image_to_string(img,'eng').split("\n")
    os.remove(path)
    i=len(text)-3
    while(text[i]==''):
        i=i-1
    award=text[i]
    i=i-2
    while(text[i]==''):
        i=i-1
    univer=text[i]
    i=0
    while(text[i].lower()!='be it known that the team of'):
        i=i+1
    i=i+1
    while(text[i]==''):
        i=i+1
    Team=[]
    while(text[i].lower()!=''and text[i].lower()!='with faculty advisor'):
        Team.append(text[i])
        i=i+1
    a.loc[num,'award']=award
    a.loc[num,'University']=univer
    for n in range(len(Team)):
        a.loc[num,'Teammate'+str(n+1)]=Team[n]
    print(num)
a.to_csv("./award.csv",encoding='utf-8-sig',index=True)
    


