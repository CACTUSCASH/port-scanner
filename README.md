# Port Scanner

This project provides a **simple TCP port scanner** implemented in pure Python. It
allows you to quickly discover open ports on a target host by attempting to
establish TCP connections. Port scanning is a fundamental technique used by
penetration testers and security professionals to map network services.

## Features

- Scan a single host over a configurable port range (default: ports 1–1000)
- Reports open ports as they are found
- Graceful error handling for unreachable hosts or invalid port ranges
- No third‑party dependencies

## Usage

Run the script from the command line, specifying the target host and
optionally a start and end port:

```bash
python port_scanner.py <host> [<start_port> <end_port>]

# examples
python port_scanner.py 192.168.1.10      # scan common ports
python port_scanner.py example.com 1 1024  # scan ports 1–1024
```

**Note:** Only scan systems you own or have permission to test.

## Why this matters

Understanding how to enumerate network services is a key skill in
cybersecurity. This simple scanner demonstrates socket programming and can be
expanded into more advanced tools. It makes a great addition to your GitHub
portfolio when applying for internships or security roles.
