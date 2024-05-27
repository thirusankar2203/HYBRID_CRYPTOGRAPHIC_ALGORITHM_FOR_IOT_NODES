import urequests as requests
import network
import json

# Function to connect to WiFi
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('WiFi Connected:', wlan.ifconfig())

# Function to send data to Firebase
def send_to_firebase(data):
    firebase_url = "https://project-final-year-b31d2-default-rtdb.firebaseio.com/datas.json"
    response = requests.post(firebase_url, json=data)
    print("Firebase Response:", response.text)

# Main function
def main(ssid,password,sendid,recvid,ciphertext,senderpublickey):
    ssid = ssid
    password = password

    # Connect to WiFi
    connect_wifi(ssid, password)

    # Sample data to send to Firebase
    data = {"sender_id": sendid, "receiver_id" : recvid, "cipher_text" : ciphertext, "sender_public_key" : senderpublickey}

    # Send data to Firebase
    send_to_firebase(data)
    


