import paho.mqtt.client as mqtt

broker = "127.0.0.1"

print("Podaj identyfikator tego terminalu: ")
terminal_id = input()
client = mqtt.Client()
print("Podaj czy to wejsciowy terminal (1) czy wyjsciowy (0)")
entryTerminal = input()
if not (entryTerminal == "1" or entryTerminal == "0"):
    print("Blad podania! Ustawiam terminal na wejsciowy!")
    entryTerminal = "0"

def scanCard(rfid_identifier):
    client.publish("terminal", rfid_identifier + "." + terminal_id + "." + str(entryTerminal),)

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