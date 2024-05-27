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
      
    account_sid = 'AC0174e42c58355fefe24989236455f8e5'
    auth_token = '3f6b86aac149f69c54457942b1904916'
    recipient = '+919629701158'
    sender = '+12522622106'
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
  

