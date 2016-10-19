#! /usr/bin/env python

"""
Collects RTT metrics based on ICMP
Usage: python pyngcollector <dest> <num_packet>
    - dest: the destination
    - num_packet: the number of ICMP packets
Output:
    - avg: the average RTT time in ms
    - max: the max RTT time in ms
    - min: the min time in ms
    - lost: the number of packets lost
"""

import sys
from scapy.all import sr,IP,ICMP,conf
from datetime import datetime, time
import logging

def get_times(ans):
    for pack in ans:
        yield pack[1].time - pack[0].sent_time

if __name__ == '__main__':
    # sssssh
    conf.verb=0
    dest = sys.argv[1] if len(sys.argv) > 1 else 'google.com'
    num_packet = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    # constructs the ICMP packet
    p=IP(dst=dest,ttl=50)/ICMP()
    # sends 10 of them.
    ans,unans = sr(p*num_packet)

    l = list(get_times(ans))
    avg_time = sum(l)/len(l) if l else None
    max_time = max(l)
    min_time = min(l)

    print 'avg: {:03.3f} ms'.format(avg_time*1000)
    print 'max: {:03.3f} ms'.format(max_time*1000)
    print 'min: {:03.3f} ms'.format(min_time*1000)
    print 'lost: {:d} packets'.format(len(unans))
