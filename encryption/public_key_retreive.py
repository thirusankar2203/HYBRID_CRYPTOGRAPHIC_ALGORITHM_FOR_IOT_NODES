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
        firebase_url = f"https://project-final-year-b31d2-default-rtdb.firebaseio.com/publickeys.json"
        response = requests.get(firebase_url)
        data = response.json()
        if data:
            first_key = next(iter(data))
            public_key = data[first_key][receiver_id]
            return public_key
        else:
            print("No data found for", receiver_id)
            return None
    except Exception as e:
        print("Error retrieving data:", e)
        return None

# Main function
def main(ssid, password, recv_id):
    # Connect to WiFi
    connect_wifi(ssid, password)

    # Retrieve data from Firebase
    key = retrieve_data(ssid, password, recv_id)
    return key

# Replace 'Thiru', 'thiru2203', 'ANU' with your WiFi SSID, password, and receiver_id respectively

