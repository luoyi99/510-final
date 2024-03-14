import json
import datetime

import requests

from db import get_db_conn

from bs4 import BeautifulSoup
import json

from urllib.parse import urlencode
from urllib.request import urlretrieve
# q = '''
#     DELETE FROM webpages;
#     '''
# conn = get_db_conn()
# cur = conn.cursor()
# cur.execute(q)

def get_page_content(pagelink):

    r = requests.get(pagelink)
    html_content = r.text
 
    # parse html content
    soup = BeautifulSoup(html_content, "html.parser")
    try:
        title = soup.title.string
    except AttributeError:
        title = "No title"
 
    # for data in soup(['head','style', 'script','nav','header','footer']):
    for data in soup(['nav','style', 'script', 'head', 'title', 'meta', '[document]', 'header', 'footer', 'aside', 'form', 'input', 'select', 'option', 'label', 'textarea', 'svg', 'path', 'defs', 'g', 'use', 'symbol', 'rect', 'circle', 'clipPath', 'mask', 'pattern', 'line', 'polyline', 'polygon', 'ellipse', 'text', 'tspan', 'textPath', 'image', 'pattern', 'filter', 'foreignObject', 'linearGradient', 'radialGradient', 'stop', 'view', 'a', 'link', 'style', 'noscript', 'iframe', 'embed', 'object', 'param', 'video', 'audio', 'source', 'track', 'canvas', 'map', 'area', 'table', 'caption', 'colgroup', 'col', 'tbody', 'thead', 'tfoot', 'tr', 'td', 'th', 'table', 'caption', 'colgroup', 'col', 'tbody', 'thead', 'tfoot', 'tr', 'td', 'th', 'table', 'caption', 'colgroup', 'col', 'tbody', 'thead', 'tfoot', 'tr', 'td', 'th', 'table', 'caption', 'colgroup', 'col', 'tbody', 'thead', 'tfoot', 'tr', 'td', 'th', 'table', 'caption', 'colgroup', 'col', 'tbody', 'thead', 'tfoot', 'tr', 'td', 'th', 'table', 'caption', 'colgroup', 'col', 'tbody', 'thead', 'tfoot', 'tr', 'td', 'th', 'table', 'caption', 'colgroup', 'col', 'tbody', 'thead', 'tfoot', 'tr', 'td', 'th', 'table', 'caption', 'colgroup', 'col', 'tbody', 'thead', 'tfoot', 'tr', 'td', 'th', 'table', 'caption', 'colgroup', 'col', 'tbody', 'thead', 'tfoot', 'tr', 'td', 'th', 'table', 'caption', 'colgroup', 'col', 'tbody', 'thead', 'tfoot', 'tr', 'td', 'th', 'table', 'caption', 'colgroup', 'col', 'tbody', 'thead', 'tfoot', 'tr', 'td']):
        
        # Remove tags
        data.decompose()
 
    # return data by retrieving the tag content
    return [title,' '.join(soup.stripped_strings)]


def get_page_screenshot(pagelink):   
    params = urlencode(dict(access_key="312547eec671428e93dbe34de811903e",
                            url=pagelink,response_type="json"))
    urlretrieve("https://api.apiflash.com/v1/urltoimage?" + params, "data/screenshot.json")
    image_link = json.load(open('data/screenshot.json', 'r'))['url']
    return image_link


def insert_to_pg(data):
    q = '''
    CREATE TABLE IF NOT EXISTS webpages (
        url TEXT PRIMARY KEY,
        title TEXT,
        date TIMESTAMP WITH TIME ZONE,
        tags TEXT[],
        image TEXT,
        content TEXT
    );
    '''
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(q)

    q = '''
    INSERT INTO webpages (url, title, date, tags, image, content)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON CONFLICT (url) DO NOTHING;
    '''
    cur.execute(q, (data['url'], data['title'], data['date'] , data['tags'], data['image'], data['content']))


def merge_page_data(pagelink,title,page_content,image_link,tags,date):

    data = {"url":pagelink, "title":title, "tags":tags, "date":date, "image": image_link, "content":page_content}
    return data


def get_saved_pages(sort_by, selected_tag = None):
    if sort_by == "Oldest to Newest":
        order = "date ASC"
    elif sort_by == "Newest to Oldest":
        order = "date DESC"
    elif sort_by == "Title A-Z":
        order = "title ASC"
    elif sort_by == "Title Z-A":
        order = "title DESC"

    if not selected_tag:
        q = f'''
        SELECT * FROM webpages
        ORDER BY {order};
        '''
    else:
        q = f'''
        SELECT * FROM webpages
        WHERE tags && ARRAY{selected_tag}
        ORDER BY {order};
        '''
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(q)
    return cur.fetchall()

def get_all_tags():
    q = '''
    SELECT tags FROM webpages;
    '''
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(q)
    all_tags = cur.fetchall()
    tags = set()
    for tag in all_tags:
        tags.update(tag[0])
    
    return list(tags)

def delete_page(url):
    q = '''
    DELETE FROM webpages
    WHERE url = %s;
    '''
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(q, (url,))