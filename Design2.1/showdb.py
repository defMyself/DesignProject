import db

mydb = db.DB()
for i in mydb.getalltables():
    print(i)