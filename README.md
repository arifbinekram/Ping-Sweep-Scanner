# Ping Sweep Scanner

The IP Scanner is a Python script designed to scan a range of IP addresses and identify live hosts within that range. It sends ICMP echo requests (pings) to each IP address in the specified range and checks for responses to determine if the host is live.

## Features

- Scans a range of IP addresses to identify live hosts.
- Uses ICMP echo requests (pings) to check for responses.
- Supports specifying a range of IP addresses to scan.

## Requirements

- Python 3.x
- Scapy library

## Installation

1. **Install Python 3:**
   If you haven't already, install Python 3 on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Install Scapy:**
   Install the Scapy library using pip:
   ```
   pip install scapy
   ```

3. **Download the Script:**
   Download the `scanner.py` script from this repository.

## Usage

Run the script with two IP addresses as arguments to specify the range of IP addresses to scan:
```
python3 scanner.py start_ip_addr end_ip_addr
```
Replace `start_ip_addr` and `end_ip_addr` with the starting and ending IP addresses of the range you want to scan, respectively.

For example:
```
python3 scanner.py 192.168.1.1 192.168.1.10
```

## Troubleshooting

- **Permission Denied Error:** If you encounter a "Permission Denied" error, try running the script with administrative privileges using `sudo`:
  ```
  sudo python3 scanner.py start_ip_addr end_ip_addr
  ```

- **Network Configuration:** Ensure that your network configuration allows ICMP echo requests (pings) and responses. Firewalls and network settings may block or filter ICMP traffic.

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.


---

**Note:** This script is intended for educational and testing purposes only. Ensure that you have the necessary permissions before scanning any network.
```

Feel free to modify this template to better fit your project's specifics or add any additional information you think would be useful for users.
