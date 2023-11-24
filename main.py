
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.header("Zena's amazing athleisure catalog")

streamlit.text_input('Pick a sweatsuit color or style','red')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(),CURRENT_REGION()")
my_data_row = my_cur.fetchone()
