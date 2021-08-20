from mysql.connector import Error
from mysql.connector import pooling


class DatabasePool:
    # class variable
    connection_pool = pooling.MySQLConnectionPool(pool_name="ws_pool",
                                                  pool_size=5,
                                                  host='localhost',
                                                  database='tutorial4',
                                                  user='root',
                                                  password='password')

    @classmethod
    def getConnection(cls):
        dbConn = cls.connection_pool.get_connection()
        return dbConn


'''
connection_object=DatabasePool.getConnection()
db_Info = connection_object.get_server_info()

print("Connected to MySQL database using connection pool ... MySQL Server version on ", db_Info)

cursor = connection_object.cursor(dictionary=True)

cursor.execute("select * from user;")
records = cursor.fetchall()
for record in records:
    print(record)
'''
