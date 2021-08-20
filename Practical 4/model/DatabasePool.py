from mysql.connector import pooling
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


class DatabasePool:

    connection_pool = pooling.MySQLConnectionPool(
        pool_name="ws_pool", pool_size=5, host='localhost', database='furniture', user='root', password='root'
    )


@classmethod
def getConnection(cls):
    dbConn = cls.connection_pool.get_connection()
    return dbConn
