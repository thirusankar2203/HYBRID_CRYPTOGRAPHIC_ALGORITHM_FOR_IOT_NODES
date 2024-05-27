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

# Function to retrieve data from Firebase
def retrieve_data(ssid, password, receiver_id):
    try:
        firebase_url = f"https://project-final-year-b31d2-default-rtdb.firebaseio.com/datas.json?orderBy=%22receiver_id%22&equalTo=%22{receiver_id}%22&limitToLast=1"
        response = requests.get(firebase_url)
        data = response.json()
        if data:
            first_key = next(iter(data))
            cipher_text = data[first_key]['cipher_text']
            sender_public_key = data[first_key]['sender_public_key']
            send_id = data[first_key]['sender_id']
            
        else:
            print("No data found.")
        return cipher_text,sender_public_key,send_id
    except Exception as e:
        print("Error retrieving data:", e)
        return None

# Main function
def main(ssid, password, recv_id):
    # Connect to WiFi
    connect_wifi(ssid, password)

    # Retrieve data from Firebase
    text,key,sendid = retrieve_data(ssid, password, recv_id)
    return text,key,sendid



