# Bookmark Assistant

The Bookmark Assistant is a Streamlit-based web application designed to help users manage their bookmarks effectively. By automatically generating relevant tags for URLs entered by the user, the app enhances the organization and retrieval of bookmarks. It also features a robust interface for filtering and managing bookmarks, making it an essential tool for users looking to streamline their web browsing experience.

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

## Lessons Learned
- Learned how to integrate AI models with a web application to enhance functionality.
- Gained insights into building and managing a Streamlit app, including the use of Streamlit components like `st_tags` and `Modal`.
- Enhanced understanding of web scraping techniques and their applications in real-world projects.
- Developed skills in managing and displaying dynamic content in a web application interface.

## Future Exploration
- How to effectively scale the app to handle a large number of bookmarks without compromising performance?
- What is the best way for ensuring the privacy and security of every user's bookmark data?
- Exploring ways to improve the accuracy and relevance of automatically generated tags.
