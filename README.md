# Port Scanner

A small Python script that scans a list of common ports on a target IP and reports which ports respond. Intended as an educational/lab tool to demonstrate basic socket scanning and simple OS-guessing via TTL values.

## Features

* Scans a pre-defined list of common and interesting ports
* Attempts to detect alive/open ports by sending probes and waiting for responses
* Parses TTL from responses to produce a very rough OS guess (based on a small TTL mapping)
* Single-file, no external libraries required (uses Python standard `socket` and `struct`)

## How to Run

1. Save the script as `pscanner.py`.
2. Run the script with a target IP or hostname:

```bash
python pscanner.py <target-ip>
# Example:
python pscanner.py 192.168.1.10
```

3. The script will iterate the hard-coded `common_ports` list and print any ports that respond.

## Notes

* This script is a minimal educational scanner — it is **not** a full-featured port scanner like `nmap`.
* The included `common_ports` list contains typical service ports plus a few "interesting" ports; edit it to match your needs.
* The script as provided expects the target IP as a command-line argument. You may need to fix small issues before running (e.g., ensure `argv` is imported/used from `sys`, initialize the socket `s`, and define the `OS_TTL` mapping used for TTL-based OS guesses).
* Scanning other people's hosts without permission may be illegal or against terms of service — only scan machines you own or are explicitly allowed to test.
* Improvements you may add later: threaded scanning for speed, proper TCP connect/UDP checks, configurable port ranges, timeout handling, and more accurate OS fingerprinting.
