
import pymysql

class ConnectDB(object):
    # singleton pattern
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self.con = pymysql.connect(
            host="localhost",
            user="myaccount",
            password="123456",
            db="mydb")

        self.cur = self.con.cursor()


class DB(ConnectDB):
    def __init__(self):
        super().__init__()

    # task_name = "v.zzu.edu.cn"
    # records = [("doamin1", "ip1"), ("domain2", "ip2")]
    def write(self, task_name, records):
        task_name = task_name.replace(".", "_")
        #sql_create_table = "CREATE TABLE IF NOT EXISTS {}(domain TEXT PRIMARY KEY, ip TEXT)".format(task_name)
        sql_create_table = """
        CREATE TABLE IF NOT EXISTS {} (
            domain varchar(40) PRIMARY KEY,
            ip varchar(40)
        )
        """.format(task_name)

        self.cur.execute(sql_create_table)
        sql_add_record = "INSERT INTO {} values".format(task_name)

        records = [str(i) for i in records]
        for record in records:
            try:
                new_sql = sql_add_record + record
                print(new_sql)

                self.cur.execute(new_sql)
                self.con.commit()
            except:
                print(str(record) + "exists")

    # get all records from task_name
    def read(self, task_name):
        task_name = task_name.replace(".", "_")
        sql = 'select * from {}'.format(task_name)
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data

    def getalltables(self):
        sql = "show tables"
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return [i[0] for i in data]

    def __del__(self):
        self.cur.close()
        self.con.close()


if __name__ == "__main__":
    task_name = "www.zzu.edu.cn"
    mydb = DB()
    records = [
        ("record1111", "ip1"),
        ("record2111", "ip2"),
        ("record3111", "ip3"),
    ]

    mydb.write(task_name, records)
    data = mydb.read(task_name)

    for i in data:
        print(i)

