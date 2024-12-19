import pandas as pd
import sqlite3


file_path = "hotel_bookings.csv"

data = pd.read_csv(file_path, index_col=False)
print("Data har lästs in:")
print(data.head())  

print(data.info())

data['total_guests'] = data['adults'] + data['children'] + data['babies']

df_filtered = data[(data['total_guests'] > 0) & (df['adults'] > 0)]

df_filtered = df[df['total_guests'] > 3]

print(df_filtered[['hotel', 'adults', 'children', 'babies', 'total_guests']].head())

data[data["arrival_date_year"] == 2017]


df_filtered = data[data['adults'] > 30]
display (df_filtered)

con = sqlite3.connect("hotel_bookings.db")

df_filtered.to_sql("hotel_bookings_filtered", con, if_exists="replace", index=False)

print("Bearbetad data har sparats till SQL-tabellen 'hotel_bookings_filtered'.")

con.close()


import logging

logging.basicConfig(
    filename='hotel_bookings_log.txt',
    format='[%(asctime)s][%(levelname)s] %(message)s',
    level=logging.INFO)

logger.info('Startar databehandling.')

try:
   
    data = pd.read_csv("hotel_bookings.csv")
    data['total_guests'] = data['adults'] + data['children'] + data['babies']
    df_filtered = data[(data['total_guests'] > 0) & (data['adults'] > 0)]
    
  
    con = sqlite3.connect("hotel_bookings.db")
    df_filtered.to_sql("hotel_bookings_filtered", con, if_exists="replace", index=False)
    con.close()
    
    logging.info('Data har bearbetats och sparats.')

except Exception as e:
    logging.error(f"Ett fel uppstod: {e}")
    print("Fel! Kontrollera loggen.")


def compare_is_canceled_children(df):
    is_canceled = df.is_canceled
    children = df.children
    


