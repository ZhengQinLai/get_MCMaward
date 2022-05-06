import requests
import pandas as pd
a=pd.read_excel(io=r"1.xlsx",sheet_name=0)
for num in [2207171,2207254,2207336,2207365,2207369,2207375,2207376,2207384,2207395,2207415,2207592,2207654,2207707,2207718,2207721,2207722,2207732,2207738,2207739,2207872,2208053,2208059,2208066,2208071,2208084,2208522,2208535,2208539,2208550,2208552,2208564,2208573,2208579]:
    url = "https://www.comap-math.com/mcm/2022Certs/"+str(num)+".pdf"
    print(str(num)+"下载中")
    pdf = requests.get(url).content  #这里必须用.content而不能用text
    print(str(num)+"写入中")
    with open(str(num)+".pdf", "wb") as f:
        print(num)
        f.write(pdf)


print(requests.get('http://ifconfig.me/ip').text)