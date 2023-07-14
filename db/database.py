import sqlite3

conn = sqlite3.connect('passengerdb.db')
cursor = conn.cursor()

sql = '''
select b.pnr_number, b.travel_date, b.source_airport, b.destination_airport, b.seat_preference, b.meal_preference, p.name, p.email, p.phone
from Passengers p, Bookings b where p.passenger_id = b.passenger_id;
'''

cursor.execute(sql)

values = cursor.fetchall()
for value in values:
    for v in value:
        print(v, end=" ")
    print()
    
conn.commit()
conn.close()