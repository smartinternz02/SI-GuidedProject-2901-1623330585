import time
import sys
import ibmiotf.application
import ibmiotf.device
import datetime
import json

#Provide your IBM Watson Device Credentials
organization = "3vmhl1"
deviceType = "IOT"
deviceId = "1001"
authMethod = "token"
authToken = "1234567890"

try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        dtym=datetime.datetime.now().strftime("%d-%m-%y-%H-%M")
        time.sleep(10)      
        data = { 'device1' :"Xray machine", 'location1':"block1",'device2': "ecgmachine" ,"location2": "block2","dtym":dtym}
        print(data)
        def myOnPublishCallback():
            print ("Published data to IBM Watson")

        success = deviceCli.publishEvent("Data", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(1)
        
