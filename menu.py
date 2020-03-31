import database as db
from datetime import date
import cardReader
import workingTimeRaport as raport
import fileHandler

def menu():
    print("-------------MENU---------")
    print("1.Dodaj użytkownika")
    print("2.Dodaj karte")
    print("3.Dodaj odczyt karty")
    print("4.Pokaz wszystkie odczyty.")
    print("5.Pokaz odczyty uzytkownika.")
    print("6.Dodaj uzytkownika do karty")
    print("7.Usun uzytkownika karty")
    print("8.Usuń karte")
    print("9.Pokaz wszystkie karty")
    print("10.Pokaz wszystkich pracownikow")
    print("11.Wygeneruj raport czasu pracy dla pracownika.")

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
        selectedCard = ""
        for card in db.arrayOfCards:
            if idCard == card.IdCard:
                selectedCard = card.IdCard
                break
        if selectedCard != None:
            print("Podaj id pracownika do którego ma być przypisana ta karta: ")
            idEmployee = input()
            db.updateCardFromDatabase(selectedCard, idEmployee)
            print("Powiodło się!")
        else :
            print("Nie ma takiego id karty")

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
