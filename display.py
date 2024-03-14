import streamlit as st
from itertools import cycle
import datetime
from hashlib import md5
import hashlib



colors = ['#026E81', '#00ABBD', '#0099DD', '#FF9933', '#A1C7E0','#F19483','#572A3F']

def generate_tag_color(tag):
    # 使用标签文本的哈希值来选择颜色
    hash_code = int(hashlib.md5(tag.encode()).hexdigest(), 16)
    # 使用哈希值对颜色列表的长度取余，以选择一个颜色
    color_index = hash_code % len(colors)
    return colors[color_index]

def display_bookmarks(bookmarks):
    # CSS for styling the bookmarks
    st.markdown("""
    <style>
    .bookmark-card {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        width: 100%;
        margin-bottom: 20px;
    }
    .bookmark-card img {
        border-radius: 10px;
        margin-right: 10px;
        align-self: center;
        padding: 10px;
    }
    .bookmark-content {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        padding:10px 15px 10px 15px;
        width: 100%;
    }
    .bookmark-tag {
        display: inline-block;
        margin: 2px;
        padding: 2px 5px;
        border-radius: 3px;
        color: white;
        font-size: 12px;
    }
    .bookmark-title {
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    # Display bookmarks in two columns
    cols = cycle(st.columns(2))
    for bookmark in bookmarks:
        image = bookmark[4]
        title = bookmark[1]
        url = bookmark[0]
        tags = bookmark[3]
        date = datetime.datetime.strftime(bookmark[2], '%Y-%m-%d')
        with next(cols):
            tags_html = ' '.join(f'<span class="bookmark-tag" style="background-color: {generate_tag_color(tag)};">{tag}</span>' for tag in tags)
            st.markdown(f"""
                <div class="bookmark-card">
                    <img src="{image}" alt="Bookmark Image" width=90% >
                    <div class="bookmark-content">
                        <div class="bookmark-title">{title}</div>
                        <div class="bookmark-url"><a href={url} target="_blank">{url}</a ></div>
                        <div class="bookmark-tags">{tags_html}</div>
                        <div class="bookmark-date">Date: {date}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)




