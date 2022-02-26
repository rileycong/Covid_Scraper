from bs4 import BeautifulSoup
import requests
#import pandas as pd

# link to the web
source = requests.get('https://www.worldometers.info/coronavirus/').text
soup = BeautifulSoup(source, 'lxml')

## The Scrape Begins ##

# Pick the id of the table we want to scrape
covid_table = soup.find("table", attrs={"id": "main_table_countries_today"})

# The header html
head = covid_table.thead.find_all('tr')

# Extract headers from html to create list
headings = []
for th in head[0].find_all('th'):
    print(th.text)
    headings.append(th.text.replace('\n','').strip())   # remove any newlines and extra spaces from left and right
print(headings)

# The body html
body = covid_table.tbody.find_all('tr')

# Append the values of rows to create list
data = []   # A list that hold all rows
for a in range(1, len(body)):
    row = []
    for td in body[a].find_all('td'):
        row.append(td.text.replace('\n','').strip())
    data.appennd(row)

# data contains all the rows excluding header
# row contains data for one row








# #We can now pass data into a pandas dataframe
# #with headings as the columns
# df = pd.DataFrame(data,columns=headings)
# df.head(10)

# data = df[df["#"]!=""].reset_index(drop=True)
# # Data points with # value are the countries of the world while the data points with
# # null values for # columns are features like continents totals etc
# data = data.drop_duplicates(subset = ["Country,Other"])
# #Reason to drop duplicates : Worldometer reports data for 3 days: today and 2 days back
# #I found out that removing duplicates removes the values for the bast two days and keep today's

# # Columns to keep
# cols = ['Country,Other', 'TotalCases', 'NewCases', 'TotalDeaths',
#        'NewDeaths', 'TotalRecovered', 'NewRecovered', 'ActiveCases',
#        'Serious,Critical', 'TotalTests']
# # Extract the columns we are interested in a display the first 5 rows
# data_final = data[cols]
# data_final.head()