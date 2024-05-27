import usocket as socket
import network

def wificonnect(ssid,password):
    # Connect to WiFi
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(ssid, password)

    # Wait until connected
    while not wifi.isconnected():
        pass

    # Print the IP address
    print("Connected to WiFi. IP address:", wifi.ifconfig()[0])
    
    


# <!DOCTYPE html>
# <html>
# <head>
#   <title>Input Form</title>
#   <style>
#     body{
#       background-color: burlywood;
#     }
#     .page{
#       text-align: center;
#       font-size: 200%;
#     }
#     h1{
#       text-align: center;
#       font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
#       font-size: 250%;
#     }
#     #text{
#       font-family: monospace;
#     }
#     input{
#       font-size: 100%;
#       font-family:system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
#     }
# 
#   </style>
# </head>
# <body>
#   <h1>HYBRID CRYPTOGRAPHIC ALGORITHM</h1> <h1>FOR IOT NODES</h1>
#   <br>
# <form action="/submit" method="post">
#   <div class="page">
#     <p id="text">Enter the receiver ID : </p><input type="text" name="recvid"><br>
#     <br><input type="submit" value="Submit">
#   </div>
# 
# </form>
# </body>
# </html>
# Define HTML form
html = """


<!DOCTYPE html>
<html>
<head>
    <title>Input Form</title>
    <style>
        body {
          background-image: url('https://tresorit.com/blog/content/images/size/w2000/2021/09/e2ee.png');
          background-repeat: no-repeat;
          background-attachment: fixed;  
          background-size: cover;
          background-position: center;

        }

        p{
            font-family:monospace;
            color:mintcream;
            font-size: 220%;
        }

        form{
            text-align: center;
        }

        input{
            font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
            font-size: 180%;
            color: black;
        }

        input[type="text"] {
            border: 2px solid #ffffff; /* White border */
            border-radius: 5px; /* Rounded corners */
            background-color: rgba(255, 255, 255, 0.8);
            padding: 8px;
            color: #333333;
        }

        input[type="text"]:hover {
            border-color:darkred; /* Lighter border color on hover */
        }

    </style>
</head>
<body>
    <br><br>
    <form action="/submit" method="post">
        <p><b>Enter the Receiver ID : </b></p><input type="text" name="recvid" id="left"><br>
        <br><br>
        <input type="submit" value="Submit">
    </form>
    
</body>
</html>
"""

# Define request handler
    
def handle_request(client):
    list=[]
    request = client.recv(1024)
    method, path, *_ = request.decode().split('\r\n')[0].split()
    
    if method == "GET" and path == "/":
        client.send(html)
    elif method == "POST" and path == "/submit":
        data = request.decode().split('\r\n')[-1]
        input_data = data.split('&')
        recvid_list=input_data[0].split('=')
        recvid=recvid_list[1]

        list.append(recvid)
        
        # Return iv and plaintext as a tuple
    else:
        client.send("404 Not Found")

    return list
    

# Create server
server = socket.socket()
server.bind(('0.0.0.0', 80))
server.listen(5)

# Main loop
def main(ssid,password):
    wificonnect(ssid,password)
    while True:
        data=[]
        client, addr = server.accept()
        data=handle_request(client)
        if data:
            break
        client.close()
        
    
    return data

