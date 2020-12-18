import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import matplotlib.pyplot as plt

browser = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')  #sau r'' in loc de \\
browser.get('https://www.bnr.ro/files/xml/nbrfxrates2019.htm') #htm, nu html lol
table = browser.find_element_by_xpath('//*[@id="Data_table"]') #//*[@id="Data_table"]

#salvare in txt
# fisier = open('curs_valutar_bnr_google.txt', 'w+')
# fisier.writelines(table.text)
# fisier.close()

tabel = table.text
lista = tabel.split('\n')

header_len = browser.find_element_by_xpath('//*[@id="Data_table"]/table/thead/tr') #/html/body/div[4]/table/thead
header = header_len.text.split('\n')
dictionar = {i: [] for i in header}


for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        if '-' in lista[i]:
            dictionar[header[int(j)]].append(lista[i])
        else:
            dictionar[header[int(j)]].append(float(lista[i]))


print(dictionar)
df = pd.DataFrame(dictionar)
df.to_excel("BNR_ALL_VALUES_GOOGLE.xls")

browser.close()

#eroare, '' in loc de "" era eraorea lol


a = header[3:9]
c = []
for i in range(3,9):
    c.append(dictionar[header[int(i)]][int(i)])
d = sum(c)
e = []
for item in c:
    e.append(round(item/d*100))

colors = ['r', 'y', 'g', 'b', 'g', 'y']

plt.pie(e, labels = a, colors = colors, startangle=90, shadow=True, explode=(0.1, 0.1, 0.1, 0.1,0.1, 0.2),
        radius=1.2, autopct='%1.1f%%')

plt.legend()
plt.show()

#preluam de pe un site niste date cu ajutorul selenium-ului