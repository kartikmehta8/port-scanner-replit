import sys
import socket
from datetime import datetime

target = ""
# Define our target
if len(sys.argv) == 2:
  # Translate hostname to IPv4
  target = socket.gethostbyname(sys.argv[1])
else:
  print("Invalid amount of arguments.")
  print("Syntax: python3 main.py <ip_address>")
  print("Execution for Replit Server | Taking Default IP: 8.8.8.8")
  
  # sys.exit(0)
  target = "8.8.8.8" # For Replit

# Add a pretty banner
print("-" * 50)
print("Scanning Target: " + target)
print("Time Started: " + str(datetime.now()))
print("-" * 50)

try:
  for port in range(50, 85):
    print(f"Scanning port {port}")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
      print(f"Port {port} is open.")
    s.close()

  print("-" * 50)
  print("Time Completed: " + str(datetime.now()))
  print("-" * 50)

except KeyboardInterrupt:
  print("\nExiting program.")
  sys.exit(0)

except socket.gaierror:
  print("\nHostname could not be resolved.")
  sys.exit(0)

except socket.error:
  print("\nCould not connect to the server.")
  sys.exit(0)