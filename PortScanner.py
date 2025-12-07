import socket
import sys
from datetime import datetime

def scan_ports(target_host, start_port, end_port):
    """
    Scans a range of ports on a target host and reports open ports.
    """
    print("-" * 50)
    print(f"Scanning Target: {target_host}")
    print(f"Scanning started at: {datetime.now()}")
    print("-" * 50)

    open_port_count = 0

    start_time = datetime.now()

    try:
        for port in range(start_port, end_port + 1):
            
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)  # Set timeout to 1 second
                result = sock.connect_ex((target_host, port))
                if result == 0:
                    print(f"Port {port}: Open")
                    open_port_count += 1
                sock.close()

            except socket.error:
                print(f"\nCould not check {port}, skipping...")
                continue

    except KeyboardInterrupt:
        print("\nExiting Program !!!!")
        sys.exit()
    except socket.gaierror:
        print("\nHostname could not be resolved. Exiting")
        sys.exit()

    if open_port_count == 0:
        print("No open ports found in the specified range.")

    end_time = datetime.now()
    duration = end_time - start_time
    print("Scan completed in: ", duration)    


if __name__ == "__main__":
    target = input ("Enter the IP Address or hostname: ")
    start_port_input = input ("Enter the starting port number: ")
    end_port_input = input ("Enter the ending port number: ")

    try:
        start_port = int(start_port_input)
        end_port = int(end_port_input)
        if start_port < 0 or end_port > 65535 or start_port > end_port:
            raise ValueError
    except ValueError:
        print("Please enter valid integer port numbers (0-65535).")
        sys.exit()

    scan_ports(target, start_port, end_port)        