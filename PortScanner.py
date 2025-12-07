import socket
import sys
from datetime import datetime

def scan_ports(target_host, start_port, end_port):
    """
    Scans a range of ports on a target host and reports open pors.
    """
    print("-" * 50)
    print(f"Scanning Target: {target_host}")
    print(f"Scanning started at: {datetime.now()}")
    print("-" * 50)

    try:
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Set timeout to 1 second
            result = sock.connect_ex((target_host, port))
            if result == 0:
                print(f"Port {port}: Open")
            sock.close()
    except KeyboardInterrupt:
        print("\nExiting Program !!!!")
        sys.exit()
    except socket.gaierror:
        print("\nHostname could not be resolved. Exiting")
        sys.exit()