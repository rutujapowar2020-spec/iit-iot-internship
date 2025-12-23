
import mysql.connector as myc
import time
from datetime import datetime

connection= myc.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="smart_agriculture",
    use_pure=True
)

id = int(input ("enter id : "))
temp = float(input ("enter temp : "))
humidity = float(input ("enter hum :")) 
now = datetime.now()
formatted_time = now.strftime("%Y-%M-%D %H:%M:%S")
timestamp = formatted_time
query= f"insert into smart_agriculture values({id},'{temp}', '{humidity}', '{timestamp}');"

cursor=connection.cursor()

cursor.execute(query)

readings=cursor.fetchall()

print(readings)

cursor.execute(query)

filtered_readings = cursor.fetchall()

print(filtered_readings)


cursor.close()

connection.close()
