from model.DatabasePool import DatabasePool


class Furniture:
    @classmethod
    def getFurnitureByCat(cls, catid):
        dbConn = DatabasePool.getConnection()
        cursor = dbConn.cursor(dictionary=True)
        sql = "select * from furniture"
        cursor.execute(sql)
        furniture = cursor.fetchall()

        dbConn.close()

        return furniture
