from ctypes import*
import struct
import sys
import os
import socket
class UDP (structure):
    _fields_=[
        ("src",c_ushort),
        ("dst",c_ushort),
        ("len",c_short),
        ("check",c_short),
        ]
    def _new_(self,socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)
    def _init_(self,socket_buffer=None):
        self.src_address=socket.inet_ntoa(struct.pack("@I",self.src))
        self.dest_address=socket.inet_ntoa(struct.pack("@I",self.dest))
        
rawfile=open("udp.bin","rb").read()

udp = UDP (rawfile[0:20])

print(udp.src_address)

