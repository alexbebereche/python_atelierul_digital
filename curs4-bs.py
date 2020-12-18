import requests
from bs4 import BeautifulSoup
import pandas as pd

req = requests.get('https://www.bnr.ro/Cursul-de-schimb--7372.aspx')
response = req.text


# print(response)
link = BeautifulSoup(response, 'html.parser')
title = link.find_all('div', attrs = {'class': 'contentDiv'})
# print(title)


"""
<table>
    <thead>
        <tr>
            <th></th>
            <th></th>
        </tr>
        
    </thead>
    <tbody>
        <tr>
        </tr>
        <tr>
        </tr>
    </tbody>
</table>

"""

header = []
data_list = []
set_td = set()
header_html = ''
tbody_html = ''
td = ''
tr = ''
table = ''
thead = ''

for i in title:
    for tr_index in i.find_all('table'):
        for td_index in tr_index.find_all('tr'):
            list_td = list()
            td = ''

            for th_index in td_index.find_all('th'):
                header.append(th_index.get_text())  #get text ne ia textul din elementul de th
                header_html += f'<th>{th_index.get_text()}</th>'
            thead = f'<thead><tr>{header_html}</tr></thead>'
            for trd_index in td_index.find_all('td'):
                list_td.append(trd_index.get_text().lstrip(' '))
                td += f'<td>{trd_index.get_text().lstrip(" ")}</td>'
                # header.append(trd_index.get_text().lstrip(' '))
                # header_html += f'<td>{trd_index.get_text().lstrip(" ")}</td>'
            tr += f'<tr>{td}</tr>'
            data_list.append(tuple(list_td))

table = f'<table>{thead}<tbody>{tr}</tbody></table>'
# print(data_list)
#html
# file = open('C:\\Users\\alexb\\Desktop\\fileGoogle.html', 'w')

file = open('C:\\Users\\alexb\\OneDrive\\fileGoogle.html', 'w')
file.writelines(table)
file.close()


#excel
df = pd.DataFrame(data_list, columns = header)
df.to_excel('CursBNR_ExcelGoogle.xls', sheet_name = 'BNR', header = header, index = 0) #index = 0 => nu imi trece index in coloana
#df.to_excel('CursBNR_ExcelGoogle.xls', sheet_name = 'BNR', header = header)