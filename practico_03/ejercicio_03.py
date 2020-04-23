from ejercicio_01 import reset_table,cursor,connection,getAll
from ejercicio_02 import insertPerson
import datetime

def deleteOne(personId):
        sql_delete_query = """DELETE FROM `practico_03`.`person` WHERE (`personId` = %s)"""
        cursor.execute(sql_delete_query,personId)
        connection.commit()
        return False if cursor.rowcount == 0 else True


@reset_table
def tests():
   assert (deleteOne(insertPerson('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)))
   assert deleteOne(12345) is False


if __name__ == '__main__':
    tests()