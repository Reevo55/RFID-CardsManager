import database as db
from datetime import datetime

def readCard():
    currentTime = datetime.now()
    date = currentTime.replace(microsecond=0)
    print("Wszedl czy wyszedl (1 wszedł, 0 wyszedł): ")
    wentIn = input()
    print("Id karty: ")
    cardId = input()
    db.addReadingToDatabase(date, wentIn, cardId)
