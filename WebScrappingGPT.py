import requests
from bs4 import BeautifulSoup
import os

# Function to create a directory if it doesn't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to download images
def download_image(url, directory):
    img_name = url.split("/")[-1]
    with open(os.path.join(directory, img_name), 'wb') as f:
        f.write(requests.get(url).content)

# URL of the website to scrape images from
url = "https://www.google.com"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Create a directory to save the images
image_directory = "images"
create_directory(image_directory)

# Find all img tags on the webpage
img_tags = soup.find_all('img')

# Iterate through each img tag and download the image
for img in img_tags:
    img_url = img.get('src')
    if img_url:
        if not img_url.startswith("http"):
            img_url = url + img_url
        download_image(img_url, image_directory)
