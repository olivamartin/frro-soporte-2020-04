from ejercicio_01 import createTable,dropTable,connection
import pymysql

cursor = connection.cursor(pymysql.cursors.DictCursor)

def createWeightTable():
    personTable = """CREATE TABLE `practico_03`.`person_weight` (
  `weightId` INT NOT NULL AUTO_INCREMENT,
  `personId` INT NOT NULL,
  `date` DATE NULL,
  `weight` INT NULL,
  PRIMARY KEY (`weightId`),
  INDEX `personId_fk1_idx` (`personId` ASC),
  CONSTRAINT `personId_fk1`
    FOREIGN KEY (`personId`)
    REFERENCES `practico_03`.`person` (`personId`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE);"""
    cursor.execute(personTable)

def dropWeightTable():
    personTable = "DROP TABLE IF EXISTS `practico_03`.`person_weight`"
    cursor.execute(personTable)


def reset_table(func):
    def func_wrapper():
        createTable()
        createWeightTable()
        func()
        dropWeightTable()
        dropTable()
    return func_wrapper





