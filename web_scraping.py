import requests
from bs4 import BeautifulSoup

# Step 1: Define the URL of the website you want to scrape
url = 'http://books.toscrape.com/catalogue/page-1.html'

# Step 2: Send a GET request to fetch the webpage content
response = requests.get(url)

# Step 3: Check if the request was successful
if response.status_code == 200:
    # Step 4: Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Step 5: Find all book containers on the page
    books = soup.find_all('article', class_='product_pod')

    # Step 6: Loop through each book and extract title and rating
    for book in books:
        title = book.h3.a['title']  # Extract the title
        rating = book.find('p', class_='star-rating')['class'][1]  # Extract the rating class
        
        # Print the title and rating
        print(f'The Title of the Book is : {title}, and its Rating: {rating}')
else:
    print("Failed to retrieve the webpage.")