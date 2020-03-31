import database as db
from datetime import date
import cardReader
import workingTimeRaport as raport
import fileHandler

def menu():
    print("-------------MENU---------")
    print("1.Dodaj użytkownika")
    print("2.Dodaj kartę")
    print("3.Dodaj odczyt karty")
    print("4.Pokaż wszystkie odczyty")
    print("5.Pokaż odczyty użytkownika")
    print("6.Dodaj użytkownika do karty")
    print("7.Usuń użytkownika karty")
    print("8.Usuń karte")
    print("9.Pokaż wszystkie karty")
    print("10.Pokaż wszystkich pracowników")
    print("11.Wygeneruj raport czasu pracy dla pracownika")

    print("Wprowadź liczbę przypisaną komendzie: ")
    executeCommand(input())
    db.saveChangesInDatabase()
    db.dataToArrays()

    menu()

def executeCommand(command):
    if command == "1":
        print("Imie uzytkownika: ")
        name = input()
        db.addEmployeeToDatabase(name)
        print("Zostal dodany: " + name)

    elif command == "2":
        print("Identyfikator karty: ")
        identifier = input()
        print("Id pracownika: ")
        idEmployee = input()
        db.addCardToDatabase(identifier, idEmployee)
        print("Zostala dodana karta: " + identifier + " Pracownika: "+ idEmployee)

    elif command == "3":
        cardReader.readCard()

    elif command == "4":
        db.dataToArrays()
        print(db.arrayOfReadings)

    elif command == "5":
        print("Podaj id użytkownika: ")
        db.printReadingsForEmployee(input())

    elif command == "6":
        print("Podaj id karty: ")
        idCard = input()
        print("Podaj id pracownika: ")
        idEmployee = input()
        db.updateCardFromDatabase(idCard, idEmployee)

    elif command == "7":
        print("Podaj id karty z której chcesz usunąć pracownika: ")
        idCard = input()
        db.resetEmployeeFromCard(idCard)
        print("Powiodło się")

    elif command == "8":
        print("Podaj id karty, którą chcesz usunąć: ")
        idCard = input()
        db.deleteCardFromDatabase(idCard)
        print("Powiodlo sie!")

    elif command == "9":
        db.printAllCards()

    elif command == "10":
        db.printAllEmployees()

    elif command == "11":
        print("Podaj id pracownika dla ktorego ma byc raport: ")
        idEmployee = input()
        fileName = "Employee" + idEmployee + ".csv"
        fileHandler.writeToFile(fileName, db.fullStringReadingsOfEmployee(idEmployee))

    else : print("Wybierz poprawną opcję!")


menu()
