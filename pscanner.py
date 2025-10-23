import socket
import struct

ip_dest = argv[1]

common_ports = [80, 137, 433, 123, 138, 1434, 445, 136, 67, 23, 21, 139, 22, 68, 8080, 8433, 8080, 25, 111, 110, 998, 53, 2222, 135, 3306, 2049, 1433, 3456, 443, 7, 5900]

for port in common_ports:
    dest_addr = (ip_dest, port)
    s.sendto(b"", dest_addr)

    try:
        data, addr = s.recvfrom(1024)
        ttl = struct.unpack("!B", data[8:9])[0]

        os_guess = None
        for os_name, os_ttl in OS_TTL.items():
            if ttl == os_ttl:
                os_guess = os_name
                break


      print(f"{addr[0]}:{addr[1]} is open (TTL: {ttl}, likely OS: {os_guess})")
    except socket.timeout:
        pass

s.close()
