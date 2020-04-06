import paho.mqtt.client as mqtt

broker = "127.0.0.1"

print("Podaj identyfikator tego terminalu: ")
terminal_id = input()
client = mqtt.Client()

def scanCard(rfid_identifier):
    client.publish("terminal", rfid_identifier + "." + terminal_id,)

def connect_to_broker():
    client.connect(broker)
    scanCard("Client connected")


def disconnect_from_broker():
    scanCard("Client disconnected")
    client.disconnect()

def main():
    connect_to_broker()

    while(True):
        print("Nacisnij 1 aby dodac odczyt. 0 żeby zamknąć")
        
        userInput = input()

        if userInput == "1":
            print("Podaj kod RFID karty (identyfikator):")
            rfid = input()
            scanCard(rfid)
        elif userInput == "0":
            break

    disconnect_from_broker()


main()