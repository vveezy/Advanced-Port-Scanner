"""
Advanced Port Scanner
Soufiane.Z
Copyright (C) 2024 vveezy
Distributed under the GNU General Public License v3.0
"""

import socket
import argparse

def scan_ports(target, start_port, end_port, timeout=2):
    """
    Scan the specified range of ports on the target.
    
    :param target: The IP or hostname of the target to scan.
    :param start_port: The starting port of the range to scan.
    :param end_port: The ending port of the range to scan.
    :param timeout: The timeout for each connection attempt in seconds.
    """
    print(f"Scanning {target} for open ports from {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                result = s.connect_ex((target, port))
                if result == 0:
                    print(f"[+] Port {port} is OPEN")
                else:
                    print(f"[-] Port {port} is CLOSED")
        except socket.error as err:
            print(f"[!] Error scanning port {port}: {err}")
    print("\nScan complete.")

if __name__ == "__main__":
    # Setup argument parser
    parser = argparse.ArgumentParser(description="Advanced Port Scanner")
    parser.add_argument("target", help="The target hostname or IP address.")
    parser.add_argument(
        "-sp", "--start-port", type=int, default=1, help="Start of port range to scan (default: 1)"
    )
    parser.add_argument(
        "-ep", "--end-port", type=int, default=65535, help="End of port range to scan (default: 65535)"
    )
    parser.add_argument(
        "-t", "--timeout", type=int, default=2, help="Connection timeout in seconds (default: 2)"
    )

    args = parser.parse_args()

    # Validate port range
    if args.start_port < 1 or args.end_port > 65535 or args.start_port > args.end_port:
        print("[!] Invalid port range. Please specify a valid range between 1 and 65535.")
    else:
        # Perform port scan
        scan_ports(args.target, args.start_port, args.end_port, args.timeout)
