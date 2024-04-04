import requests
import os
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# Function to download a PDF given its URL and desired file name
def download_pdf(url, folder):
    # Send a request to the URL and follow redirections
    response = requests.head(url, allow_redirects=True)
    # Extract the final URL after following the redirections
    final_url = response.url
    # Extract the filename from the final URL
    filename = os.path.basename(urlparse(final_url).path)
    # Construct the file path
    file_path = os.path.join(folder, filename)
    # Download the PDF file
    with open(file_path, 'wb') as f:
        response = requests.get(final_url)
        f.write(response.content)
    print(f"Downloaded: {filename}")

# Base URL of the webpage containing the links to the PDF reports
base_url = "https://www.dmv.ca.gov"

# Make a GET request to fetch the webpage
response = requests.get(f"{base_url}/portal/vehicle-industry-services/autonomous-vehicles/autonomous-vehicle-collision-reports/")

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the <a> tags containing links to PDF reports
pdf_links = soup.find_all('a', href=lambda href: (href and href.endswith('-pdf')))

# Create a folder to save the downloaded PDFs
folder = "data/collisions"
if not os.path.exists(folder):
    os.makedirs(folder)

# Download each PDF report
for link in pdf_links:
    # Construct the complete URL by appending the relative URL to the base URL
    pdf_url = base_url + link['href']
    download_pdf(pdf_url, folder)
