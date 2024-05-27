from BlynkLib import Blynk
import time
import network
def connect_wifi(ssid,password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('WiFi Connected:', wlan.ifconfig())



def main(ssid,password,temp,humi):
    connect_wifi(ssid,password)
    # Blynk credentials
    BLYNK_AUTH_TOKEN = "OKdeujZ30MFh5uTXLi1Sp7U-CZtIgs2g"

    # Initialize Blynk
    blynk = Blynk(BLYNK_AUTH_TOKEN)
    try:
        blynk.virtual_write(0,temp)
        blynk.virtual_write(1,humi)
        # Read sensor data (assuming text data)
             # Example text data
        
        # Send numerical data to Blynk server
        #blynk.virtual_write(0, numerical_data)  # Assuming V1 is the virtual pin for the graph
        
        # Process Blynk events
        blynk.run()
        
        time.sleep(2)
    except Exception as e:
        print("Error:", e)
        
    