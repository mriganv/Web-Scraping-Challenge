# Web Scraping Homework - Mission to Mars

![mission_to_mars](Mission_to_Mars/screenshots/mission_to_mars.png)

In this assignment, we built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. We need the following outlines. 


## Step 1 - Scraping

We did our initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Created a Jupyter Notebook file called `mission_to_mars.ipynb` and use this to complete all of your scraping and analysis tasks. Started scraping the following outlines.

### NASA Mars News

* Scraped the [Mars News Site](https://redplanetscience.com/) and collected the latest News Title and Paragraph Text. Assigned the text to variables to use it to later add to a  dictionary. 

![Latest news and paragraph screenshot](https://user-images.githubusercontent.com/81407869/132165999-1a47a667-f387-48fa-9d2f-931e98189e4f.jpg)!


### JPL Mars Space Images - Featured Image

* Visited the url for the Featured Space Image site [here](https://spaceimages-mars.com).

* Used splinter to navigate the site and found the image url for the current Featured Mars Image and assigned it the url string to a variable called `featured_image_url`.

* Image url of the enhanced featured Image was scraped.

* Saved a complete url string for this image.


![featured image](https://user-images.githubusercontent.com/81407869/132166745-b90d46ca-c342-4562-94f9-252dc66dfad6.jpg)



### Mars Facts

* Visited the Mars Facts webpage [here](https://galaxyfacts-mars.com) and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Used Pandas to convert the data to a HTML table string.

![Screenshot 2021-09-05 224130](https://user-images.githubusercontent.com/81407869/132166153-7dd1dfb1-daae-46de-9f4f-6e966b350fe4.jpg)


### Mars Hemispheres

* Visited the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres.

* Did a click on each of the links to the hemispheres in order to find the image url to the full resolution image.

* Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Used a Python dictionary to store the data using the keys `img_url` and `title`.

* Appended the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.


![image urls ](https://user-images.githubusercontent.com/81407869/132166814-f078516c-16fc-495f-b6f6-a543611825bf.jpg)


## Step 2 - MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above. The following tasks were undertaken: 

* Started by converting Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that executed the code from above and returned one Python dictionary containing all of the scraped data.

* Created a root route `/` (index.html) that will display a cover image of Mission to mars and a button to initialize the scraping. 

* Next, it routes to `/scrape` route that will import `scrape_mars.py` script  calling `scrape` function.

* Once the scraping completes it redirects the '/Marsdata' route to display all the Mars facts datas that were gathered. 

* Stores the return value in Mongodb as a Python dictionary.

* The '/Marsdata' (Marsdata.html) route displays the collected data of Mars that were scraped from all of the URLs mentioned above and displays in an HTML page.

______________________________________________________________________________________________________________________________________________________________________________
## Screenshots 

![final_app_index](https://user-images.githubusercontent.com/81407869/132166397-9cb804e2-9e17-409b-9c7a-7a440587643e.png)


![final_app_marsdata](https://user-images.githubusercontent.com/81407869/132166410-7c8f1daa-a777-4a0b-9f67-4c36037ee4bd.png)




