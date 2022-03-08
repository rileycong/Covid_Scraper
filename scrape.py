import datetime as dt
from bs4 import BeautifulSoup
import requests
import pandas as pd


# link to the web
source = requests.get('https://www.worldometers.info/coronavirus/').text
soup = BeautifulSoup(source, 'lxml')

## The Scrape Begins ##

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

data = data.drop_duplicates(subset = ["Country,Other"])
# Reason to drop duplicates : Worldometer reports data for 3 days: today and 2 days back
# Removing duplicates removes the values for the past two days and keep today's

# Drop the following columns
cols = ['#',
            'Tot\xa0Cases/1M pop',
            'Deaths/1M pop',
            'TotalTests',
            'Tests/1M pop',
            '1 Caseevery X ppl',
            '1 Deathevery X ppl',
            '1 Testevery X ppl',
            'New Cases/1M pop',
            'New Deaths/1M pop',
            'Active Cases/1M pop']



# Data full has all needed informations
data_full = data.drop(cols, axis=1)

#Cleaning data
#Remove '+'
data_full['NewCases'] = data_full['NewCases'].str.replace('+', ' ')
data_full['NewDeaths'] = data_full['NewDeaths'].str.replace('+', ' ')
data_full['NewRecovered'] = data_full['NewRecovered'].str.replace('+', ' ')
data_full

#Remove','
data_full = data_full.apply(lambda x: x.str.replace(',',''))
data_full

data_full = data_full.drop(211) #Remove Diamond Princess
data_full = data_full.drop(221) #Remove MS Zaandam
data_full.reset_index(inplace=True) #Reset index

#remove N/A and replace with 0
#remove Empty string and replace with 0
data_full = data_full.replace('N/A', '0')
data_full = data_full.replace(r'^\s*$', '0', regex=True)

#sorting
data_full.sort_values('Country,Other', ascending=True, inplace=True)
data_full.reset_index(inplace=True)
data_full.index = data_full.index + 1

#Drop country_info
data_full = data_full.drop('Country,Other',axis=1) 
data_full = data_full.drop('Continent',axis=1)


#Convert to INT
data_full = data_full.astype(int) 

#Timestamp
data_full['Timestamp'] = dt.datetime.now()  

# Select specific columns from data_full
def cases():
    cases = data_full[['TotalCases','ActiveCases','NewCases','Serious,Critical','Timestamp']]
    return cases

def deaths():
    deaths = data_full[['TotalDeaths','NewDeaths','Timestamp']]
    return deaths

def recovered():
    recovered = data_full[['TotalRecovered','NewRecovered','Timestamp']]
    return recovered

def population():
    population = data_full[['Population','Timestamp']]
    return population
   
