"""Simple Port Scanner
=======================

This script performs a basic TCP port scan against a target host. It accepts a
host (hostname or IP address) and a port range, then attempts to connect to
each port in that range using Python's built-in `socket` library. Open ports
are reported on the console.

Usage::

    python port_scanner.py 127.0.0.1 1 1024

This will scan ports 1 through 1024 on localhost. If no port range is
provided, the scanner defaults to the first 1000 ports. Error handling is
included to gracefully handle unreachable hosts or ports.

This project demonstrates network fundamentals and is a great addition to a
cybersecurity portfolio. Port scanning is a common technique used by
penetration testers and security professionals to discover services running on
a machine. Be sure to only scan hosts you own or have permission to test.
"""

import socket
import sys
from typing import Tuple


def parse_args(args: list[str]) -> Tuple[str, int, int]:
    """Parse command-line arguments.

    Args:
        args: A list of command-line arguments (excluding the program name).

    Returns:
        A tuple containing the host, starting port, and ending port.

    Raises:
        SystemExit: If the arguments are invalid.
    """
    if len(args) == 0:
        print("Usage: python port_scanner.py <host> [<start_port> <end_port>]")
        raise SystemExit(1)

    host = args[0]
    start_port = 1
    end_port = 1000
    if len(args) == 3:
        try:
            start_port = int(args[1])
            end_port = int(args[2])
        except ValueError:
            print("Port numbers must be integers.")
            raise SystemExit(1)
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("Invalid port range. Ports must be between 1 and 65535 and start_port <= end_port.")
            raise SystemExit(1)
    elif len(args) != 1:
        print("Usage: python port_scanner.py <host> [<start_port> <end_port>]")
        raise SystemExit(1)
    return host, start_port, end_port


def scan_port(host: str, port: int) -> bool:
    """Attempt to connect to a host on a specific port.

    Args:
        host: The target host.
        port: The port to scan.

    Returns:
        True if the connection succeeds (port open), False otherwise.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)
        try:
            result = sock.connect_ex((host, port))
            return result == 0
        except (OSError, socket.error):
            return False


def main() -> None:
    host, start_port, end_port = parse_args(sys.argv[1:])
    print(f"Scanning {host} from port {start_port} to {end_port}...")
    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            open_ports.append(port)
            print(f"Port {port} is open")
    if not open_ports:
        print("No open ports found in the specified range.")
    else:
        print(f"\nScan complete. Open ports: {open_ports}")


if __name__ == "__main__":
    main()
