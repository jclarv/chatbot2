import pandas as pd


data = pd.read_csv ('chatlog.csv')
df = pd.DataFrame(data)

import pymysql

db = pymysql.connect(
    user='superadmin',
    passwd='mysqlR@gn@r0k',
    host='mysqlubiq.mysql.database.azure.com',
    database='chatbotubiq',
    ssl={"fake_flag_to_enable_tls":True})

mycursor = db.cursor()

sql = "INSERT INTO chatlogs (ID,message, name,date, correct, correction, reponse) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = ("1","message","name","1999-12-01 01:01:01","correct","correction", "response")
mycursor.execute(sql, val)

print(mycursor.rowcount, "record inserted.")