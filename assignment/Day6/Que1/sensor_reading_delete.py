Skip to content
Navigation Menu
Sign in
IOT-94157-snehal
/
IIT_IOT_Internship
Public
Code
Issues
Pull requests
Actions
Projects
Security
Insights
IIT_IOT_Internship/Assignment/Day6_Assignment/Que1
/senosr_reading_delete.py
sk3149478-cmd
sk3149478-cmd
18 Dec Assignment
c18022e
 · 
4 days ago
32 lines (22 loc) · 581 Bytes

Code

Blame

import mysql.connector as myc

connection= myc.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="iot_application",
    use_pure=True
)


# form a query to be executed
id = int(input("Enter id to be deleted : "))

query = f"DELETE FROM sensor_readings WHERE id = {id};"

# create a cursor to execute a query
cursor = connection.cursor()

# execute a query
cursor.execute(query)

# commit your changes on mysql server
connection.commit()

# close the cursor
cursor.close()

# close the connection with mysql server
connection.close()
