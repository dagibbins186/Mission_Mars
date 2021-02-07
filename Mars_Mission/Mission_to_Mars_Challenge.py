#!/usr/bin/env python
# coding: utf-8

# In[66]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup


# In[68]:


# Set the executable path and initialize chrome browser in splinter
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome',**executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[3]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[4]:


# Parse the HTML
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[5]:


# Scrape the Title
slide_elem.find("div", class_='content_title')


# In[6]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### JPL Space Images Featured Image

# In[12]:


# Visit URL
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)


# In[16]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[17]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[18]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[19]:


# Use the base URL to create an absolute URL
img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
img_url


# ### Mars Facts

# In[20]:


import pandas as pd
df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df


# In[21]:


df.to_html()


# ### Mars Weather

# In[22]:


# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)


# In[23]:


# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')


# In[24]:


# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[60]:


# 1. Use browser to visit the URL 
Hemisphere_browser = Browser('chrome', headless=False)
Hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
Hemisphere_browser.visit(Hemisphere_url)


# In[63]:


Hemisphere_html = Hemisphere_browser.html
Hemisphere_html


# In[65]:


type(Hemisphere_html)


# In[69]:


Hemisphere_soup = soup(Hemisphere_html, 'html.parser')


# In[70]:


# 3. Write code to retrieve the image urls for each hemisphere and create a list to hold the images and titles.
Image_hemisphere_one = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
Image_hemisphere_two = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
Image_hemisphere_three = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
Image_hemisphere_four = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'
links = [Image_hemisphere_one,Image_hemisphere_two,Image_hemisphere_three,Image_hemisphere_four]
All_Images=Hemisphere_soup.find_all('h3')
All_Images


# In[74]:


# 4. Write code to retrieve the titles for each hemisphere.
titles = [h3.text.strip() for h3 in titles]
titles


# In[75]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls = [{'title': titles, 'img_url': link} for titles, link in zip(titles,links)]
hemisphere_image_urls


# In[76]:


# 5. Quit the browser
browser.quit()

