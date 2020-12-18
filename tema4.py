# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
#
#
# req = requests.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-3-aprilie-2020-ora-13-00/')
#
#
# response = req.text
# link = BeautifulSoup(response, 'html.parser')
# title = link.find_all('div', attrs={'class': 'entry-content'})
#
# print(title)
#
# header = []
# data_list = []
# set_td = set()
# header_html = ''
# # tbody_html = ''
# td = ''
# tr = ''
# table = ''
# thead = ''
#
#
# for i in title:
#     for tr_index in i.find_all('table'):
#         for td_index in tr_index.find_all('tr'):
#             list_td = list()
#             td = ''
#
#             for th_index in td_index.find_all('th'):
#                 header.append(th_index.get_text())
#                 header_html += f'<th>{th_index.get_text()}</th>'
#             thead = f'<thead><tr>{header_html}</tr></thead>'
#             for trd_index in td_index.find_all('td'):
#                 list_td.append(trd_index.get_text().lstrip(' '))
#                 td += f'<td>{trd_index.get_text().lstrip(" ")}</td>'
#
#             tr += f'<tr>{td}</tr>'
#             data_list.append(tuple(list_td))
#
#             for th_index in td_index.find_all('th'):
#                 header.append(th_index.get_text())
#                 header_html += f'<th>{th_index.get_text()}</th>'
#             thead = f'<thead><tr>{header_html}</tr></thead>'
#             for trd_index in td_index.find_all('td'):
#                 list_td.append(trd_index.get_text().lstrip(' '))
#                 td += f'<td>{trd_index.get_text().lstrip(" ")}</td>'
#             tr += f'<tr>{td}</tr>'
#             data_list.append(tuple(list_td))
# table = f'<table>{thead}<tbody>{tr}</tbody></table>'
#
# #html
# file = open('C:\\Users\\alexb\\OneDrive\\fileTema.html', 'w')
# file.writelines(table)
# file.close()
#

import requests
from bs4 import BeautifulSoup
import pandas as pd

req = requests.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-3-aprilie-2020-ora-13-00/')
response = req.text

# print(response)
link = BeautifulSoup(response, 'html.parser')
title = link.find_all('div', attrs={'class': 'entry-content'})
# print(title)


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
                header.append(th_index.get_text())  # get text ne ia textul din elementul de th
                header_html += f'<th>{th_index.get_text()}</th>'
            thead = f'<thead><tr>{header_html}</tr></thead>'
            for trd_index in td_index.find_all('td'):
                list_td.append(trd_index.get_text().lstrip(' '))
                td += f'<td>{trd_index.get_text().lstrip(" ")}</td>'
            tr += f'<tr>{td}</tr>'
            data_list.append(tuple(list_td))

table = f'<table>{thead}<tbody>{tr}</tbody></table>'
# print(data_list)


file = open('C:\\Users\\alexb\\OneDrive\\asdfile.html', 'w')
file.writelines(table)
file.close()