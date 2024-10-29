import ipaddress
import binascii

ADDRESSES=['192.168.31.66','fe80::e8f8:ead:91f:75c0','211.46.131.11']

for ipaddr in ADDRESSES:
    addr = ipaddress.ip_address(ipaddr)
    print(f'IP address: {addr!r}')
    print('IP version',addr.version)
    print('Packed addr:',binascii.hexlify(addr.packed))
    print("Integer addr:",int(addr))
    print("Is private:",addr.is_private)
    print("=====================")