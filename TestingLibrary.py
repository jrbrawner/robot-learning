import pyshark
from Typing import PacketRef

class TestingLibrary:

    def __init__(self):
        ROBOT_LIBRARY_VERSION = 0.1


    def print_hello(self):
        print("hello world")

    def open(self):
        file = pyshark.FileCapture('pcaps/ipv4frags.pcap')
        something = file[0].__dict__
        packet_ref = PacketRef(
            layers=something['layers'],
            frame_info=something['frame_info'],
            number=something['number'],
            interface_captured=something['interface_captured'],
            captured_length=something['captured_length'],
            length=something['length'],
            sniff_timestamp=str(['sniff_timestamp'])
        )
        
        print(packet_ref.layers[0].field_names)
        print(packet_ref.layers[0].get_field('dst'))
        


test = TestingLibrary()

test.open()
