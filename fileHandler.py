import csv
import datetime
import time

def writeToFile(filename, readings):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Card Identifier", "Date", "WentIn (1) WentOut(0)"])

        for reading in readings:
            writer.writerow([reading.EmployeeName, reading.CardId, reading.Date, reading.WentIn])

        sumOfHours = calculateWorkingTime(readings)
        writer.writerow(["Sum of all working hours: " , sumOfHours])
    
def calculateWorkingTime(arrayOfReadings):
    sumOfWorkingHours = 0
    currentEntryTime = ""

    for reading in arrayOfReadings:
        if reading.WentIn == 1:
            currentEntryTime = reading.Date
        elif currentEntryTime != "" and reading.WentIn == 0:
            sumOfWorkingHours += diffrenceInTime(currentEntryTime, reading.Date)\
    
    return sumOfWorkingHours



def diffrenceInTime(dateOfEntry, dateOfLeave):
    
    dateWentIn = datetime.datetime.strptime(dateOfEntry, '%Y-%m-%d %H:%M:%S')
    dateWentOut = datetime.datetime.strptime(dateOfLeave, '%Y-%m-%d %H:%M:%S')

    diff = dateWentOut - dateWentIn

    days, seconds = diff.days, diff.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
        
    return hours
