from scapy.all import sniff


#NEEDED FOR WINDOWS : https://nmap.org/npcap/#download

# Number of records to be sniffed
COUNT = 50

## Define our Custom Action function
def custom_action(packet):
    #get destination keys
    print(packet[0][1].dst)

## Setup sniff, filtering for IP traffic
sniff(filter="ip", prn=custom_action, count = COUNT)

