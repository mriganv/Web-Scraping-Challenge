from splinter import Browser
import pandas as pd
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager


def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    ##########################################################################################################################################

    ################################################
    # Latest news title and Latest news paragraph
    ################################################

    # Visit https://redplanetscience.com/
    url = "https://redplanetscience.com/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Get the Latest news title
    Latest_news_title = soup.find_all('div', class_='content_title')[0].text

    # Get the Latest news paragraph
    Latest_news_paragraph = soup.find_all('div', class_='article_teaser_body')[0].text

##############################################################################################################################################

    ######################### 
    # Featured Image url
    #########################

    url = "https://spaceimages-mars.com/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    for div in soup.find_all('div', class_='floating_text_area'):
        a = div.find('a')
        image = a['href']
    
    # Get the featured image url
    Featured_image_url = 'https://spaceimages-mars.com/' + image


#################################################################################################################################################

    ########################
    # Mars Facts Table
    ########################

    url = "https://galaxyfacts-mars.com"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    tables = pd.read_html(url)
    type(tables)

    df = tables[1]
    df.columns = ['Mars Planet Profile', 'Values']

    Mars_facts_html_table = df.to_html(index=False, header=False, border=0, classes="table table-sm table-striped font-weight: bold;")


#################################################################################################################################################

    #######################
    # Hemisphere Images
    #######################

    url = 'https://marshemispheres.com/'
    browser.visit(url)

    time.sleep(1)

    html = browser.html

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find_all('div', class_='description')

    Hemisphere_img_urls = []

    # Loop through returned results
    for result in results:
        # Error handling
        try:
            # Identify and return title of listing
            title = result.find('h3').text
            # get the image link
            img_link = result.a['href']
            url = f"https://marshemispheres.com/" + img_link
            browser.visit(url)
            html = browser.html
            soup = BeautifulSoup(html, 'html.parser')
            output = soup.find('img', class_="wide-image")
            download_link = output['src']
            img_url = f"https://marshemispheres.com/" + download_link
            # Append the title and Image url to the Hemisphere_img_urls dictionary 
            if (title and download_link):
                    hemis_dictionary = {
                    'Title': title,
                    'img_url': img_url}

                    Hemisphere_img_urls.append(hemis_dictionary)

        except Exception as e:
            print(e)

    # Create dictionary for all info scraped from sources above
    Mars_data = {
        "Latest_news_title": Latest_news_title,
        "Latest_news_paragraph": Latest_news_paragraph,
        "Featured_image_url": Featured_image_url,
        "Mars_facts_html_table": Mars_facts_html_table,
        "Hemisphere_images": Hemisphere_img_urls
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return Mars_data
###############################################################################################################################################