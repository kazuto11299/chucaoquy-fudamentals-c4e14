from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

webpage = urlopen('https://www.nhaccuatui.com/bai-hat/top-20.au-my.html')
data = webpage.read()
html_content = data.decode('utf8')
soup = BeautifulSoup(html_content, 'html.parser')
ul = soup.find('ul', 'list_show_chart')
li_list = ul.find_all('li')
for li in li_list:
    a = soup.find('li', 'list_name_singer')
    print(li.a.prettify())
    print("* " * 20)
news_list = []
lis = soup.find('li', 'h3')
li_lists = lis.find_all('h3')
for lit in li_lists:
    h3 = lit.h3
    b = h3.b
    h3.find_all('b')
    news = {
        'author': b.string,
        'song': '' + b['href']
    }
    news_list.append(news)
pyexcel.save_as(records = news_list, dest_file_name = 'nct.xlsx')
