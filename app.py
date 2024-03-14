import streamlit as st
from streamlit_modal import Modal
from streamlit_tags import st_tags
import datetime


from db import conn_str
from scraper import insert_to_pg, get_page_content, merge_page_data, get_page_screenshot, get_saved_pages, get_all_tags, delete_page
from gpt import get_tags
from display import display_bookmarks

# test URLs
# url = "https://docs.edgeimpulse.com/docs/"
# url2= "https://www.geeksforgeeks.org/remove-all-style-scripts-and-html-tags-using-beautifulsoup/"
# url3= "https://ollama.com/blog"


# def filter_bookmarks(tags):
#     if not tags:
#         return bookmarks
#     filtered = []
#     for bookmark in bookmarks:
#         if any(tag in bookmark['tags'] for tag in tags):
#             filtered.append(bookmark)
#     return filtered


page = st.sidebar.radio("Go to", ('Homepage', 'History'))


if page == 'Homepage':
    
    st.title("Bookmark Assistant")

    # Add bookmarked pages
    pagelink = st.text_input(
        "Enter a webpage URL",
        label_visibility='hidden',
        placeholder='Enter a webpage URL',
        key='add_url'
    )

    # popup window for information confirmation
    modal = Modal(
        "Page Info", 
        key="page_info_modal",
        
        # Optional
        padding=20,
        max_width=744  # default value
    )

    # open the popup window when the "Upload" button is clicked
    open_modal = st.button("Upload")

    if open_modal:
        modal.open()

    if modal.is_open(): # if the popup window is open
        with modal.container():
            with st.spinner("Loading..."): # display a loading spinner while loading information
                page_info = get_page_content(pagelink)
                generated_tags = get_tags(page_info[1][:1000])
                image_link = get_page_screenshot(pagelink)
                date = datetime.datetime.now().strftime('%Y-%m-%d')
            
            # display website screenshot in the middle
            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                st.image(image_link)
            
            # display website information
            st.write("Page link: ",pagelink)
            title = st.text_input("Title:", page_info[0])
            tags = st_tags(
                        label='Tags:',
                        text='Press enter to add more',
                        value=generated_tags,
                        key='add_tags')

            # display "save" button in the middle
            col1, col2, col3 , col4, col5 = st.columns(5)
            with col1:
                pass
            with col2:
                pass
            with col3:
                if st.button("Save", type="primary",use_container_width=True):
                    data = merge_page_data(pagelink,title,page_info[1],image_link,tags,date)
                    insert_to_pg(data)
                    modal.close()
            with col4:
                pass
            with col5:
                pass
    
    st.divider()

    st.subheader("Saved Pages")

    col1, col2 = st.columns([1, 2])
    
    all_tags = get_all_tags()

    with col1:
        # 下拉框滤镜
        sort_by = st.selectbox('Sort by', options=["Newest to Oldest", "Oldest to Newest", "Title A-Z", "Title Z-A"], index=0)

    with col2:
        # 关键词搜索栏
        selected_tags = st.multiselect(
            'Filter by Tags',
            options=all_tags)
    
    bookmarks = get_saved_pages(sort_by, selected_tags)
    display_bookmarks(bookmarks)

    

elif page == 'History':
    st.title('Search and Filter Bookmarks')
    all_tags = get_all_tags()
    selected_tags = st.multiselect(
            'Enter Keywords:',
            options=all_tags)
    bookmarks = get_saved_pages("Newest to Oldest", selected_tags)
    display_bookmarks(bookmarks)