from ctypes import *
import struct
import sys
import os
import socket

class IP(Structure):
    _fields_=[
        ("version",c_ubyte, 4),
        ("ihl",c_ubyte, 4),
        ("tos",c_ubyte),
        ("length",c_ushort),
        ("ident",c_ushort),
        ("offset",c_ushort),
        ("ttl",c_ubyte),
        ("protocol",c_ubyte),
        ("checksum",c_ushort),
        ("src",c_long),
        ("dest",c_long)
        ]
    
    def _new_(self,socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)
    def _init_(self,socket_buffer=None):
        self.src_address=socket.inet_ntoa(struct.pack("@I",self.src))
        self.dest_address=socket.inet_ntoa(struct.pack("@I",self.dest))
host = ''
r=socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.hton(0*800))
Eathernet
r.setsocket(socket.SOL_SOCKET,socket.SO_REUSEADDR)
r.bind('host',0))

while True:
	data=r.recvfrom(65565)[0]
	ip = ip_header(data)
	
	print("source Address" + ip.src_address + ": " + "destination address" + ip.dst_address)

rawfile=open("ip.bin","rb").read()

ip = IP(rawfile[0:20])

print(ip.src_address)

