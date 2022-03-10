from bs4 import BeautifulSoup
import requests
import pandas as pd


# link to the web
source = requests.get('https://www.worldometers.info/coronavirus/').text
soup = BeautifulSoup(source, 'lxml')


# Pick the table we want to scrape using id
covid_table = soup.find("table", attrs={"id": "main_table_countries_today"})

# The header's html
head = covid_table.thead.find_all('tr')

# Extract text headers from html to create list
headings = []
for th in head[0].find_all('th'):
    headings.append(th.text.replace('\n','').strip())   # remove any newlines and extra spaces from left and right

# The body's html
body = covid_table.tbody.find_all('tr')

# Append the values of rows to create list
data = []   # A list that hold all rows
for a in range(1, len(body)):
    row = []
    for td in body[a].find_all('td'):
        row.append(td.text.replace('\n','').strip())
    data.append(row)

# data contains all the rows excluding header
# row contains data for one row

# Pass data into a pandas dataframe with headings as the columns
df = pd.DataFrame(data,columns=headings)

data = df[df['#']!=''].reset_index(drop=True)
# Data points with # value are the countries of the world while the data points with
# null values for # columns are features like continents totals etc

# Drop duplicates to only get today's data
data = data.drop_duplicates(subset = ["Country,Other"])

data = data.drop(211) #remove diamond princess
data = data.drop(221) #remove ms zaandam
data.reset_index(inplace=True) #Reset index

#sorting alphabetically
data.sort_values('Country,Other', ascending=True, inplace=True)

data.reset_index(inplace=True)
data.index = data.index + 1
# Select the country-related columns
def Country():
    country_info = data[['Country,Other','Continent']]
    return country_info

