import datetime,pymysql
from ejercicio_01 import reset_table,connection
from ejercicio_02 import insertPerson

cursor = connection.cursor(pymysql.cursors.DictCursor)

def convert(dicc):
    return (*dicc, )

def getOne(personId):
 try:
    sql_getOne_query = """SELECT * FROM `practico_03`.`person` WHERE (`personId` = %s)"""
    cursor.execute(sql_getOne_query,personId)
    result = cursor.fetchall()[0]
    return result
 except:
     return False

@reset_table
def tests():
    juan = convert(getOne(insertPerson('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)).values()) #el convert es para convertir el diccionario a tupla
    assert juan == (1, 'juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    assert getOne(12345) is False

if __name__ == '__main__':
    tests()
