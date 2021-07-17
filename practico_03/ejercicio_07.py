from ejercicio_01 import connection
from ejercicio_02 import insertPerson
from ejercicio_04 import getOne,cursor
from ejercicio_06 import reset_table
import datetime,  pymysql


def addWeight(personId,date,weight):
    person = getOne(personId)
    if person:
        if person["personId"] == personId:
            sql_getOne_query = """SELECT personId,MAX(date) maxDate  FROM practico_03.person_weight
                                    WHERE personId = %s 
                                    GROUP BY personId;"""
            cursor.execute(sql_getOne_query, personId)
            if cursor.rowcount != 0:
                result = cursor.fetchall()[0]
                if result["maxDate"] >= date or result["personId"] != personId:
                    return False
            sql_insert_query = """INSERT INTO `practico_03`.`person_weight` (personId, date, weight) VALUES (%s,%s,%s)"""
            recordTuple = (personId, date, weight)
            cursor.execute(sql_insert_query, recordTuple)
            connection.commit()
            sql_getMaxId_query = """SELECT MAX(weightId) maxId FROM practico_03.person_weight"""
            cursor.execute(sql_getMaxId_query)
            result2 = cursor.fetchall()[0]['maxId']
            return result2
    else:
        return False



@reset_table
def tests():
    id_juan = insertPerson('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert addWeight(id_juan, datetime.datetime(2022, 5, 26), 80) > 0
    # id incorrecto
    assert addWeight(20, datetime.date(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert addWeight(id_juan, datetime.date(2018, 5, 16), 80) == False

if __name__ == '__main__':
   tests()

