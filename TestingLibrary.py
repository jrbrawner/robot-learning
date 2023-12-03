import pyshark
from pyshark.packet.packet import Packet

class TestingLibrary:

    def __init__(self):
        ROBOT_LIBRARY_VERSION = 0.1


    def print_hello(self):
        print("hello world")

    def read_pcap(self):
        file = pyshark.FileCapture('pcaps/ipv4frags.pcap')
        packet = file[1]
        packet : Packet

        assert packet.layers[0].get_field('src') == '08:00:27:fc:6a:c9'
