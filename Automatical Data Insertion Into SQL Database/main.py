#The main goal of this script is to automatically create certain databases and insert data into them from a text file for example.
#For this project the data isn't cleaned, and I've used a txt file, the only real goal here was the automatisation itself.
#However, I'll be focusing on data cleaning as well in future projects.

import mysql.connector

db = mysql.connector.connect(  #connecting to local database
    host="localhost",
    user="root",
    password=""
)

cursor = db.cursor()  #cursor executes MySQL commands in the server

try:  #try creating the database if it doesn't exist
    cursor.execute("CREATE DATABASE TestingDatabase")
    print("Database crated successfully!")
except:
    print("Database already exists")

db = mysql.connector.connect(
    user="root",
    password="",
    database="TestingDatabase"
)

cursor = db.cursor()

array = [] #we store the data from the txt, so we can upload it to the database
with open("menu.txt",encoding="ISO-8859-1") as ff:
    for line in ff:
        data = line.strip().split(",") # for now, I'll won't clean the data more
        array.append(data)
try:
    cursor.execute("CREATE TABLE menu (id INT AUTO_INCREMENT PRIMARY KEY)")#creating table to store the data
    print("Table created successfully!")
except:
    print("Table already exists")

for i in array[0]: #minimal cleaning so we can add columns automatically according to the array
    i = i.replace(" ", "_")
    i = i.replace("%", "")
    i = i.replace("(", "")
    i = i.replace(")", "")
    try:
        cursor.execute("ALTER TABLE menu ADD COLUMN {} TEXT(200)".format(i))
    except:
        continue
try:
    cursor.execute("ALTER TABLE menu DROP ID") #at the moment this isn't needed
except:
    print("Can't drop ID")

sql="INSERT INTO menu VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
for j in array[1::]: #automatically filling the database
    val = (j[0], j[1], j[2], j[3], j[4], j[5], j[6], j[7], j[8], j[9], j[10], j[11], j[12], j[13], j[14], j[15], j[16], j[17], j[18], j[19], j[20], j[21], j[22], j[23])
    cursor.executemany(sql,[val])
    db.commit()
print("Data inserted successfully!")
