import os
from curses import echo
import os
import sqlite3
import sqlalchemy
import pandas as pd
import pymysql
from scrape import cases, deaths, population, recovered

cre = os.environ.get('DB_CRE')

engine = sqlalchemy.create_engine(cre, echo=False)
#import cases into database
cases().to_sql('cases', engine, if_exists='append', index_label='country_id')

deaths().to_sql('deaths', engine, if_exists='append', index_label='country_id')

recovered().to_sql('recovered', engine, if_exists='append', index_label='country_id')

population().to_sql('population', engine, if_exists='append', index_label='country_id')