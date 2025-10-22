import sys
import meshtastic
import meshtastic.tcp_interface
import os
from contextlib import redirect_stdout

radio_hostname = "192.168.237.7"
iface = meshtastic.tcp_interface.TCPInterface(radio_hostname)

print ("Please select from the following menu of options")
print ("1: Get all discovered nodes")
print ("2: Search for node by name")
print ("3: Send message to LongFast")
print ("4: Send message to DefSpend")
print ("5: Send message to specified node")
print ("6: Send bell alert to specified node")
print ("7: Exit")

opt = input("Selection: ")

match opt:
    case "1":
        print ("Get All Nodes")
        iface.showNodes(includeSelf=False, showFields=["user.id", "user.longName", "user.shortName", "lastHeard"])
    case "2":
        print ("Search Node")
        nodeList = ""
        with open(os.devnull, 'w') as fnull:
            with redirect_stdout(fnull):
                nodeList = iface.showNodes(includeSelf=False, showFields=["user.id", "user.longName", "user.shortName", "lastHeard"])
        print (type(nodeList))
    case "3":
        print ("Send to LongFast")
        txt = input("Message: ")
        iface.sendText(text=txt, channelIndex=0)
    case "4":
        print ("Send to DefSpend")
        txt = input("Message: ")
        iface.sendText(text=txt, channelIndex=1)
    case "5":
        print ("Send to Node")
        node = input("Node ID: ")
        txt = input("Message: ")
        iface.sendText(text=txt, destinationId=node)
    case "6":
        print ("Ring Node")
        node = input("Node ID: ")
        iface.sendText(text="0x07", destinationId=node)
    case "7":
        print ("Goodbye!")
        exit
    case _:
        print ("Not An Option!")

iface.close