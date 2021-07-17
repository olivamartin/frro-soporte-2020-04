from ejercicio_01 import reset_table,cursor,connection
import datetime

def insertPerson(name, birthDate, dni, height):
    sql_insert_query = """INSERT INTO `practico_03`.`person` (name, birthDate, dni, height) VALUES (%s,%s,%s,%s)"""
    recordTuple = (name, birthDate, dni, height)
    cursor.execute(sql_insert_query, recordTuple)
    connection.commit()
    sql_selectOne_query = "SELECT max(personId) FROM practico_03.person;"
    cursor.execute(sql_selectOne_query)
    result = cursor.fetchone()
    return result[0]

@reset_table
def tests():
    id_juan = insertPerson('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = insertPerson('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    tests()