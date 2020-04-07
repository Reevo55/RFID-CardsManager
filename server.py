import paho.mqtt.client as mqtt
import sqlite3 as db
from datetime import datetime

broker = "127.0.0.1"
server = mqtt.Client()

def connect_to_broker():
    server.connect(broker)
    server.on_message = receive_message
    server.loop_start()
    server.subscribe("terminal")

def checkCursorEmpty(cursor):
    for cursor in cursor.fetchall():
        return False
    return True

def disconnect():
    server.loop_stop()
    server.disconnect()

def addReading(cursor, decodedMessage, date):
    for card in cursor.fetchall():
        idCard = card[0]

    data = (date, str(decodedMessage[2]), str(idCard))
    cursor.execute("INSERT INTO Readings(Date, WentIn, IdCard) VALUES (?, ?, ?)", data)
    print("Dodanie odczytu przebiegło pomyślnie")

def addAnonymousCard(cursor, rfid):
    cursor.execute("INSERT INTO Cards (Identifier) VALUES (?)", (rfid,))
    

def receive_message(client, data, message):
    message_decoded = (str(message.payload.decode("utf-8"))).split(".")

    if message_decoded[0] != "Client connected" and message_decoded[0] != "Client disconnected":
        date = datetime.now()

        print("RFID: " + message_decoded[0]+ ", " + message_decoded[1] + " terminal. Godzina: " + str(date))
        
        conn = db.connect('idReaderDatabase.db')
        c = conn.cursor()   
        c.execute("SELECT * FROM Cards WHERE Identifier = ?", (message_decoded[0],))

        if not checkCursorEmpty(c):
            addReading(c, message_decoded, date)
        else: 
            addAnonymousCard(c, message_decoded[0])
            c.execute("SELECT * FROM Cards WHERE Identifier = ?", (message_decoded[0],))
            addReading(c, message_decoded, date)
        
        conn.commit()
    else:
        print(message_decoded[0] + ":" + message_decoded[1]) 


def main():
    connect_to_broker()
    while(True):
        print("Nacisnij 1 aby zamknac.")
        
        userInput = input()

        if userInput == "1":
            break
    
        

main()