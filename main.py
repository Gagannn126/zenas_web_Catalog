
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.header("Zena's amazing athleisure catalog")

picked_option=streamlit.text_input('Pick a sweatsuit color or style','red')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from catalog_for_website where color_or_style = "+picked_option)
my_data_row = my_cur.fetchone()
streamlit.text(my_data_row)