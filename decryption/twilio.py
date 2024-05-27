try:
  import urequests as requests
except:
  import requests
  
import network
import esp
esp.osdebug(None)

import gc
gc.collect()

# Your Account SID and Auth Token from twilio.com/console


def send_sms(message):
      
    account_sid = 'AC2220ae2a06fb676f15ef6dcd7e7580f9'
    auth_token = '48136faffd5fdb03aab1916972fae1e2'
    recipient = '+918807342948'
    sender = '+13344893920'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = "To={}&From={}&Body={}".format(recipient,sender,message)
    url = "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json".format(account_sid)
    
    print("Trying to send SMS with Twilio")
    
    response = requests.post(url,
                             data=data,
                             auth=(account_sid,auth_token),
                             headers=headers)
    
    if response.status_code == 201:
        print("SMS sent!")
    else:
        print("Error sending SMS: {}".format(response.text))
    
    response.close()

def connect_wifi(ssid, password):
  station = network.WLAN(network.STA_IF)
  station.active(True)
  station.connect(ssid, password)
  while station.isconnected() == False:
    pass

  send_sms(station.ifconfig()[0])
  
