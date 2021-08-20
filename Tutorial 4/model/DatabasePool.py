from mysql.connector import pooling


class DatabasePool:
    # class variable
    connection_pool = pooling.MySQLConnectionPool(
        pool_name="ws_pool",
        pool_size=5,
        host='localhost',
        database='tutorial4',
        user='root',
        password='password')

    @classmethod
    def getConnection(cls):
        dbConn = cls.connection_pool.get_connection()
        return dbConn
