import pymysql

connection = pymysql.connect(
    host="localhost",  # Si la DB es remota, colocar IP
    user="root",
    password="39855209",
    db="practico_03"
)
cursor = connection.cursor()#pymysql.cursors.DictCursor

def createTable():
    personTable = """CREATE TABLE IF NOT EXISTS `practico_03`.`person` (
    `personId` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(30) NULL,
    `birthDate` DATE NULL,
    `dni` INT(8) NULL,
    `height` INT NULL,
    PRIMARY KEY (`personId`));"""
    cursor.execute(personTable)


def closeConnection():
    cursor.close()
    connection.close()

def dropTable():
    personTable = "DROP TABLE IF EXISTS `practico_03`.`person`"
    cursor.execute(personTable)


def getAll():
    sql_getAll_query = "SELECT * FROM `practico_03`.`person`"
    cursor.execute(sql_getAll_query)
    people = cursor.fetchall()
    return print(people)


def reset_table(func):
    def func_wrapper():
        createTable()
        func()
        dropTable()
    return func_wrapper

if __name__ == '__main__':
    reset_table(getAll)()




