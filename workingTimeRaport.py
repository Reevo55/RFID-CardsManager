import database as db

def generateRaportForEmployee(employeeId):
    employeeCards = []
    employeeReadings = []

    for card in db.arrayOfCards:
        if card.IdEmployee == employeeId:
            employeeCards.append(card)

    for reading in db.arrayOfReadings:
        for card in employeeCards:
            if card.IdCard == reading.CardId:
                employeeReadings.append(reading)

  