import re
import json
import datetime
from zoneinfo import ZoneInfo
import html

import requests

from db import get_db_conn

from bs4 import BeautifulSoup
from bs4.element import Comment
import json

from urllib.parse import urlencode
from urllib.request import urlretrieve


# URL = 'https://visitseattle.org/events/page/'
# URL_LIST_FILE = './data/links.json'
# URL_DETAIL_FILE = './data/data.json'

# def list_links():
#     res = requests.get(URL + '1/')
#     last_page_no = int(re.findall(r'bpn-last-page-link"><a href=".+?/page/(\d+?)/.+" title="Navigate to last page">', res.text)[0])

#     links = []
#     for page_no in range(1, last_page_no + 1):
#         res = requests.get(URL + str(page_no) + '/')
#         links.extend(re.findall(r'<h3 class="event-title"><a href="(https://visitseattle.org/events/.+?/)" title=".+?">.+?</a></h3>', res.text))

#     json.dump(links, open(URL_LIST_FILE, 'w'))

# def get_detail_page():
#     links = json.load(open(URL_LIST_FILE, 'r'))
#     data = []
#     for link in links:
#         try:
#             row = {}
#             res = requests.get(link)
#             row['title'] = html.unescape(re.findall(r'<h1 class="page-title" itemprop="headline">(.+?)</h1>', res.text)[0])
#             datetime_venue = re.findall(r'<h4><span>.*?(\d{1,2}/\d{1,2}/\d{4})</span> \| <span>(.+?)</span></h4>', res.text)[0]
#             row['date'] = datetime.datetime.strptime(datetime_venue[0], '%m/%d/%Y').replace(tzinfo=ZoneInfo('America/Los_Angeles')).isoformat()
#             row['venue'] = datetime_venue[1].strip() # remove leading/trailing whitespaces
#             metas = re.findall(r'<a href=".+?" class="button big medium black category">(.+?)</a>', res.text)
#             row['category'] = html.unescape(metas[0])
#             row['location'] = metas[1]
#             data.append(row)
#         except IndexError as e:
#             print(f'Error: {e}')
#             print(f'Link: {link}')
#     json.dump(data, open(URL_DETAIL_FILE, 'w'))



url = "https://docs.edgeimpulse.com/docs/"

url2= "https://www.geeksforgeeks.org/remove-all-style-scripts-and-html-tags-using-beautifulsoup/"

url3= "https://ollama.com/blog"


# r = requests.get(url2)

# html_content = r.text

def remove_tags(html):
 
    # parse html content
    soup = BeautifulSoup(html, "html.parser")
 
    # for data in soup(['head','style', 'script','nav','header','footer']):
    for data in soup(['nav','style', 'script', 'head', 'title', 'meta', '[document]', 'header', 'footer', 'aside', 'form', 'input', 'select', 'option', 'label', 'textarea', 'svg', 'path', 'defs', 'g', 'use', 'symbol', 'rect', 'circle', 'clipPath', 'mask', 'pattern', 'line', 'polyline', 'polygon', 'ellipse', 'text', 'tspan', 'textPath', 'image', 'pattern', 'filter', 'foreignObject', 'linearGradient', 'radialGradient', 'stop', 'view', 'a', 'link', 'style', 'noscript', 'iframe', 'embed', 'object', 'param', 'video', 'audio', 'source', 'track', 'canvas', 'map', 'area', 'table', 'caption', 'colgroup', 'col', 'tbody', 'thead', 'tfoot', 'tr', 'td', 'th', 'table', 'caption', 'colgroup', 'col', 'tbody', 'thead', 'tfoot', 'tr', 'td', 'th', 'table', 'caption', 'colgroup', 'col', 'tbody', 'thead', 'tfoot', 'tr', 'td', 'th', 'table', 'caption', 'colgroup', 'col', 'tbody', 'thead', 'tfoot', 'tr', 'td', 'th', 'table', 'caption', 'colgroup', 'col', 'tbody', 'thead', 'tfoot', 'tr', 'td', 'th', 'table', 'caption', 'colgroup', 'col', 'tbody', 'thead', 'tfoot', 'tr', 'td', 'th', 'table', 'caption', 'colgroup', 'col', 'tbody', 'thead', 'tfoot', 'tr', 'td', 'th', 'table', 'caption', 'colgroup', 'col', 'tbody', 'thead', 'tfoot', 'tr', 'td', 'th', 'table', 'caption', 'colgroup', 'col', 'tbody', 'thead', 'tfoot', 'tr', 'td', 'th', 'table', 'caption', 'colgroup', 'col', 'tbody', 'thead', 'tfoot', 'tr', 'td', 'th', 'table', 'caption', 'colgroup', 'col', 'tbody', 'thead', 'tfoot', 'tr', 'td']):
        
        # Remove tags
        data.decompose()
 
    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)
# print(remove_tags(html_content))


# ## get html screenshot
# params = urlencode(dict(access_key="312547eec671428e93dbe34de811903e",
#                         url="https://google.com",response_type="json"))
# urlretrieve("https://api.apiflash.com/v1/urltoimage?" + params, "screenshot.json")


def insert_to_pg():
    q = '''
    CREATE TABLE IF NOT EXISTS webpages (
        url TEXT PRIMARY KEY,
        title TEXT,
        date TIMESTAMP WITH TIME ZONE,
        tags TEXT[],
        image TEXT
    );
    '''
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(q)

    # image_link = json.load(open(data['image'], 'r'))
    image_link = json.load(open('screenshot.json', 'r'))['url']


    print(image_link['url'])

    # q = '''
    # INSERT INTO webpages (url, title, date, tags, image)
    # VALUES (%s, %s, %s, %s, %s)
    # ON CONFLICT (url) DO NOTHING;
    # '''
    # cur.execute(q, (data['url'], data['title'], data['date'], data['tags'], image))
insert_to_pg()
# if __name__ == '__main__':
#     list_links()
#     get_detail_page()
#     insert_to_pg()


def get_html_file(url):
    res = requests.get(url)
    with open('data.html', 'w') as f:
        f.write(res.text)

# def get_detail_page(url):
#     data = []
#     try:
#         row = {}
#         res = requests.get(url)
#         row['title'] = html.unescape(re.findall(r'<h1 class="page-title" itemprop="headline">(.+?)</h1>', res.text)[0])
#         datetime_venue = re.findall(r'<h4><span>.*?(\d{1,2}/\d{1,2}/\d{4})</span> \| <span>(.+?)</span></h4>', res.text)[0]
#         row['date'] = datetime.datetime.strptime(datetime_venue[0], '%m/%d/%Y').replace(tzinfo=ZoneInfo('America/Los_Angeles')).isoformat()
#         row['venue'] = datetime_venue[1].strip() # remove leading/trailing whitespaces
#         metas = re.findall(r'<a href=".+?" class="button big medium black category">(.+?)</a>', res.text)
#         row['category'] = html.unescape(metas[0])
#         row['location'] = metas[1]
#         data.append(row)
#     except IndexError as e:
#         print(f'Error: {e}')
#         print(f'Link: {link}')
#     json.dump(data, open(URL_DETAIL_FILE, 'w'))
