from urllib.request import urlopen
from bs4 import BeautifulSoup #Camel Case
import pyexcel

# 1. Download dantri home page
webpage = urlopen('http://dantri.com.vn') #Open connection
data = webpage.read()
html_content = data.decode('utf8')
# print(html_content)
# 2. Analyze ROI aka Region of Interest
# 2.1 Create Beautiful soup
soup = BeautifulSoup(html_content, 'html.parser')
ul = soup.find('ul', 'ul1 ulnew') # find one
li_list = ul.find_all('li')
# for li in li_list:
#     print(li.prettify())
#     print("* " * 20)
news_list = []

for li in li_list:
    h4 = li.h4 # find('h4')
    a = h4.a # find('a')
    news = {
        'title': a.string,
        'link': 'http://dantri.com' + a['href']
    }
    news_list.append(news)
pyexcel.save_as(records = news_list, dest_file_name = 'dantri.xlsx')

# 3. Extract data from ROI
