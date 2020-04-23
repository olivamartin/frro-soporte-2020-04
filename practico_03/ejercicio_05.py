from ejercicio_01 import reset_table,cursor,connection
from ejercicio_02 import insertPerson
from ejercicio_04 import getOne,convert
import datetime

def updateOne(personId,name,birthDate,dni,height):
    sql_updateOne_query = """UPDATE `practico_03`.`person` SET `name` = %s,`birthDate` = %s, `dni` = %s, `height` = %s WHERE (`personId` = %s)"""
    recordTuple = (name, birthDate, dni, height,personId)
    cursor.execute(sql_updateOne_query,recordTuple)
    connection.commit()
    if cursor.rowcount != 0:
        sql_getOne_query = """SELECT * FROM `practico_03`.`person` WHERE `personId` = %s"""
        cursor.execute(sql_getOne_query,personId)
        result = cursor.fetchall()
        return result[0]
    else:
        return False

@reset_table
def tests():
    id_juan = insertPerson('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    updateOne(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert convert(getOne(id_juan).values()) == (1, 'juan carlos perez', datetime.date(1988, 4, 16), 32165497, 181)
    assert updateOne(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    tests()

