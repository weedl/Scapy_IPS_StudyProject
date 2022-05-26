from scapy.all import *

x = sniff(iface='ens33', prn = lambda x: x.show())