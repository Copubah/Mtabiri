import schedule
import smtplib
import requests
from bs4 import BeautifulSoup

# Create a URL with a specific city name,i will use Nairobi and create a requests instance bypassing the URL

city = "Nairobi"
url = "https://www.google.com/search?q=" + "weather" + city
html= requests.get(url).content

# pass the retrieved HTML document into bs4
soup = BeautifulSoup(html,
                     'html.parser')
temperature = soup.find(
    'div', attrs={'class': 'BNeawe iBP4i AP7Wnd'}
).text

time_sky = soup.find(
    'div', attrs={'class': 'BNeawe tad8D AP7Wnd'}
).text

# format the data
sky = time_sky.split('\n')[1]

if sky == "Rainy" or sky == "Rain and Wind" or sky == "Showers" or sky =="Sunshine" or 
   smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

   