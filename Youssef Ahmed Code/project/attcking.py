import os
# Create a PortScanner object
nm = nmap.PortScanner()
# Perform a scan on the localhost for ports 22 to 443
nm.scan('127.0.0.1', '22-443')
# Print the command line used for the scan
print(nm.command_line())
# Print scan information
print(nm.scaninfo())
# Print all hosts found
print(nm.all_hosts())
# Print the state of the localhost
print(nm['127.0.0.1'].state())
# Print all protocols used
print(nm['127.0.0.1'].all_protocols())
# Print all open TCP ports
print(nm['127.0.0.1']['tcp'].keys())
# Check if a specific port is open
print(nm['127.0.0.1'].has_tcp(22))