<<<<<<< HEAD
import os
from curses import echo
import os
=======

from curses import echo
from dataclasses import replace
>>>>>>> 016b5c5d1fd09dae59d81a938e402f9cfb793e11
import sqlite3
import sqlalchemy
import pandas as pd
import pymysql
from scrape import cases, deaths, population, recovered

<<<<<<< HEAD
cre = os.environ.get('DB_CRE')

engine = sqlalchemy.create_engine(cre, echo=False)
=======
engine = sqlalchemy.create_engine("mysql+pymysql://lad:1@138.2.88.234:3306/corona_virus_demo", echo=False)

>>>>>>> 016b5c5d1fd09dae59d81a938e402f9cfb793e11
#import cases into database
cases().to_sql('cases', engine, if_exists='append', index_label='country_id')

deaths().to_sql('deaths', engine, if_exists='append', index_label='country_id')

recovered().to_sql('recovered', engine, if_exists='append', index_label='country_id')

population().to_sql('population', engine, if_exists='append', index_label='country_id')