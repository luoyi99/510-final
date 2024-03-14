# Bookmark Assistant

The Bookmark Assistant is a Streamlit-based web application designed to help users manage their bookmarks effectively. 

## The Problem We're Solving
Bookmark Assistant tackles the common problem of managing an overwhelming number of browser bookmarks. Our solution provides an intelligent way to automatically generate tags, filter, and organize bookmarks, turning a cluttered bookmark bar into a neatly arranged, easily navigable repository.It also features a robust interface for filtering and managing bookmarks, making it an essential tool for users looking to streamline their web browsing experience.

## How to Run
To use the Bookmark Assistant, follow these steps:
1. Visit the online version at [https://bookmark-assistant.azurewebsites.net](https://bookmark-assistant.azurewebsites.net) or run it locally on your machine.
2. To run locally, ensure you have Streamlit installed. If not, install it using the command `pip install -r requirements.txt`.
3. Navigate to the application directory in your terminal or command prompt.
4. Run the app by executing `streamlit run app.py`.
5. The app will launch in your default web browser.

## What's Included
- `app.py`: The main application script that utilizes Streamlit for the web interface.
- `db.py`: Contains the database connection string and functions related to database operations.
- `scraper.py`: Handles web scraping functionalities, including retrieving page content and taking webpage screenshots.
- `gpt.py`: Utilizes a GPT model to generate relevant tags based on the content of the webpage.
- `requirements.txt`: Lists all the necessary Python packages to run the app.
- `display.py`: Handles saved bookmarks styling.

## Features
- **Automatic Tag Generation**: The app uses AI to analyze the content of the webpage and automatically generates relevant tags.
- **Bookmark Management Interface**: A user-friendly interface allows for easy addition, deletion, and organization of bookmarks.
- **Filtering and Sorting**: Users can filter their bookmarks based on tags, titles, or URLs and sort them according to their preferences.
- **Page Screenshot**: For each bookmark, the app captures and displays a screenshot of the webpage, providing a visual reference.

## Reflections: What we learned
- Learned how to integrate AI models with a web application to enhance functionality.
- Gained insights into building and managing a Streamlit app, including the use of Streamlit components like `st_tags` and `Modal`.
- Enhanced understanding of web scraping techniques and their applications in real-world projects.
- Developed skills in managing and displaying dynamic content in a web application interface.

## Reflections: What questions/problems did we face
- **AI Integration for Tag Generation**: One of the core features of Bookmark Assistant is its ability to generate relevant tags automatically using AI. Integrating this functionality posed several challenges, including selecting the right AI model, ensuring its accuracy in understanding and summarizing web content, and optimizing its performance to work in real-time without slowing down the app.

- **Web Scraping Accuracy**: Extracting content from various websites to generate tags required implementing robust web scraping techniques. We encountered challenges in dealing with websites that have dynamic content loaded by JavaScript, as well as handling rate limits and IP bans implemented by some sites to block scrapers.

- **User Data Privacy and Security**: Ensuring the privacy and security of user data, especially bookmarks which can contain sensitive information, was a significant concern. We faced questions on the best practices to encrypt user data, manage secure sessions, and protect against vulnerabilities such as SQL injection and Cross-Site Scripting (XSS).



## Future Exploration
- How to effectively scale the app to handle a large number of bookmarks without compromising performance?
- What is the best way for ensuring the privacy and security of every user's bookmark data?
- Exploring ways to improve the accuracy and relevance of automatically generated tags.

## Developer
Yi Luo，Margaret Lin，Yahan Xie
