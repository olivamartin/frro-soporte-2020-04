from ejercicio_02 import insertPerson
from ejercicio_04 import getOne
from ejercicio_06 import reset_table, cursor
from ejercicio_07 import addWeight
import datetime

def show_weights(personId):
    person = getOne(personId)
    if person:
        if person["personId"] == personId:
            sql_getAll_query = """SELECT date,weight FROM practico_03.person_weight WHERE (`personId` = %s)  """
            cursor.execute(sql_getAll_query,personId)
            result = cursor.fetchall()
            weights = []
            if cursor.rowcount != 0:
                for row in result:
                    mytuple = (row["date"].strftime("%Y-%m-%d"),row["weight"])
                    weights.append(mytuple)
            return weights
    else:
        return False

@reset_table
def pruebas():
    id_juan = insertPerson('juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    addWeight(id_juan, datetime.date(2018, 5, 1), 80)
    addWeight(id_juan, datetime.date(2018, 6, 1), 85)
    pesos_juan = show_weights(id_juan)
    pesos_esperados = [
        ('2018-05-01', 80),
        ('2018-06-01', 85),
    ]
    assert pesos_juan == pesos_esperados
    # id incorrecto
    assert show_weights(200) == False


if __name__ == '__main__':
    pruebas()