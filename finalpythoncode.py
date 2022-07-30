#IBM Watson IOT Platform
#pip install wiotp-sdk
import wiotp.sdk.device
import time
import random
myData={}
myConfig = { 
    "identity": {
        "orgId": "dq6ptm",
        "typeId": "pipeleakage",
        "deviceId":"099099"
    },
    "auth": {
        "token": "7995893956"
    }
}
 
    

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    if m=="Mainon":
        print("MAIN VALVE IS TURNED ON")
    elif m=="Mainoff":
        print("MAIN VALVE IS TURNED OFF")
    if m=="Node1on":
        print("NODE1 IS TURNED ON")
    elif m=="Node1off":
        print("NODE1 IS TURNED OFF")
    
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    Main=100
    node1=random.randint(90,100)
    node2=random.randint(90,100)
    myData={'d':{'Id':"GUDLAVALLERU_WATER_PIPELINE_LEAKAGE_DETECTION_SYSTEM",'Main':Main, 'node1':node1, 'node2':node2}}
    
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    M=(myData['d']['Main'])
    N1=(myData['d']['node1'])
    N2=(myData['d']['node2'])
    if(M!=N1):
        print("Lekage detected between Main & Node1")
        print("Please Turn Off Main Valve")
    elif(N2!=N1):
        print("Lekage detected between Node1 & Node2")
        print("Please Turn Off Nodel")
    client.commandCallback = myCommandCallback
 
    time.sleep(10)
client.disconnect()
