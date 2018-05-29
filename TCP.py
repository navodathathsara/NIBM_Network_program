from ctypes import*
import struct
import sys
import os
import socket
class TCP (structure):
    _fields_=[
        ("src",c_ushort),
        ("dst",c_ushort),
        ("seqq",c_long),
        ("ack",c_long),
        ("off",c_ubyte,4),
        ("res",c_ubyte,4),
        ("flag",c_ubyte),
        ("win",c_ushort),
        ("check",c_ushort),
        ("urg",c_ushort),
        ]
    def _new_(self,socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)
    def _init_(self,socket_buffer=None):
        self.src_address=socket.inet_ntoa(struct.pack("@I",self.src))
        self.dest_address=socket.inet_ntoa(struct.pack("@I",self.dest))
        
rawfile=open("udp.bin","rb").read()

udp = TCP (rawfile[0:20])

print(tcp.src_address)

