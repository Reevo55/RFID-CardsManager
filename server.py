import paho.mqtt.client as mqtt

broker = "127.0.0.1"
server = mqtt.Client()


def connect_to_broker():
    server.connect(broker)
    server.on_connect = on_connect
    server.on_message = receive_message
    server.loop_start()
    server.subscribe("terminal")

def on_connect(client, userdata, flags, rc, properties=None): 
    print("Connect " + client + " " + userdata + " " + flags + " " + rc + " " + properties)


def disconnect():
    server.loop_stop()
    server.disconnect()

def receive_message(client, data, message):
    message_decoded = (str(message.payload.decode("utf-8"))).split(".")

    if message_decoded[0] != "Client connected" and message_decoded[0] != "Client disconnected":
        print("RFID: " + message_decoded[0]+ ", " + message_decoded[1] + " terminal.")
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