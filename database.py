import sqlite3 as db
from datetime import date

conn = db.connect('idReaderDatabase.db')

c = conn.cursor()

arrayOfReadings = []
arrayOfCards = []
arrayOfEmployees = []

def dataToArrays():
    arrayOfReadings.clear()
    arrayOfCards.clear()
    arrayOfEmployees.clear()

    employeesCursor = c.execute("SELECT * FROM Employees")

    for employee in employeesCursor:
        employeeObj = Employee(employee[0], employee[1])
        arrayOfEmployees.append(employeeObj)

    cardsCursor = c.execute("SELECT * FROM Cards")
    for card in cardsCursor:
        cardObj = Card(card[0], card[1], card[2])
        arrayOfCards.append(cardObj)

    readingsCursor = c.execute("SELECT Employees.Name, Cards.Identifier, Readings.Date, Readings.WentIn FROM((Readings INNER JOIN Cards ON Readings.IdCard = Cards.IdCard) INNER JOIN Employees ON Cards.IdEmployee = Employees.IdEmployee);")
    for reading in readingsCursor:
        readingObj = Reading(reading[0], reading[1], reading[2], reading[3])
        arrayOfReadings.append(readingObj)
        

def addEmployeeToDatabase(name):
    name = (name,)
    c.execute("INSERT INTO Employees(Name) VALUES (?)", name)

def addCardToDatabase(cardIdentifier, whoseCard):
    data = (cardIdentifier, whoseCard)
    c.execute("INSERT INTO Cards(Identifier, IdEmployee) VALUES (?,?)", data)

def addReadingToDatabase(date, wentIn, cardId):
    data = (date, wentIn, cardId)
    c.execute("INSERT INTO Readings(Date,WentIn,IdCard) VALUES (?,?,?)", data)

def deleteCardFromDatabase(cardId):
    data = (cardId,)
    c.execute("DELETE FROM Cards WHERE IdCard = ?", data)

def deleteEmployeeFromDatabase(employeeId):
    data = (employeeId,)
    c.execute("DELETE FROM Employees WHERE IdEmployee = ?", data)
    
def deleteReadingFromDatabase(readingId):
    data = (readingId,)
    c.execute("DELETE FROM Readings WHERE IdReading = ?", data)

def updateCardFromDatabase(idCard, idEmployee):
    data = (idEmployee, idCard)
    c.execute("UPDATE Cards SET IdEmployee = ? WHERE IdCard = ?", data)

def resetEmployeeFromCard(idCard):
    data = (idCard,)
    c.execute("UPDATE Cards SET IdEmployee = NULL WHERE IdCard = ?", data)

def printAllReadings():
    c.execute("SELECT Employees.Name, Cards.Identifier, Readings.Date, Readings.WentIn FROM((Readings LEFT JOIN Cards ON Readings.IdCard = Cards.IdCard) LEFT JOIN Employees ON Cards.IdEmployee = Employees.IdEmployee);")
    print("Name | Identifier | Date | WentIn")
    for reading in c.fetchall():
        print(reading)
        print("\n")

def printReadingsForEmployee(employeeId):
    data = (employeeId,)
    c.execute("SELECT Employees.Name, Cards.Identifier, Readings.Date, Readings.WentIn FROM((Readings INNER JOIN Cards ON Readings.IdCard = Cards.IdCard) INNER JOIN Employees ON Cards.IdEmployee = Employees.IdEmployee)  WHERE Employees.IdEmployee = ?", data)
    print("Name | Identifier | Date | WentIn")
    for reading in c.fetchall():
        print(reading)
        print("\n")     

def fullStringReadingsOfEmployee(employeeId):
    data = (employeeId,)
    c.execute("SELECT Employees.Name, Cards.Identifier, Readings.Date, Readings.WentIn FROM((Readings INNER JOIN Cards ON Readings.IdCard = Cards.IdCard) INNER JOIN Employees ON Cards.IdEmployee = Employees.IdEmployee)  WHERE Employees.IdEmployee = ?", data)
    arrOfReadings = []
    for reading in c.fetchall():
        readingObj = Reading(reading[0], reading[1], reading[2], reading[3])
        arrOfReadings.append(readingObj)
    
    return arrOfReadings


def getIdOfCardByRFID(rfid):
    data = (rfid,)
    c.execute("SELECT * FROM Cards")
    for card in c.fetchall():
        print(card[0])
        return card[0]
    return None

def printAllEmployees():
    c.execute("SELECT * FROM Employees")
    print("IdEmployee | Name")
    for employee in c.fetchall():
        print(employee)
        print("\n")

def printAllCards():
    c.execute("SELECT Cards.IdCard, Cards.Identifier, Cards.IdEmployee, Employees.Name FROM Cards LEFT JOIN Employees ON Cards.IdEmployee = Employees.IdEmployee;")
    print("IdCard | Identifier | IdEmployee | Name")
    for card in c.fetchall():
        print(card)
        print("\n")

def saveChangesInDatabase():
    conn.commit()

class Employee:
    Name = ""
    IdEmployee = ""
    
    def __init__(self, id, name):
        self.Name = name
        self.IdEmployee = id
    def __repr__(self):
        return str(self)
    def __str__(self):
        return "<Employee id=%s name=%s>" % (self.IdEmployee, self.Name)

class Card:
    IdCard = ""
    Identifier = ""
    IdEmployee = ""

    def __init__(self, idCard, identifier, idEmployee):
        self.Identifier = identifier
        self.IdCard = idCard
        self.IdEmployee = idEmployee
    def __str__(self):
        return "<Card id = %s, identifier = %s, employee = %s>" % (self.IdCard, self.Identifier, self.IdEmployee)
    def __repr__(self):
        return str(self)


class Reading:
    EmployeeName = ""
    CardId = ""
    Date = ""
    WentIn = ""

    def __init__(self, employee, cardId, date, wentIn):
        self.Date = date
        self.CardId = cardId
        self.WentIn = wentIn
        self.EmployeeName = employee
    def __str__(self):
        return  "<%s, %s, %s, %s>" % (self.EmployeeName, self.Date, self.WentIn, self.CardId)
    def __repr__(self):
        return str(self)
