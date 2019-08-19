#import necessary items
from bs4 import BeautifulSoup
import pandas as pd
import time
from splinter import Browser
def scrape():
#Website Navigation
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    #Mars Website (NASA)
    nasa_url = 'https://mars.nasa.gov/news/'
    browser.visit(nasa_url)
    time.sleep(1)
    nasa_html = browser.html
    nasa_soup = BeautifulSoup(nasa_html, 'html.parser')

    #Grabbing Article
    latest_article = nasa_soup.find("div", "list_text")
    news_title = latest_article.find("div", class_="content_title").text
    news_paragraph = latest_article.find("div", class_="article_teaser_body").text
    print(news_title)
    print(news_paragraph)

    #Jet Propulsion Labs Website
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)
    time.sleep(1)

    #get image
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(1)
    expand = browser.find_by_css('a.fancybox-expand')
    expand.click()
    time.sleep(1)

    jpl_html = browser.html
    jpl_soup = BeautifulSoup(jpl_html, 'html.parser')

    #get landing page
    img_relative = jpl_soup.find('img', class_='fancybox-image')['src']
    image_path = f'https://www.jpl.nasa.gov{img_relative}'
    print(image_path)

    #Scrape twitter for the Mars weather tweet
    mars_tweet_weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_tweet_weather_url)
    time.sleep(1)
    mars_tweet_weather_html = browser.html
    mars_tweet_weather_soup = BeautifulSoup(mars_tweet_weather_html, 'html.parser')

    weather_tweets = mars_tweet_weather_soup.find('p', class_='tweet-text').text
    weather_tweets

    #Scrape Mars Facts (diameter,mass....)
    mars_facts_url = "https://space-facts.com/mars/"
    mars_facts = pd.read_html(mars_facts_url)
    mars_facts

    mars_facts_pd = pd.DataFrame(mars_facts[0])
    del mars_facts_pd['Earth']
    mars_facts_pd

    mars_facts_pd.to_html()

    #Grab Mars Hemispheres Images from United States Geological Survey Website
    mars_hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemisphere_url)

    mars_facts_data = {}
    mars_facts_data['news_title'] = news_title
    mars_facts_data['news_paragraph'] = news_paragraph
    mars_facts_data['image_path'] = image_path
    mars_facts_data['weather_tweets'] = weather_tweets
    mars_facts_data['mars_facts'] = mars_facts
    return mars_facts_data
