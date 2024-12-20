#!/user/bin/python3

import nmap 

#Initialize the PortScanner object
scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("<--------------------------------------------------->")

#Takes in user input a IP address and returns IP address and type
ip_addr = input("Please enter the IP address you want to scan:")
print("The Ip you entered is:", ip_addr)
type(ip_addr)

#Takes in user input as 1-3 and returns response
resp = input(""" \n Please enter the type of scan you want to run
                  1)SYN ACK Scan
                  2)UDP Scan
                  3)Comprehensive Scan \n""")
print("You have selected options:", resp)

#Print scan results, check if TCP ports are open. Provides verbose responses
if resp =='1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2': 
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
else: 
    print("Please enter a valid option")
