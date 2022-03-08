
from curses import echo
from dataclasses import replace
import sqlite3
import sqlalchemy
import pandas as pd
import pymysql
from scrape import cases, deaths, population, recovered

engine = sqlalchemy.create_engine("mysql+pymysql://lad:1@138.2.88.234:3306/corona_virus_demo", echo=False)

#import cases into database
cases().to_sql('cases', engine, if_exists='replace', index_label='country_id')

deaths().to_sql('deaths', engine, if_exists='replace', index_label='country_id')

recovered().to_sql('recovered', engine, if_exists='replace', index_label='country_id')

population().to_sql('population', engine, if_exists='replace', index_label='country_id')