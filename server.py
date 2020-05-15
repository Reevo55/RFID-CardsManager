import paho.mqtt.client as mqtt
import sqlite3 as db
from datetime import datetime

port=8883
broker = "DESKTOP-KPVCDVG" 
server = mqtt.Client()

def connect_to_broker():
    server.tls_set("C:\Program Files\mosquitto\certs\ca.crt") 
    server.username_pw_set(username='server', password='1')
    server.connect(broker, port)
    server.on_message = receive_message
    server.loop_start()
    server.subscribe("worker/name")

def disconnect():
    server.loop_stop()
    server.disconnect() 

def checkCursorEmpty(cursor):
    for cursor in cursor.fetchall():
        return False
    return True

def receive_message(client, data, message):
    message_decoded = (str(message.payload.decode("utf-8"))).split(".")

    if message_decoded[0] != "Client connected" and message_decoded[0] != "Client disconnected":
        date = datetime.now()        
        conn = db.connect('idReaderDatabase.db')
        c = conn.cursor()   
        c.execute("SELECT * FROM Cards WHERE Identifier = ?", (message_decoded[0],))

        idCard = -1 
        wentIn = str(message_decoded[2])

        for card in c.fetchall(): 
            idCard = str(card[0])
        
        print("RFID: " + message_decoded[0]+ ", " + message_decoded[1] + " terminal. Godzina: " + str(date))

        if idCard != -1:         
            query = "INSERT INTO Readings(Date, WentIn, IdCard) VALUES (?, ?, ?)"
            c.execute(query, (date,wentIn, idCard))

            print("Dodanie odczytu przebiegło pomyślnie")
        else: 
            c.execute("INSERT INTO Cards (Identifier) VALUES (?)", (message_decoded[0],))
            c.execute("SELECT * FROM Cards WHERE Identifier = ?", (message_decoded[0],))

            for card in c.fetchall(): 
                idCard = str(card[0])

            query = "INSERT INTO Readings(Date, WentIn, IdCard) VALUES (?, ?, ?)"
            c.execute(query, (date, wentIn, idCard))

            print("Dodanie anonimowej karty")
    
        conn.commit()
        # conn.close()
    else:
        print(message_decoded[0] + ":" + message_decoded[1]) 


def main():
    print("Serwer uruchomiony!")
    connect_to_broker()
    while(True):
        print("Nacisnij 1 aby zamknac.")
        
        userInput = input()

        if userInput == "1":
            break
    
main()