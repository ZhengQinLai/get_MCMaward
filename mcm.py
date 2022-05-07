import requests
import pandas as pd
a=pd.read_excel(io=r"1.xlsx",sheet_name=0)
for num in a["Control Number"]:
    url = "https://www.comap-math.com/mcm/2022Certs/"+str(num)+".pdf"
    print(str(num)+"下载中")
    pdf = requests.get(url).content  #这里必须用.content而不能用text
    print(str(num)+"写入中")
    with open("./certificates/"+str(num)+".pdf", "wb") as f:
        print(num)
        f.write(pdf)
