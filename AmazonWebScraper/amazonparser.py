
import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.in/Dell-Inspiron-5370-13-3-inch-Windows/dp/B079P2X5R6/ref=sr_1_3?_encoding=UTF8&m=A14CZOWI0VEHLG&pf_rd_i=desktop&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=9806b2c4-09c8-4373-b954-bae25b7ea046&pf_rd_r=27V7KJQJXY8QTDQ27YAH&pf_rd_t=36701&qid=1554104280&refinements=p_6%3AA14CZOWI0VEHLG&s=computers&smid=A14CZOWI0VEHLG&sr=1-3"
page = requests.get(URL,headers={"User-Agent":"Defined"})
soup = BeautifulSoup(page.content, "html.parser")

price = soup.find_all( attrs =  {'class': ['priceBlockStrikePriceString']})

title =soup.find(id="productTitle").get_text()
availability =soup.find(id="availability").get_text()
regularprice_savings =soup.find(id="regularprice_savings").get_text()


print(title)
print("M.R.P "+ price[0].text)

print(regularprice_savings)

print(availability)